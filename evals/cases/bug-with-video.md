# Caso de avaliação: bug documentado em vídeo

## Entrada simulada

Um vídeo mostra a tela Etiqueta Endereço, a URL completa com host e porta, três impressoras e o campo retornando à primeira opção após a seleção da terceira. O Product Owner informa somente: “Isto acontece na produção do cliente X; deveria imprimir na escolhida.”

## Comportamento esperado

- Extrair do vídeo o nome da tela, caminho sem host/porta, opções e sequência da falha.
- Não perguntar por fatos visíveis na mídia.
- Perguntar somente por decisões relevantes ainda ausentes, como escopo de perfis ou comportamento do cancelamento, se afetarem a correção.
- Especificar comportamento funcional sem presumir a causa técnica.
- Incluir testes com impressora padrão e alternativa apenas após validação das condições aplicáveis.
