"""Confere invariantes da tradução; execute na raiz do checkout.

Por padrão verifica as seções disponíveis. --complete exige a cobertura total.
Não avalia fidelidade linguística nem substitui revisão ou testes no navegador.
"""

import argparse
import json
import re
from pathlib import Path

import yaml


def sections(language):
    tree = yaml.safe_load(Path(f"chapters/{language}/_toctree.yml").read_text())
    return [section for unit in tree for section in unit["sections"]]


def quiz_structure(content):
    """Remove somente strings de apresentação, mantendo lógica e ordem."""
    questions = re.findall(r"<Question\b.*?/>", content, flags=re.S)
    return [
        re.sub(
            r'(text|explain):\s*"(?:[^"\\]|\\.)*"',
            r'\1: ""',
            question,
        ).split()
        for question in questions
    ]


def verify(complete=False):
    source = sections("en")
    translated = sections("pt-BR")
    expected = [s["local"] for s in source]
    actual = [s["local"] for s in translated]
    assert len(actual) == len(set(actual)), "Entradas duplicadas no índice"
    assert actual == [p for p in expected if p in actual], "Ordem ou caminhos divergentes"
    if complete:
        assert actual == expected, "Cobertura incompleta"
    results = []
    for section in translated:
        path = section["local"]
        en = Path("chapters/en", path + ".mdx").read_text()
        pt = Path("chapters/pt-BR", path + ".mdx").read_text()
        code = r"```[^\n]*\n.*?\n```"
        assert re.findall(code, en, re.S) == re.findall(code, pt, re.S), path
        urls = r'https?://[^\s<>"\)]+'
        assert re.findall(urls, en) == re.findall(urls, pt), (path, "URLs")
        assert quiz_structure(en) == quiz_structure(pt), (path, "lógica dos quizzes")
        assert len(re.findall(r"^#{1,6} ", en, re.M)) == len(
            re.findall(r"^#{1,6} ", pt, re.M)
        ), (path, "títulos")
        reference = next(s for s in source if s["local"] == path)
        assert section.get("quiz") == reference.get("quiz"), (path, "índice do quiz")
        assert "{{CODE_" not in pt, (path, "marcador não expandido")
        results.append({"path": path, "invariants": "passed"})
    return {
        "available": len(actual),
        "total": len(expected),
        "missing": [p for p in expected if p not in actual],
        "results": results,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--complete", action="store_true")
    args = parser.parse_args()
    print(json.dumps(verify(args.complete), ensure_ascii=False, indent=2))
