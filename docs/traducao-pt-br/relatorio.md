# Retomada da tradução: unidades 0–5

## Diagnóstico do ambiente e da execução

Em 10 de outubro de 2026, o runtime informou `observed_phase: running`, `observations_current: true`, `failure: null` e conectividade `connected`. O checkout e o ambiente Python estavam acessíveis. A política de rede retornou estado `unknown`; as respostas dos destinos foram verificadas diretamente, sem presumir acesso.

O histórico anterior continha três turnos concluídos de preparação, planejamento e criação do texto da meta. A leitura do thread mostrou este turno de retomada como a única execução atual. Não foi encontrada outra execução de tradução. O arquivo `GOAL_TRADUCAO_PT_BR.md` foi preservado. Não há ferramenta de leitura ou ativação do agendador de metas disponível nesta sessão; não foi afirmada ativação automática nem conclusão da meta. Não foi necessário reprovisionar o ambiente para executar a tradução.

## Alterações

- Glossário e registro de progresso para as 50 seções, com SHA da referência inglesa.
- Revisão comparativa e linguística das 10 seções existentes, nas unidades 0 e 1.
- Tradução das 11 seções das unidades 2 e 3 e inclusão no índice.
- Atualização dos exemplos desatualizados de português para os blocos exatos do inglês atual, incluindo Gradio e a reamostragem em `prepare_dataset`.
- Correção da apresentação do token `<UNK>` no quiz da unidade 3 e da ênfase no quiz da unidade 1, preservando ordem, chaves e respostas corretas.
- Verificador reproduzível em `docs/traducao-pt-br/verificar.py`. O modo normal verifica o lote disponível; `--complete` exige cobertura integral.

## Evidências e limites

| Verificação | Resultado |
| --- | --- |
| `make quality` | Aprovado |
| Compilação de todo `pt-BR` com doc-builder | Aprovada para o conteúdo disponível |
| Código e saídas dos exemplos iguais ao inglês | Aprovado nas 21 seções |
| URLs preservadas, contagem de títulos e lógica dos quizzes | Aprovado nas 21 seções |
| Ordem do índice e existência dos arquivos | Aprovado para 21 de 50 seções |
| Requisições no navegador | 21 rotas com HTTP 200, títulos presentes e zero erros JavaScript de página |
| Interação nos quizzes | 41 alternativas testadas, incluindo corretas e incorretas, com feedback correspondente |
| Notebooks | 8 gerados e validados com `nbformat`; células de ML não executadas |
| Inspeção visual | Realizada nas páginas indicadas em `progresso.json`; não equivale à inspeção completa de todas as mídias |

Resultados de browser, screenshots, saída do verificador e notebooks estão em `/workspace/.onboarding/audio-transformers-course/validation/`. Não são links públicos nem comprovação de funcionamento dos serviços externos.

As screenshots mostram texto, tabelas e questionários locais, mas imagens hospedadas no Hugging Face e incorporações de vídeo/demonstração não carregaram. A requisição HTTPS de uma imagem em `huggingface.co` retornou 403 no túnel do proxy. Nenhuma validação de áudio ou imagem externa foi considerada aprovada. Algumas linhas longas de saída de código estendem a largura da prévia; os blocos foram preservados e o comportamento deve ser revisado no renderer do curso.

Rótulos genéricos como `Submit`, `Correct!` e `Copy page` pertencem ao kit externo do doc-builder e permanecem em inglês. Perguntas, alternativas e explicações do conteúdo foram localizadas. Não foi alterado o código do renderer externo.

## Questões observadas no original

- A introdução mantém um cronograma de publicação de 2023 e linguagem futura. A tradução preserva esse contexto histórico.
- A unidade 3 apresenta afirmações dependentes da época, como a ausência de modelos com saída direta de forma de onda na biblioteca. Não foram modernizadas silenciosamente.
- A descrição de CTC usa o alfabeto inglês de 26 letras como exemplo e apresenta `(768, 50)` para a sequência de saída. Esses valores foram preservados; a convenção dos eixos deve ser conferida em uma eventual revisão técnica do original.
- A explicação de filtragem menciona amostras mais longas que 20 s; o código usa `< 20.0` e também exclui exatamente 20 s. O código foi preservado.
- A definição de `AutoProcessor` no original menciona carregar “extrator de características e processador”, embora o par apresentado antes seja extrator e tokenizador. Não foi feita correção silenciosa dessa expressão.
- Strings dos quizzes usam HTML direto. O `<UNK>` sem escape desaparecia na apresentação; no português, foi escapado para exibir o identificador corretamente. A referência inglesa permaneceu intacta.

## Pendências da meta

Há 16 seções ainda não traduzidas, das unidades 6–8 e eventos. As 34 disponíveis não receberam o estado final “verificada”: continuam com revisão de links externos, mídias e/ou inspeção visual integral pendentes. O fechamento transversal do curso permanece pendente.

Diagnóstico anterior da criação de PR, posteriormente resolvida pelo conector GitHub: `gh api repos/prof-ramos/audio-transformers-course` retornou `Forbidden`, e uma requisição HTTPS confirmou 403 no túnel do proxy para `api.github.com`. Não foram criados tokens, credenciais ou permissões persistentes, nem alterada a política de rede. O acesso de leitura Git por `origin` funcionou.

O próximo lote de tradução é a unidade 6. O registro distingue tradução/revisão textual concluída de validação final pendente, para evitar duplicar trabalho ou apresentar a meta como completa.

## Entrega do lote

O commit de tradução `015c39e9a2dae7776c04aa58a02914ee076ccb01` foi enviado à branch `codex/traducao-pt-br-unidades-0-3`. O SHA remoto foi confirmado com `git ls-remote`. Não foi criado PR; a descrição está preparada em `/workspace/.onboarding/audio-transformers-course/PR_DESCRIPTION.md`. Não houve merge ou deploy.

Após reiniciar a prévia para atualizar o índice, os seis links da unidade 3 apareceram no menu. A âncora em português de reamostragem também foi confirmada no DOM.

O checkout tinha um refspec de fetch limitado a main. Foi acrescentado somente o mapeamento da nova branch e buscada sua referência para permitir o acompanhamento do upstream, preservando o mapeamento anterior e a autenticação existente.

## Lote das unidades 4–5

Foram traduzidas e revisadas, em uma segunda leitura comparativa e linguística pelo mesmo agente, as cinco seções de classificação de áudio/música e as oito seções de reconhecimento de fala. O índice agora cobre 34 das 50 seções. Nomes de modelos, parâmetros, amostras de fala em inglês e espanhol, valores das tabelas e saídas de código foram preservados. Os títulos de aplicações Gradio incorporadas foram localizados.

A compilação de todo o conteúdo disponível e `make quality` passaram. O verificador de invariantes passou nas 34 seções. O navegador respondeu HTTP 200 nas 34 rotas, com títulos presentes e nenhum erro JavaScript de página. A prévia foi reiniciada para carregar o índice ampliado. Os screenshots das 13 páginas novas foram inspecionados quanto ao layout geral; a inspeção detalhada das páginas longas permanece registrada como parcial. Imagens e incorporações externas continuam sem validação de funcionamento.

Foram gerados 16 notebooks em um diretório novo, `validation/notebooks-lote-0-5`, validados com `nbformat` e comparados com os exemplos dos capítulos quanto às células de código e saídas gravadas. Uma contagem inicial de 24 no diretório anterior incluía oito arquivos antigos em um subdiretório; ela não representa este lote. O texto genérico de instalação em inglês é inserido pelo gerador de notebooks do repositório. Nenhuma célula de ML, autenticação ou publicação foi executada.

A prévia revelou que o token `<pad>` em um aviso de CTC era tratado como uma tag HTML. Ele foi escapado na tradução, como já havia sido feito para `<UNK>` no questionário, sem alterar código nem o inglês. A confirmação do texto no DOM e a apresentação das fórmulas de avaliação integram as verificações em andamento.

Questões adicionais do original, preservadas e sem atualização técnica silenciosa:

- A unidade 4 descreve Speech Commands como tendo 15 classes de palavras-chave; isso deve ser confrontado com a versão e a configuração do conjunto/checkpoint.
- O nome “Environmental Speech Challenge” para ESC e a relação entre maior variância e menor faixa dinâmica parecem incorretos.
- FLEURS aparece com 102 idiomas na unidade 4 e 101 na tabela da unidade 5. A tabela também o descreve como gravações espontâneas do Parlamento Europeu, descrição que exige revisão do original.
- Dois links para namespaces do Hub em `chapter5/asr_models` são relativos e não apontam para arquivos locais: `hf-internal-testing/librispeech_asr_dummy` e `facebook/wav2vec2-base-100h`. Foram preservados como no original; a navegação correspondente permanece pendente.
- A alegação de melhora de 112% com WER reduzida de aproximadamente 126% para 14,1% confunde diferença em pontos percentuais e melhora relativa. Os valores não foram recalculados na tradução.
- A explicação de avaliação afirma que mandarim e japonês não têm noção de palavras; a dificuldade de segmentação não equivale à inexistência de palavras.
- O texto ainda anuncia três métricas apesar da seção adicional de RTFx; também alterna 167% e 168% para a WER ortográfica. A tabela WER tinha uma célula vazia excedente; a tradução mantém os seis tokens do exemplo alinhados à referência.
- A filtragem da unidade 5 usa `< 30`, excluindo também exatamente 30 s, embora a descrição destaque amostras maiores que 30 s.
- O modelo avaliado no exemplo anterior é `base`, mas a discussão final o chama de `Small`.

O usuário informou a criação do PR em rascunho pelo conector GitHub autorizado: https://github.com/prof-ramos/audio-transformers-course/pull/1. Esse PR foi anexado à tarefa, sem criar outro. A API GitHub continua indisponível pelas ferramentas deste ambiente; o conector que realizou a criação não aparece entre as ferramentas desta execução. A descrição atualizada do lote fica preparada em `/workspace/.onboarding/audio-transformers-course/PR_DESCRIPTION.md` para atualização pelo conector disponível no thread de origem. Não houve alteração de credenciais ou política de rede.
