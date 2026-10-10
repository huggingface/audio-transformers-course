# Plano de tradução e verificação integral para português brasileiro

## Objetivo e responsabilidade

Traduzir integralmente o curso publicado em `chapters/en` para `chapters/pt-BR`, com fidelidade técnica, português brasileiro natural e funcionamento dos componentes do curso. Eu executarei a tradução, a revisão e as verificações, inclusive dos capítulos já traduzidos. A revisão será uma etapa separada da redação, com nova leitura comparativa do original; não será apresentada como avaliação independente por outro revisor.

Este documento planeja o trabalho. Sua criação não significa que os capítulos já foram traduzidos ou revisados.

## Escopo e diagnóstico inicial

- Referência de escopo: `chapters/en/_toctree.yml`, na versão do repositório registrada no início da execução.
- SHA observado no planejamento: `56b6e8334aef7e0efa0137574f068c968f3f6e1c`.
- O índice contém 50 seções, distribuídas pelas unidades 0 a 8 e por eventos. Todos os arquivos referenciados existem em inglês.
- Há 10 seções em português, nas unidades 0 e 1; sua qualidade e atualização precisam ser conferidas integralmente.
- Faltam 40 seções no índice em português.
- O material de referência tem aproximadamente 50.322 palavras por contagem de espaços, incluindo código e marcação. Essa medida indica volume, não quantidade exata de prosa a traduzir.
- Incluem-se índice, títulos, parágrafos, tabelas, legendas, textos alternativos, avisos, exercícios, perguntas, alternativas e explicações dos quizzes, além dos recursos adicionais e eventos.
- `chapters/unpublished` não integra o curso publicado e fica fora deste escopo.
- Mudanças na referência inglesa serão identificadas antes do fechamento; alterações relevantes exigem nova conferência das seções afetadas.

## Critérios editoriais

1. Preservar o significado de cada passagem, sem omissões, resumos ou explicações adicionais que mudem o conteúdo. Registrar problemas do original separadamente.
2. Usar português brasileiro claro, com tratamento por “você” e tom didático consistente.
3. Criar um glossário antes da tradução dos novos capítulos. Adotar inicialmente: *dataset* → conjunto de dados; *sampling rate* → taxa de amostragem; *resampling* → reamostragem; *waveform* → forma de onda; *fine-tuning* → ajuste fino; *inference* → inferência; *pre-trained* → pré-treinado.
4. Explicar termos especializados na primeira ocorrência quando o original os explica. Preservar siglas como ASR, TTS, CTC, WER e CER, com suas denominações em português no contexto adequado. Manter nomes próprios, modelos, APIs e marcas.
5. Preservar identificadores, comandos, nomes de arquivos, modelos, conjuntos de dados, parâmetros, valores numéricos, fórmulas e unidades. Não converter ponto decimal em literais de código.
6. Traduzir comentários e textos de interface dos exemplos somente quando isso não alterar seu comportamento. Preservar transcrições de referência, textos usados como entradas de modelos, saídas reproduzidas e dados usados em métricas; traduzir sua explicação na prosa.
7. Traduzir os textos visíveis dos componentes MDX, inclusive `text` e `explain` nos quizzes, sem alterar chaves, expressões, flags `correct`, ordem das alternativas ou lógica dos componentes.
8. Preservar URLs de destino, nomes dos arquivos e campos `local`. Conferir links internos e âncoras após traduzir títulos; ajustar apenas referências que precisam acompanhar a tradução.
9. Não prometer traduzir textos embutidos nas imagens originais. Traduzir textos alternativos e legendas disponíveis; registrar imagens que precisariam de uma versão localizada.

## Sequência de execução

Cada lote deve terminar com tradução, revisão e verificações antes de avançar. A execução seguirá a ordem pedagógica do curso.

| Lote | Material | Seções | Trabalho principal | Pontos de atenção |
| --- | --- | ---: | --- | --- |
| 0 | Inventário e glossário | — | Registrar SHA da referência, caminhos, estados e termos | Delimitar conteúdo traduzível e elementos preservados |
| 1 | Unidade 0 | 3 | Revisar a tradução existente | Boas-vindas, preparação e comunidade |
| 2 | Unidade 1 | 7 | Revisar e atualizar a tradução existente | Amostragem, espectro, pré-processamento, streaming e quiz |
| 3 | Unidade 2 | 5 | Traduzir e verificar | Pipelines de classificação, ASR e geração de áudio |
| 4 | Unidade 3 | 6 | Traduzir e verificar | CTC, Seq2Seq, classificação e respostas do quiz |
| 5 | Unidade 4 | 5 | Traduzir e verificar | Classificação de música, ajuste fino e Gradio |
| 6 | Unidade 5 | 8 | Traduzir e verificar | Dados de fala, WER/CER, avaliação e API Trainer |
| 7 | Unidade 6 | 7 | Traduzir e verificar | Síntese de fala, SpeechT5, vocoder e avaliação |
| 8 | Unidade 7 | 6 | Traduzir e verificar | Tradução de fala, assistente e transcrição de reuniões |
| 9 | Unidade 8 e eventos | 3 | Traduzir e verificar | Conclusão, certificado e eventos |
| 10 | Curso completo | 50 | Revisão transversal e validação final | Terminologia, cobertura, navegação e renderização |

Nas unidades extensas, trabalhar seção por seção. A unidade 5 terá três etapas internas: introdução/modelos/dados; avaliação/ajuste fino; demonstração/exercício/recursos. A unidade 7 será revisada por aplicação. A divisão não reduz o escopo de verificação.

## Procedimento obrigatório por seção

1. Ler o original completo e identificar conceitos, dependências e elementos que devem ser preservados.
2. Traduzir ou revisar o arquivo correspondente em `pt-BR`, mantendo a estrutura pedagógica e a marcação.
3. Fazer uma segunda leitura comparativa, bloco a bloco: títulos, parágrafos, listas, tabelas, avisos, exercícios e componentes. Conferir especialmente negações, condições, comparações, números e instruções.
4. Fazer uma leitura contínua somente em português para eliminar ambiguidades, construções artificiais, problemas de concordância e inconsistências de terminologia.
5. Conferir exemplos de código, referências, imagens, URLs e âncoras. Toda diferença funcional em código deve ser investigada; uma atualização técnica necessária deve ser registrada como tarefa separada.
6. Atualizar os títulos do índice e adicionar a seção ao índice de português quando o arquivo estiver disponível. Ao final, preservar a ordem e a cobertura do índice inglês.
7. Compilar e inspecionar a página renderizada. Nos quizzes, testar escolhas corretas e incorretas e conferir as explicações exibidas.
8. Registrar resultado e pendências. Uma seção só recebe o estado “verificada” quando todas as etapas aplicáveis forem concluídas.

## Verificação em camadas

### Cobertura e fidelidade

- Comparar a lista e a ordem das 50 entradas dos índices inglês e português e conferir a existência de cada arquivo.
- Conferir conteúdo bloco a bloco; equivalência de contagem de arquivos ou títulos não demonstra tradução integral.
- Buscar trechos em inglês que possam ter sido esquecidos, inclusive dentro de componentes. Revisar cada ocorrência para distinguir nomes próprios, código e dados preservados de texto pendente.
- Conferir que todos os exercícios, avisos, recursos adicionais e feedbacks de quizzes foram traduzidos.

### Qualidade linguística e técnica

- Aplicar o glossário e resolver termos divergentes em todo o curso.
- Conferir distinções como áudio/fala, treino/inferência, amostragem/reamostragem, codificador/decodificador e avaliação subjetiva/objetiva.
- Conferir fórmulas, métricas, unidades e números contra o original.
- Revisar coerência entre título, explicação, exemplo e exercício.
- Documentar dúvidas e defeitos do original sem corrigi-los silenciosamente durante a tradução.

### Código, MDX e navegação

- Comparar os blocos de código e as expressões dos componentes com a referência; diferenças restritas a comentários e textos de apresentação precisam de revisão explícita.
- Conferir sintaxe MDX, propriedades dos componentes, flags dos quizzes e metadados do índice.
- Compilar todo `pt-BR` e conferir as 50 rotas por requisições locais, com conteúdo esperado, sem erros de renderização.
- Inspecionar visualmente tabelas, avisos, imagens, blocos de código e quizzes de cada página; registrar quando uma inspeção visual não tiver sido possível.
- Verificar destinos locais e âncoras. Para links externos, registrar respostas e limitações de rede, autenticação ou indisponibilidade; uma falha de acesso não implica automaticamente um link inválido.
- Gerar notebooks de português, validar o formato com `nbformat` e conferir correspondência dos exemplos com as seções. Geração de notebooks não prova execução das células.
- Executar exemplos leves quando necessário para investigar uma alteração suspeita. Treinamento completo, downloads extensos e execução de todas as aplicações de ML não são critérios obrigatórios de qualidade da tradução; verificações não realizadas devem aparecer no relatório.

## Comandos e limitações conhecidos

Executar na raiz `/workspace/audio-transformers-course`, após ativar o ambiente:

```bash
source /workspace/.venvs/audio-transformers-course/bin/activate
make quality
python utils/validate_translation.py --language pt-BR
doc-builder build audio-transformers-course chapters/pt-BR \
  --language pt-BR --not_python_module \
  --build_dir /workspace/.onboarding/audio-transformers-course/docs
```

`validate_translation.py` pode sair com código zero mesmo relatando seções ausentes. Ler sua saída e conferir índices explicitamente. `make quality` verifica formatação dos exemplos em todos os idiomas; não é uma avaliação linguística. Não executar `make style` globalmente para evitar mudanças em outros idiomas.

Para a prévia, usar as instruções de inicialização salvas no ambiente e `doc-builder preview` com `chapters/pt-BR`. Verificar a porta efetiva no log. Requisições locais e inspeção do HTML complementam, mas não substituem, a inspeção visual.

O gerador global de notebooks falha ao encontrar `chapters/unpublished` sem `_toctree.yml`. Usar a função existente `create_notebooks('pt-BR', destino)` e validar os arquivos gerados, sem alterar o material não publicado.

## Registro e entregáveis

Durante a execução, manter um registro por seção com caminho, versão da referência, estado, verificações realizadas e pendências. Estados: pendente, em tradução, traduzida, em revisão, verificada ou bloqueada. Registrar separadamente defeitos do original e limitações de verificação.

Entregáveis finais:

- Os 50 arquivos correspondentes em `chapters/pt-BR` e o índice integralmente localizado.
- Glossário de tradução com decisões terminológicas.
- Registro de verificação de todas as seções.
- Relatório final com cobertura, verificações aprovadas, falhas, limitações e questões do original.
- Mudanças limitadas ao português e aos documentos de acompanhamento; alterações fora desse escopo precisam de justificativa específica.

## Critério de conclusão

A tradução estará concluída quando as 50 seções estiverem presentes, integralmente traduzidas e revisadas, com índice completo, terminologia consistente e nenhuma pendência de tradução ou erro de renderização conhecido. O fechamento exige resultados registrados das verificações de cobertura, fidelidade, formatação, compilação, navegação, quizzes e notebooks.

Se uma capacidade do ambiente impedir uma verificação obrigatória, registrar a limitação e não declarar essa etapa concluída. O relatório distinguirá tradução finalizada, verificações efetivamente executadas e verificações pendentes. A aprovação automática das ferramentas nunca será apresentada como garantia absoluta de qualidade linguística.
