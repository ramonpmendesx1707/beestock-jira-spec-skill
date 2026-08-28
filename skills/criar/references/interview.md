# Sabatina por árvore de decisões

## Princípio

Modele a demanda como uma árvore. Uma pergunta entra na rodada somente quando suas decisões predecessoras já estiverem resolvidas. A `fronteira` é o conjunto de todas as perguntas respondíveis agora sem depender de outra resposta ainda aberta.

Pergunte a fronteira inteira em uma rodada, normalmente entre 3 e 7 perguntas. Não faça uma pergunta por mensagem quando várias já estiverem desbloqueadas. Recalcule a árvore depois das respostas.

## Responsabilidade por fatos e decisões

- Fatos presentes em arquivos, telas e fontes acessíveis são responsabilidade do agente.
- Decisões de processo, escopo e política são responsabilidade do Product Owner.
- Boas práticas podem virar recomendações, nunca fatos do BeeStock.

Antes de perguntar, tente responder pelas evidências. Não peça “qual é a URL?” quando ela estiver visível no print; não pergunte “qual erro ocorreu?” quando o vídeo mostrar a mensagem.

## Ordem da árvore

Use os ramos aplicáveis, não como formulário fixo:

1. **Identidade:** melhoria ou bug; objetivo; problema; solicitante; cliente; impacto e frequência.
2. **Estado atual:** gatilho, pré-condições, ator, plataforma, passos, dados de entrada e resposta atual.
3. **Estado desejado:** mudança observável, benefício, ponto de término e diferença em relação ao atual.
4. **Escopo:** telas/processos incluídos, fora do escopo, compatibilidade e regressões relevantes.
5. **Regras:** condições, estados, permissões, prioridades, cálculos, limites, quantidades, seleção, mensagens e configurações.
6. **Ramos:** fluxo principal, alternativas, erros, cancelamento, repetição/reprocessamento, duplicidade, dados ausentes, limites e exceções operacionais.
7. **Rastreabilidade:** documentos relacionados, integrações vistas pelo negócio, origem/destino dos dados e histórico necessário.
8. **Testabilidade:** pré-condições, massa de teste, resultado verificável e evidência de sucesso ou erro.

## Formato da rodada

```markdown
❓ **Q1 — Título curto:** pergunta contextualizada e, quando útil, opções mutuamente exclusivas.

➡️ **Recomendação:** alternativa recomendada e por que ela reduz risco de processo.

---

❓ **Q2 — Título curto:** próxima decisão disponível na fronteira.

➡️ **Recomendação:** resposta recomendada.
```

Use numeração contínua entre rodadas. Permita respostas curtas por número. Se o usuário responder parcialmente, confirme o que fechou e pergunte apenas o restante desbloqueado.

## Priorização

Pergunte primeiro o que pode mudar o desenho inteiro ou causar estoque, documento ou rastreabilidade incorretos. Depois trate exceções e permissões. Preferências de texto e detalhes cosméticos ficam por último e podem ser resolvidos pelo padrão existente.

Uma pergunta é bloqueante quando respostas diferentes produziriam requisitos, resultados esperados ou testes diferentes. Não bloqueie a issue por curiosidade, detalhe de implementação ou informação sem efeito observável.

Se mais de 7 perguntas parecerem disponíveis, mantenha na rodada somente as de maior impacto e deixe as demais para uma fronteira posterior. Não pergunte algo apenas para preencher uma seção do modelo. Quando recomendar uma decisão com alternativas plausíveis, mostre resumidamente as consequências de cada alternativa antes de indicar a preferida.

## Confirmação do entendimento

Quando a fronteira ficar vazia, apresente um resumo compacto contendo problema, processo atual, solução esperada, principais regras, exceções e itens fora do escopo. Peça confirmação de entendimento compartilhado antes do rascunho. Uma correção reabre apenas os ramos dependentes.

## Interrupção para Jira resumido

Se o usuário solicitar um Jira simples, resumido ou inicial durante qualquer rodada:

1. Pare de expandir a árvore.
2. Preserve as respostas já recebidas.
3. Converta no máximo 3 perguntas abertas em pontos de validação futura, somente quando a omissão puder levar o leitor a interpretar o escopo inicial de forma incorreta.
4. Não faça uma rodada de confirmação adicional.
5. Siga diretamente para o rascunho no modo `RESUMIDO`.

Não tente convencer o usuário a continuar a sabatina. A escolha de profundidade é uma decisão do Product Owner.
