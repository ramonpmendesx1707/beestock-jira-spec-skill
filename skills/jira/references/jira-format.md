# Formato da issue Jira

Gere em português do Brasil, com Jira Markdown simples e separadores `----` entre as seções. Use linguagem funcional orientada ao negócio. Não exponha o ledger, rótulos de evidência ou raciocínio interno dentro da issue.

## Profundidade

No modo `COMPLETO`, siga todas as orientações aplicáveis deste documento.

No modo `RESUMIDO`:

- preserve título, introdução, Descrição/Motivo, Solicitação de Desenvolvimento, Resultado Esperado, Cenários de Testes e assinatura;
- reduza a Descrição/Motivo para 1–3 parágrafos;
- descreva apenas mudanças e regras confirmadas;
- sugira de 1 a 3 cenários básicos compatíveis com as informações disponíveis;
- quando necessário, acrescente ao final da Solicitação de Desenvolvimento o subtópico `Pontos para Validação Futura`, com no máximo 3 itens e a frase “Os pontos abaixo não integram o escopo confirmado desta versão inicial”;
- não use a falta de exceções, permissões ou valores ainda não discutidos para bloquear a entrega.

## Matriz interna de rastreabilidade

Antes de redigir, associe cada regra, resultado e cenário a pelo menos um ID de evidência ou decisão do caso. A matriz é interna e não aparece na issue. Frases retiradas apenas de exemplos, conhecimento geral ou recomendação não aprovada devem ser removidas. Depois da redação, confira o caminho inverso: toda decisão confirmada aplicável precisa aparecer na issue.

## Título

- Melhoria: `[Melhoria] - <descrição concisa>`
- Bug: `[BUG] - <descrição concisa>`

O título deve permitir que qualquer leitor entenda a ação ou falha principal em uma linha.

## Introdução

```text
Prezados,

Segue especificação de melhoria para <título adaptado ao cenário>.
```

ou:

```text
Prezados,

Segue detalhamento do bug onde <comportamento incorreto>.
```

## DESCRIÇÃO / MOTIVO

Escreva de 3 a 6 parágrafos fluidos, sem subtópicos internos. Use apenas elementos aplicáveis, nesta ordem:

1. Contexto, solicitante/cliente quando informado e impacto.
2. Processo ou comportamento atual.
3. Problema, divergência ou necessidade.
4. Visão resumida da solução e do novo fluxo.
5. Referências e pré-requisitos relevantes.

Apresente chaves Jira como links completos: `https://szsolucoes.atlassian.net/browse/BEES-3005`.

## SOLICITAÇÃO DE DESENVOLVIMENTO

Organize um subtópico para cada mudança funcional. Em cada um, inclua somente os atributos aplicáveis:

- Tela e caminho sem protocolo, host ou porta.
- Localização e ação do usuário.
- Campos: nome, tipo, formato e propósito.
- Opções e valores padrão.
- Permissões e perfis.
- Parâmetros e configurações funcionais.
- Regras de negócio.
- Condições, cálculos, limites e restrições.
- Origem/destino de dados e integração vista pelo negócio.
- Mensagens ou retorno esperado.

Finalize cada subtópico com `Resultado Esperado do Desenvolvimento`, descrevendo a resposta observável do sistema e, quando útil, o contraste entre antes e depois.

Escreva “O sistema deverá...” ou “O usuário deverá conseguir...”. Deixe a forma interna de implementação para o desenvolvimento. Não use frases como “ajustar o backend”, “alterar a query”, “criar classe” ou “salvar na tabela” salvo se o usuário tiver fornecido uma restrição técnica formal que precise ser preservada.

## RESULTADO ESPERADO

Liste, linha a linha, as mudanças e benefícios verificáveis. Não repita toda a solicitação; consolide o resultado do ponto de vista do usuário e do processo.

## SUGESTÃO DE CENÁRIOS DE TESTES

Agrupe por sessão funcional. Numere todos os cenários. Para cada cenário, informe:

- Objetivo do teste.
- Plataforma: `Acesso via Web`, `App Coletor`, `Integração API REST` ou outra confirmada.
- Perfil/usuário.
- Pré-condições e dados de teste factíveis.
- Passos.
- Resultado esperado observável.

Cubra o fluxo principal, alternativas, validações, erros e exceções que correspondam às regras especificadas. Inclua testes de regressão quando a mudança afetar comportamento existente. Não escreva a expressão “Caminho Feliz”.

## Assinatura

Após o último separador:

```text
Att,

Ramon Mendes.
```

## Esqueleto

```markdown
[Melhoria] - Título

----

Prezados,

Segue especificação de melhoria para ...

----

DESCRIÇÃO / MOTIVO:

...

----

SOLICITAÇÃO DE DESENVOLVIMENTO:

Subtópico funcional

...

Resultado Esperado do Desenvolvimento:

...

----

RESULTADO ESPERADO:

- ...

----

SUGESTÃO DE CENÁRIOS DE TESTES:

Sessão 1: ...

Cenário 1: ...

...

----

Att,

Ramon Mendes.
```
