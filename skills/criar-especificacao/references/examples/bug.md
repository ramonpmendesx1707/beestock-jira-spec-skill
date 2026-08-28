# Exemplo de bug

Use como referência de contraste entre comportamento atual e esperado. Não presuma causa técnica.

```markdown
[BUG] - Impressora Selecionada é Ignorada na Emissão de Etiqueta de Endereço

----

Prezados,

Segue detalhamento do bug onde a impressora selecionada pelo usuário é ignorada na emissão de Etiqueta de Endereço.

----

DESCRIÇÃO / MOTIVO:

Foi identificada uma falha na tela de Etiqueta de Endereço (`/movement/label/address`). Ao acionar a impressão, o modal apresenta as impressoras configuradas e permite que o usuário escolha uma opção.

Atualmente, ao selecionar uma impressora diferente da opção inicialmente apresentada, o campo retorna para a impressora inicial e a impressão não respeita a escolha realizada.

O comportamento esperado é que a opção escolhida permaneça selecionada até a confirmação ou o cancelamento e que a etiqueta seja enviada exclusivamente para essa impressora.

----

SOLICITAÇÃO DE DESENVOLVIMENTO:

Seleção de Impressora

Tela: Etiqueta de Endereço (`/movement/label/address`).

Regras de Negócio:

- O modal deverá listar as impressoras disponíveis para o usuário.
- A impressora escolhida deverá permanecer visível no campo até a confirmação ou o cancelamento.
- Ao confirmar, o sistema deverá enviar a impressão para a opção efetivamente selecionada.

Resultado Esperado do Desenvolvimento:

O usuário deverá conseguir selecionar qualquer impressora disponível e concluir a emissão na opção escolhida, sem retorno automático para a primeira ou para a padrão.

----

RESULTADO ESPERADO:

- Manter no modal a impressora selecionada pelo usuário.
- Direcionar a etiqueta exclusivamente para essa impressora.

----

SUGESTÃO DE CENÁRIOS DE TESTES:

Sessão 1: Seleção e direcionamento

Cenário 1: Seleção de impressora diferente da inicial

Plataforma: Acesso via Web.

Usuário: Operador com permissão de impressão na tela de Etiqueta de Endereço.

Pré-condição: Três impressoras disponíveis para o usuário.

Passos: Acessar a tela, solicitar a impressão, selecionar a segunda impressora e confirmar.

Resultado Esperado: A segunda impressora deverá permanecer selecionada e receber exclusivamente o trabalho de impressão.

Cenário 2: Cancelamento da seleção

Plataforma: Acesso via Web.

Usuário: Operador com permissão de impressão na tela de Etiqueta de Endereço.

Pré-condição: Modal de seleção aberto com mais de uma impressora disponível.

Passos: Abrir o modal, selecionar outra impressora e cancelar.

Resultado Esperado: Nenhum trabalho de impressão deverá ser enviado.

----

Att,

Ramon Mendes.
```
