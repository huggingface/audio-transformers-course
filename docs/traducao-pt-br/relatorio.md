# Retomada da tradução: unidades 0–3

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

Há 29 seções ainda não traduzidas, das unidades 4–8 e eventos. As 21 disponíveis não receberam o estado final “verificada”: continuam com revisão de links externos, mídias e/ou inspeção visual integral pendentes. O fechamento transversal do curso permanece pendente.

A criação de PR está bloqueada: `gh api repos/prof-ramos/audio-transformers-course` retornou `Forbidden`, e uma requisição HTTPS confirmou 403 no túnel do proxy para `api.github.com`. Não foram criados tokens, credenciais ou permissões persistentes, nem alterada a política de rede. O acesso de leitura Git por `origin` funcionou.

O próximo lote de tradução é a unidade 4. O registro distingue tradução/revisão textual concluída de validação final pendente, para evitar duplicar trabalho ou apresentar a meta como completa.
