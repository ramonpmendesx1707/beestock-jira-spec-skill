# Auditoria da especificação

Audite a versão completa, não apenas a última seção editada. Cada achado deve apontar a seção afetada, explicar o risco e distinguir bloqueio de melhoria editorial.

## Auditoria leve — modo RESUMIDO

No modo `RESUMIDO`, não aplique a barra de completude do modo completo. Verifique somente:

1. O texto não contradiz os dados enviados.
2. Nenhuma decisão ou regra foi inventada.
3. Está claro que se trata de escopo inicial/resumido quando houver lacunas materiais.
4. Problema, solicitação e resultado esperado são coerentes entre si.
5. Os poucos cenários sugeridos testam apenas o que foi efetivamente descrito.
6. Título, separadores e assinatura seguem o padrão.

Corrija problemas editoriais diretamente. Lacunas tornam-se `Pontos para Validação Futura`; não retorne à sabatina, exceto se o usuário revogar o modo resumido. O veredito deve ser `APROVADA COMO ESPECIFICAÇÃO INICIAL`.

## Eixo A — Completude funcional

Compare o rascunho com FONTES, ENTENDIMENTO e DECISÕES.

Este revisor não deve receber nem consultar os arquivos de exemplos. Para cada regra do rascunho, exija origem nas evidências ou no ledger; ausência de origem é `BLOQUEIO` de fidelidade.

Verifique:

1. **Problema e motivo:** causa, impacto e objetivo estão compreensíveis.
2. **Atual versus esperado:** a divergência ou mudança está explícita.
3. **Escopo:** incluído e excluído não se contradizem.
4. **Atores e acesso:** plataforma, perfil, filial e permissões aplicáveis estão definidos.
5. **Gatilhos e pré-condições:** está claro quando o fluxo começa e em quais estados pode ocorrer.
6. **Regras de negócio:** condições, prioridades, cálculos, quantidades, limites, configurações e mensagens relevantes estão completas.
7. **Ramos de processo:** alternativas, erros, cancelamento, repetição, duplicidade e exceções relevantes possuem comportamento definido.
8. **Dados e rastreabilidade:** origem, destino, vínculos, histórico e integrações funcionais estão compreensíveis.
9. **Cobertura:** toda solicitação possui resultado esperado e ao menos um cenário que a verifique.
10. **Fidelidade:** nenhuma regra foi inventada, perdida ou ampliada além das evidências e decisões.

Classifique cada item:

- `PASSA`: suficiente e coerente.
- `BLOQUEIO`: respostas diferentes mudariam comportamento ou teste; voltar à sabatina.
- `AJUSTE`: pode ser corrigido com o que já está decidido.
- `NÃO APLICÁVEL`: justifique brevemente.

## Eixo B — Clareza, padrão e testabilidade

Este revisor recebe apenas o rascunho e `jira-format.md`. Não consulte exemplos, fontes, ledger nem o relatório do Eixo A antes de concluir seu próprio parecer.

Verifique:

1. Título e introdução correspondem ao tipo da demanda.
2. Descrição/Motivo possui 3–6 parágrafos fluidos e explica o porquê.
3. Solicitações estão separadas por comportamento, sem misturar decisões internas de código.
4. Termos do domínio são consistentes e não usados como sinônimos ambíguos.
5. URLs e referências Jira estão normalizadas.
6. Cada regra usa linguagem precisa, sem “quando necessário”, “corretamente”, “adequado” ou “etc.” como substituto de decisão.
7. Resultados são observáveis e testáveis.
8. Cenários cobrem todas as regras sem testar funcionalidade não solicitada.
9. Não há redundância que esconda diferenças ou contradições.
10. Separadores, seções e assinatura seguem o modelo.

## Lógica de retorno

- No modo `RESUMIDO`: aplique exclusivamente a auditoria leve acima.
- Qualquer `BLOQUEIO`: não rotule como final. Faça nova rodada somente com as decisões bloqueantes e seus ramos recém-desbloqueados.
- Apenas `AJUSTE`: corrija o texto e repita os dois eixos.
- Todos `PASSA`/`NÃO APLICÁVEL`: marque `APROVADA`.

## Relatório ao usuário

Após a issue final, apresente fora do bloco copiável:

```markdown
**Validação final: APROVADA**

- Completude funcional: aprovada.
- Clareza e padrão Jira: aprovados.
- Premissas explícitas mantidas: nenhuma.  <!-- ou lista curta -->
- Itens fora do escopo registrados: ...
```

Não despeje uma checklist inteira aprovada. Mostre somente o veredito, premissas e observações que ajudem o Product Owner.

Para o modo `RESUMIDO`, use:

```markdown
**Validação final: APROVADA COMO ESPECIFICAÇÃO INICIAL**

- Coerência com as informações disponíveis: aprovada.
- Pontos deixados para validação futura: ...
```
