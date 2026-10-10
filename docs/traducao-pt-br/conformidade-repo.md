# Conferência das orientações do repositório

Revisão em 10 de outubro de 2026, na mesma tarefa e branch. HEAD auditado: `967d8369c3bb19c6dc9aba905d3b9fafc271bbf1`. O `main` remoto continua em `56b6e8334aef7e0efa0137574f068c968f3f6e1c`, a referência da tradução. Não houve mudança na referência que exigisse retradução.

Foram procurados `AGENTS.md` na raiz, nos ancestrais `/` e `/workspace` e em todos os diretórios do checkout, incluindo arquivos ocultos e ignorados: nenhum foi encontrado. Não há `CONTRIBUTING` ou outro guia geral de tradução. Foram lidos `README.md`, `Makefile`, `requirements.txt`, todos os workflows, `.github/ISSUE_TEMPLATE/translations.md`, o formatador, o validador, o gerador de notebooks e o objetivo/plano. O acordo em `chapters/ru` é específico da tradução russa, fora dos diretórios aplicáveis ao português.

| Orientação e fonte | Conferência da entrega |
| --- | --- |
| README: código de idioma em formato de duas letras e região | Diretório existente `chapters/pt-BR`, no formato admitido |
| README: alterar somente `title` no índice; incluir somente seções traduzidas | Comparação recursiva dos dois YAMLs removendo apenas `title`: todos os demais campos são idênticos; 50 arquivos disponíveis na mesma ordem |
| README: conferir prévia local | Evidências anteriores preservadas: 50 rotas, inspeção visual de layout e texto, fórmulas, avisos, quizzes e navegação; mídias externas ainda bloqueadas |
| README: instalar `requirements.txt` e executar `make style` | Requisitos conferidos por `pip install --no-index -r requirements.txt` e `pip check`; mesma função `blackify` de `make style` executada nos 50 arquivos de português, sem mudar seus hashes |
| Objetivo/plano: não executar `make style` global; preservar inglês e demais idiomas | Formatação limitada a `pt-BR`; o check global `make quality` passou. A execução global com escrita foi evitada conforme a restrição explícita do objetivo |
| README: habilitar idioma nos dois workflows de build | `pt-BR` já consta em ambos na referência. A instrução de adicionar em ordem alfabética aplica-se a um idioma ausente; não foi necessário adicionar ou reordenar a lista existente |
| CI de qualidade: `make quality` | Executado novamente e aprovado; o CI declara Python 3.8, mas a verificação local usa Python 3.12. Não foi consultado o resultado remoto do CI nesta execução |
| README: gerar notebooks | Lote verificado de 21 notebooks; chamada por idioma usa o gerador existente e evita sua falha conhecida com `chapters/unpublished` sem índice. Células ML não foram executadas |
| Template de tradução: coordenar issue e referenciá-la no PR | Issue upstream de pt-BR identificada por leitura pública: https://github.com/huggingface/audio-transformers-course/issues/173, aberta, com os capítulos de áudio. Não foi publicado comentário de coordenação. O template lista capítulos do curso de NLP, não os 50 do curso de áudio; o índice inglês é a referência autorizada. Não foi inventada issue nem enviado comentário ou mensagem externa |
| README: fork e PR para revisão | Checkout do fork e PR #1 existente, em rascunho; não foi criado PR duplicado. Nenhum merge ou deploy |

A orientação de participação no Discord é de coordenação com a comunidade upstream e não demonstra qualidade da tradução. A associação ao servidor não foi executada. A descrição de envio upstream referencia a issue #173. Não foi possível publicar o PR oficial pela API, e o CI remoto continua sem confirmação.

Nesta revisão, não foram encontrados desvios novos nos arquivos do curso. As correções necessárias ficaram nos registros: a descrição remota do PR correspondente ao commit auditado já havia sido publicada e lida pelo conector autorizado no thread de origem, conforme a delegação recebida. Essa publicação anterior está resolvida. A descrição ampliada com esta conferência está preparada em `descricao-pr.md` para publicação pelo mesmo acompanhamento; o conector continua ausente nesta execução.

Evidências locais adicionais: `validation/repo-instructions.json` (inclui hashes dos 50 arquivos), `repo-requirements.log`, `repo-quality.log`, `repo-invariants.json` e `repo-translation-validator.log`, sob `/workspace/.onboarding/audio-transformers-course/`. A saída do validador foi lida e informa ausência de seções faltantes; não se usou apenas seu código de saída.

A tradução e as revisões locais permanecem completas. Mídias/links externos e os dois links relativos defeituosos herdados do inglês continuam pendentes. O sucesso da compilação não elimina esses limites nem substitui a revisão linguística já registrada. Configuração do ambiente não publicada, rede e credenciais preservadas.
