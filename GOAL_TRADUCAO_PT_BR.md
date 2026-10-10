# Goal: tradução integral do Audio Transformers Course para pt-BR

Texto para enviar como objetivo. Este arquivo não ativa o comando `/goal`.

```text
/goal Traduza e verifique integralmente o Audio Transformers Course para português brasileiro no checkout /workspace/audio-transformers-course, seguindo PLANO_TRADUCAO_PT_BR.md. Execute você mesmo a tradução e a revisão, em etapas separadas, até cumprir os critérios de conclusão abaixo.

ESCOPO
Use chapters/en/_toctree.yml e os arquivos correspondentes como referência. Confirme a versão do original no início e registre seu SHA. O inventário inicial contém 50 seções: revise e atualize as 10 existentes em pt-BR e traduza as 40 restantes, cobrindo as unidades 0 a 8 e eventos. Inclua índice, títulos, prosa, tabelas, legendas, textos alternativos, avisos, exercícios, quizzes e suas explicações. Exclua chapters/unpublished.

EXECUÇÃO
Comece pelo inventário e por um glossário persistente. Avance na ordem das unidades, concluindo tradução, revisão comparativa bloco a bloco, leitura linguística em português e verificação técnica de cada seção. Use português brasileiro natural, precisão técnica e terminologia consistente. Preserve o significado, a estrutura pedagógica e todas as informações do original, sem resumir. Registre progresso e pendências por seção para retomar o trabalho entre sessões. Continue autonomamente dentro deste escopo; solicite esclarecimento apenas diante de um bloqueio real que não possa resolver com o repositório e o plano.

RESTRIÇÕES
Preserve mudanças existentes do usuário, os arquivos ingleses e os demais idiomas. Preserve identificadores, comandos, APIs, nomes de modelos e conjuntos de dados, fórmulas, valores, entradas e saídas dos exemplos e lógica dos componentes MDX. Traduza comentários e textos de apresentação apenas quando não alterar comportamento. Preserve campos local e URLs; confira e ajuste referências internas que precisem acompanhar títulos traduzidos. Mantenha a ordem das alternativas e as flags correct dos quizzes. Registre defeitos do original separadamente, sem corrigi-los silenciosamente. Use o checkout existente, sem criar worktree. Não publique conteúdo nem faça push ou merge como parte deste objetivo.

VERIFICAÇÃO
Faça você mesmo uma segunda revisão completa de fidelidade e uma revisão linguística separada da redação. Compare cobertura e ordem dos índices, existência dos arquivos, blocos de conteúdo, números, termos, links, código e componentes. Execute make quality, compile todo pt-BR com doc-builder, confira as 50 rotas e inspecione visualmente cada página. Teste as alternativas e explicações dos quizzes. Gere e valide os notebooks de português com nbformat e confira a correspondência dos exemplos. Use create_notebooks por idioma para evitar o defeito conhecido do gerador global em chapters/unpublished. Leia a saída de validate_translation.py, pois código zero não garante cobertura completa. Investigue falhas; não substitua verificações necessárias por checks triviais. Não execute make style globalmente. Treinamento completo e execução de todas as células de ML não são requisitos deste objetivo.

CRITÉRIOS DE CONCLUSÃO
As 50 seções devem estar integralmente traduzidas e revisadas, com índice completo, terminologia consistente e nenhuma pendência de tradução ou erro de renderização conhecido. Registre resultados de cobertura, fidelidade, formatação, compilação, navegação, quizzes e notebooks. Não marque como concluída uma inspeção visual ou outra verificação que não foi executada. Se um bloqueio externo impedir a conclusão, finalize todo trabalho independente possível e reporte precisamente o bloqueio e as etapas pendentes.

ENTREGÁVEIS
Arquivos completos em chapters/pt-BR, índice localizado, glossário, registro de verificação das 50 seções e relatório final com resultados, limitações e problemas encontrados no original. Apresente um resumo das mudanças e das evidências de validação. Não trate sucesso de ferramentas como garantia absoluta de qualidade linguística nem apresente sua própria revisão como revisão independente de outro avaliador.
```
