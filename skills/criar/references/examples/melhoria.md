# Exemplo de melhoria

Use como referência de tom e decomposição, não como fonte de regras para outras demandas.

```markdown
[Melhoria] - Importação Parcial de Documento de Saída na Entrada Manual

----

Prezados,

Segue especificação de melhoria para importação parcial de Documento de Saída na tela de Documento de Entrada Manual.

----

DESCRIÇÃO / MOTIVO:

O cliente possui um fluxo no qual parte das mercadorias expedidas pode retornar ao estoque após a entrega. Atualmente, o operador precisa digitar manualmente um novo Documento de Entrada, mesmo quando todos os dados já existem no Documento de Saída original.

Esse processo aumenta o tempo operacional e o risco de divergências na identificação e na quantidade dos produtos retornados. O retorno também pode ser parcial, tanto em itens quanto em quantidades.

A melhoria deverá permitir que o operador localize um Documento de Saída da filial, selecione somente os itens efetivamente devolvidos e importe esses dados para o fluxo padrão de Documento de Entrada Manual.

----

SOLICITAÇÃO DE DESENVOLVIMENTO:

Importação de Documento de Saída

Tela: Documento de Entrada Manual (`/movement/inbound/orders/add`).

O usuário deverá conseguir acionar a opção “Importar Documento de Saída” e localizar um único documento pertencente à filial padrão do usuário.

Regras de Negócio:

- A busca deverá permitir filtrar por documento, cliente, CNPJ, status e data de separação.
- Após a escolha do documento, o sistema deverá apresentar seus produtos e quantidades originais.
- O usuário poderá selecionar parte dos itens e informar quantidade menor ou igual à expedida.
- Itens com quantidade zero não deverão compor a entrada.

Resultado Esperado do Desenvolvimento:

Após a confirmação, o sistema deverá preencher o fluxo padrão de Documento de Entrada Manual somente com os produtos e quantidades escolhidos, preservando a referência ao documento de origem.

----

RESULTADO ESPERADO:

- Permitir a criação ágil de entrada baseada em uma saída anterior.
- Aceitar retorno total ou parcial conforme seleção do operador.
- Reduzir digitação manual e preservar a rastreabilidade do processo.

----

SUGESTÃO DE CENÁRIOS DE TESTES:

Sessão 1: Importação de produtos

Cenário 1: Importação total

Plataforma: Acesso via Web.

Usuário: Operador com acesso à tela de Documento de Entrada Manual.

Pré-condição: Documento de Saída com dois produtos disponível na filial do usuário.

Passos: Acessar a tela, importar o documento, selecionar todos os itens com as quantidades originais e confirmar.

Resultado Esperado: A entrada deverá ser preenchida com os dois produtos e as quantidades originais.

Cenário 2: Importação parcial

Plataforma: Acesso via Web.

Usuário: Operador com acesso à tela de Documento de Entrada Manual.

Pré-condição: Documento de Saída da filial do usuário com um produto e quantidade 5.

Passos: Importar um documento com quantidade 5, selecionar o produto, informar quantidade 2 e confirmar.

Resultado Esperado: A entrada deverá conter o produto com quantidade 2, mantendo a referência à saída original.

----

Att,

Ramon Mendes.
```
