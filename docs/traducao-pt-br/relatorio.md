# Tradução integral para pt-BR: unidades 0–8 e eventos

## Diagnóstico e escopo

Em 10 de outubro de 2026, o runtime confirmou `observed_phase: running`, `observations_current: true`, `failure: null` e conectividade `connected`. O checkout e o ambiente Python estavam acessíveis. A rede é restrita: conectividade do runtime não implica acesso externo. Não foi necessário reprovisionar o ambiente e não foi encontrada tradução concorrente.

As 50 seções do índice inglês estão traduzidas e passaram por revisão comparativa e leitura linguística em etapas separadas, pelo mesmo agente. A referência é `56b6e8334aef7e0efa0137574f068c968f3f6e1c`. Foram revisadas as 10 seções existentes e traduzidas as outras 40, incluindo índice, prosa, títulos, avisos, tabelas, textos alternativos, exercícios e quizzes. Essa revisão não equivale à avaliação independente de outro tradutor.

`GOAL_TRADUCAO_PT_BR.md` foi preservado. Contém o texto do objetivo, mas não comprova ativação do agendador. A autorização posterior permite commits, push e PR na branch existente, sem merge ou deploy. Inglês e demais idiomas permaneceram intactos.

## Verificações

| Verificação | Resultado |
| --- | --- |
| Cobertura e ordem do índice | 50/50 seções, mesmos caminhos e ordem do inglês |
| `make quality` | Aprovado |
| Compilação pt-BR com doc-builder | Aprovada |
| `verificar.py --complete` | Aprovado: blocos de código e saídas, URLs em ordem, contagem de títulos, estrutura/flags dos quizzes e índice |
| `validate_translation.py --language pt-BR` | Saída lida: `No missing sections - translation complete!` |
| Navegador | 50 rotas HTTP 200, títulos presentes, nenhum erro JavaScript de página |
| Referências internas | 242 destinos distintos; nenhuma âncora ausente; dois caminhos defeituosos herdados do original |
| Quizzes | 41 alternativas de 14 perguntas testadas, com feedback correto e incorreto correspondente |
| Notebooks | 21 gerados em diretório novo; esquema `nbformat`, código e saídas gravadas conferidos |
| Inspeção visual | Layout e texto renderizado das 50 páginas examinados; complemento com 117 recortes legíveis de 33 páginas, em 30 painéis |
| Fórmulas | Quatro fórmulas de avaliação examinadas em tamanho legível após corrigir o CSS da prévia local |
| Mídias e links externos | Pendentes: acesso bloqueado; 38 imagens observadas sem carregar |

Números e significado da prosa foram conferidos na revisão comparativa. O verificador automatizado não prova qualidade linguística ou equivalência semântica da prosa. Valores e fórmulas foram preservados, com convenções decimais do português no texto; entradas e saídas dos modelos permanecem no idioma original. Não foram executadas células de treinamento, autenticação ou publicação.

Evidências locais: `/workspace/.onboarding/audio-transformers-course/validation/`, incluindo `invariants.json`, `translation-validator.log`, `build.log`, `browser/routes.json`, `browser/internal-links.json`, `browser/quizzes.json`, screenshots e `notebooks-completo/verification.json`. O resumo revisável está em `evidencias.json`. Esses arquivos locais não são links públicos. A contagem definitiva de notebooks é 21; a geração foi repetida em `notebooks-avisos/`, com esquema válido e código/saídas idênticos ao lote completo verificado. Diretórios antigos de lotes anteriores não entram nessa contagem.

## Renderização e configuração do ambiente

Os tokens `<UNK>`, `<pad>` e `<unk>` foram escapados fora de código para aparecerem como texto; a ênfase do quiz da unidade 1 foi adaptada ao HTML aceito pelo componente. Os títulos de incorporações Gradio foram localizados. Na retomada, código inline em dez avisos de seis páginas e uma lista indentada foram adaptados ao HTML aceito pelo renderer; seis rotas foram conferidas novamente no navegador, sem erros de página. Os literais e exemplos foram preservados, escapando chaves no exemplo JSON. A tabela de WER teve uma célula vazia excedente removida para alinhar os mesmos seis tokens. Lógica dos quizzes, identificadores e blocos de código foram preservados. `git diff --check` aponta quatro espaços finais nos delimitadores de código da unidade 6 (linhas 406, 422, 498 e 505); são idênticos aos delimitadores ingleses e foram mantidos para preservar os blocos integralmente. `make quality` aprova esses exemplos. As âncoras que dependem de títulos traduzidos foram conferidas no DOM.

A prévia duplicava fórmulas porque o kit instalado não importava o CSS do KaTeX. Foi acrescentada a importação de `katex/dist/katex.min.css` no kit local, fora do checkout, usando o pacote já instalado. A correção idempotente foi incorporada ao script de instalação. A prévia foi reiniciada a partir desse kit para conferir sua persistência. Isso não altera nem valida o renderer publicado do curso.

Os campos `install_script` e `start_skill` foram salvos pelo serviço de onboarding em um rascunho de configuração (`requires_publish: true`). Ainda precisa ser revisado e publicado nas configurações do ambiente. O runtime atual foi testado; a restauração de um ambiente novo a partir de snapshot não foi verificada. Não foram criados tokens, credenciais ou acessos persistentes, nem alterada a política de rede.

Controles como `Submit`, `Correct!` e `Copy page` pertencem ao kit externo; o texto genérico de instalação dos notebooks pertence ao gerador. Permanecem em inglês. Algumas saídas longas de código ampliam a largura da prévia, com conteúdo preservado. Imagens, áudios, vídeos e demonstrações externas exigem inspeção funcional com acesso aos destinos. Requisições a `huggingface.co`, `www.youtube.com` e `course-demos-song-classifier.hf.space` retornaram 403 no túnel do proxy; isso não comprova defeito na mídia original.

## Questões do original preservadas

- Cronograma de 2023, números de modelos, linguagem futura e APIs históricas exigem avaliação em eventual atualização técnica.
- A unidade 3 afirma ausência de modelos com saída direta de forma de onda na biblioteca, embora a unidade 6 apresente Bark e MMS. CTC usa 26 letras inglesas e forma `(768, 50)`; a convenção dos eixos merece revisão.
- A definição de `AutoProcessor` menciona extrator e processador, embora o par anterior seja extrator e tokenizador.
- Filtros `< 20`, `< 30` e `< 200` excluem também o limite exato, enquanto algumas descrições destacam apenas valores maiores.
- A unidade 4 atribui 15 classes a Speech Commands; a unidade 7 apresenta checkpoint com 35. O nome “Environmental Speech Challenge” para ESC e a relação entre maior variância e menor faixa dinâmica exigem revisão.
- FLEURS aparece com 102 idiomas na unidade 4 e 101 na tabela da unidade 5; a descrição de gravações espontâneas do Parlamento Europeu nessa tabela parece incorreta. MLS aparece com seis idiomas na unidade 5 e oito na unidade 6.
- Em `chapter5/asr_models`, `hf-internal-testing/librispeech_asr_dummy` e `facebook/wav2vec2-base-100h` são links relativos sem URL do Hub e viram caminhos locais inexistentes. Foram preservados conforme a restrição de URLs; essa navegação permanece pendente.
- A melhora de WER de cerca de 126% para 14,1% é chamada de 112%, confundindo pontos percentuais e melhora relativa. O texto alterna 167% e 168%, anuncia três métricas apesar de incluir RTFx e chama de `Small` o modelo anteriormente avaliado como `base`.
- A dificuldade de segmentação de mandarim e japonês é apresentada como inexistência de palavras.
- A unidade 6 anuncia duas arquiteturas, mas inclui uma terceira; o trecho de MSE usa “gerado” onde seria necessário esclarecer o alvo. O link de “treinamento” de x-vectors apresenta cálculo de embeddings; identificação de falantes aparece sob descrição de fala para texto.
- A unidade 7 anuncia três modelos, mas apresenta cadeia de quatro etapas. O “truque” de Whisper para tradução não foi validado como tradução geral. Transformers Agents e afirmações sobre pipelines dependem da versão histórica das APIs.

Essas observações são pendências técnicas da referência, sem alterações silenciosas no inglês.

## Entrega e pendências

PR existente em rascunho: https://github.com/prof-ramos/audio-transformers-course/pull/1, base `main`, branch `codex/traducao-pt-br-unidades-0-3`. Foi anexado à tarefa, sem duplicação. Os lotes anteriores foram enviados nos commits `015c39e`, `d712da3` e `c432e52`; o lote final inclui unidades 6–8, eventos e este registro integral.

A descrição final está em `descricao-pr.md` e em `/workspace/.onboarding/audio-transformers-course/PR_DESCRIPTION.md`. O conector que criou o PR no thread de origem não está disponível nesta execução, e `api.github.com` é bloqueado pelo proxy. Preparar esse texto não equivale a atualizar a descrição remota. O push usa a autenticação Git já existente. Não houve merge ou deploy.

Nenhuma seção está pendente de tradução ou revisão textual. A verificação final permanece pendente: mídias e links externos e dois links originais defeituosos. A inspeção detalhada do texto renderizado foi concluída nesta retomada. O objetivo está bloqueado pelas verificações externas: uma nova retomada precisa de acesso aos destinos e do conector para atualizar a descrição remota do PR. Não há tradução nem revisão textual pendente para repetir.
