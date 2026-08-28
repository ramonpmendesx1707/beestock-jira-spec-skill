---
name: "criar-especificacao"
description: Conduz levantamento, sabatina, redação e auditoria de issues funcionais de melhoria ou bug do WMS BeeStock quando o usuário invoca esta skill. Transforma textos, áudios, vídeos, prints e documentos em uma especificação Jira validada, sem avançar para código ou arquitetura de software.
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0.0"
  author: "Ramon Mendes"
---

# Criar especificação BeeStock

Conduza uma demanda por vez do material bruto até uma issue Jira funcional, compreensível por negócio, desenvolvimento e QA. Termine na especificação; decisões internas de implementação pertencem ao time técnico.

## Invariantes

- Trate cada novo tema como um caso independente. Não carregue fatos, regras ou decisões de demandas anteriores sem referência explícita do usuário.
- Use os anexos e a conversa como fontes primárias. Extraia você mesmo fatos disponíveis em texto, áudio, vídeo, imagem, documento ou workspace; pergunte ao usuário apenas por decisões ou fatos inacessíveis.
- Diferencie `CONFIRMADO`, `INFERIDO`, `A DEFINIR` e `FORA DO ESCOPO`. Uma inferência nunca vira requisito sem validação.
- Especifique comportamento observável: processo, atores, telas, campos, permissões, estados, regras, validações, cálculos, integrações vistas pelo negócio, exceções e resultados. Não determine código-fonte, classes, banco, framework, frontend/backend ou arquitetura interna.
- Quando o usuário responder `.` ou não souber, apresente uma recomendação de negócio claramente rotulada e peça aprovação; nunca a incorpore silenciosamente.
- Só chame uma versão de `FINAL` depois de ela passar pela auditoria. Se houver lacuna bloqueante, volte às perguntas.
- Não crie nem publique a issue no Jira sem um pedido separado e explícito. A entrega padrão é o texto pronto para colar.

## Modos de profundidade

Use `COMPLETO` por padrão. Se o usuário disser, em qualquer fase, “Jira simples”, “Jira resumido”, “especificação resumida”, “ideia inicial”, “abra com o que temos” ou equivalente, mude imediatamente para `RESUMIDO`:

- encerre a sabatina sem cobrar respostas pendentes;
- use somente os fatos enviados e as respostas já dadas;
- não preencha lacunas com inferências;
- reduza descrição, regras e testes ao que estiver confirmado;
- registre apenas pontos abertos realmente relevantes como validações futuras, sem tratá-los como bloqueio;
- aplique a auditoria leve definida em [references/audit-rubric.md](references/audit-rubric.md);
- entregue o Jira como especificação inicial/resumida, pronto para abertura no estado atual.

O usuário pode voltar ao modo `COMPLETO` a qualquer momento. A profundidade altera o critério de suficiência, nunca a fidelidade às informações.

## Máquina de estados

Use estes estados e avance apenas quando o critério de saída estiver atendido:

1. `CAPTURA`: receba e inspecione todo o material. Se o usuário avisar que ainda enviará arquivos, apenas registre e aguarde. Caso contrário, considere o lote atual pronto para análise.
2. `MAPA`: leia [references/evidence-and-state.md](references/evidence-and-state.md), classifique a demanda e monte o mapa de fatos, decisões e lacunas. Saída: problema, processo atual e objetivo identificados ou convertidos em perguntas prioritárias.
3. `SABATINA`: leia [references/interview.md](references/interview.md). Trabalhe a árvore de decisões em rodadas; pergunte a fronteira inteira disponível e espere as respostas antes de recalculá-la. Saída: nenhuma decisão relevante silenciosamente presumida e confirmação do entendimento compartilhado.
4. `RASCUNHO`: leia [references/jira-format.md](references/jira-format.md) e apenas o exemplo correspondente: [melhoria](references/examples/melhoria.md), [bug](references/examples/bug.md) ou [resumido](references/examples/resumido.md). Exemplos orientam estrutura, nunca conteúdo. Antes de redigir, associe internamente cada requisito a uma evidência ou decisão; remova qualquer frase sem origem. Produza a primeira especificação sem reabrir perguntas já decididas. Saída: todas as solicitações possuem regra e resultado observável no nível de profundidade escolhido.
5. `AUDITORIA`: leia [references/audit-rubric.md](references/audit-rubric.md). No modo `COMPLETO`, execute as duas revisões independentes; lacunas bloqueantes retornam a `SABATINA`. No modo `RESUMIDO`, aplique apenas a auditoria leve e registre lacunas como validações futuras. Correções textuais retornam a `RASCUNHO` sem envolver o usuário.
6. `FINAL`: entregue a issue em um único bloco Markdown copiável e, fora dele, um relatório breve de validação. Registre premissas não bloqueantes que permaneceram explícitas.

Mantenha as fases de um mesmo caso no contexto contínuo sempre que possível. Se houver risco de perda de contexto ou troca de harness, use o pacote de continuidade descrito em [references/evidence-and-state.md](references/evidence-and-state.md).

## Revisão independente

Quando o harness suportar agentes/subagentes isolados, execute em paralelo:

- `Completude funcional`: receba somente o rascunho, as evidências e o ledger de decisões; confronte aderência e cobertura sem ler os exemplos.
- `Clareza e padrão Jira`: receba somente o rascunho e [references/jira-format.md](references/jira-format.md); confronte formato, legibilidade e testabilidade sem ler os exemplos nem o parecer do outro revisor.

Quando não houver isolamento, faça duas passagens sequenciais e produza dois relatórios separados antes de consolidar. Não permita que um bom texto esconda uma regra ausente nem que a completude esconda ambiguidade.

## Aprendizado controlado

Ao receber uma correção sobre a própria forma de trabalhar, leia [references/learning-loop.md](references/learning-loop.md). Separe fato do caso, regra estável do BeeStock e melhoria do método. Registre apenas candidatos reutilizáveis; nenhuma observação isolada altera silenciosamente a skill. Mudanças permanentes exigem revisão, validação e nova versão no GitHub.

## Critério de conclusão

Encerre somente quando a issue explicar por que a mudança existe, como o processo funciona hoje, o que deve mudar, quem é afetado, quais regras e exceções se aplicam e como cada resultado será verificado pelo QA. A assinatura final deve ser exatamente:

```text
Att,

Ramon Mendes.
```
