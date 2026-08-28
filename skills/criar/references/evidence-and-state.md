# Evidências e estado do caso

## Objetivo

Transformar materiais heterogêneos em uma fonte de verdade rastreável antes das perguntas. Não reproduza transcrições inteiras; extraia decisões e fatos úteis.

## Registro do caso

Mantenha, no contexto ou em um diretório temporário do workspace, um pacote equivalente a:

```text
caso/
├── FONTES.md
├── ENTENDIMENTO.md
├── DECISOES.md
├── RASCUNHO.md
├── AUDITORIA.md
└── FINAL.md
```

Use arquivos quando o caso atravessar sessões, sofrer compactação ou precisar viajar entre harnesses. Em uma conversa curta, o registro estruturado no contexto é suficiente. Não copie anexos sensíveis para o repositório da skill.

### FONTES.md

Liste cada fonte e o que ela comprovou:

| Fonte | Tipo | Conteúdo relevante | Limitação |
|---|---|---|---|
| Vídeo 1 | vídeo | Operador reproduz falha após confirmar | Não mostra perfil do usuário |

### ENTENDIMENTO.md

Registre:

- Tipo: `MELHORIA`, `BUG` ou `A CONFIRMAR`.
- Problema e impacto.
- Processo atual.
- Comportamento desejado.
- Atores e plataformas.
- Elementos do BeeStock citados: telas, URLs, cadastros, parâmetros, documentos, status e integrações.
- Escopo sugerido e limites ainda incertos.

### DECISOES.md

Use um ledger, não uma narrativa:

| ID | Estado | Decisão ou lacuna | Evidência/resposta | Impacto |
|---|---|---|---|---|
| D01 | CONFIRMADO | Permitir devolução parcial | Resposta da rodada 1 | Fluxo e testes |
| D02 | A DEFINIR | Quantidade máxima permitida | — | Integridade de estoque |

Estados:

- `CONFIRMADO`: declarado ou demonstrado sem ambiguidade.
- `INFERIDO`: leitura provável que ainda exige validação.
- `A DEFINIR`: decisão necessária sem resposta.
- `FORA DO ESCOPO`: deliberadamente excluído.

## Extração de evidências

- Leia transcrições completas e associe falas às regras correspondentes.
- Em prints, procure nome da tela, campos, mensagens, status e URL. Ao citar a URL do BeeStock, remova protocolo, host e porta; preserve apenas o caminho iniciado por `/`.
- Em vídeos, separe ação do usuário, resposta do sistema e ponto em que o comportamento diverge do esperado.
- Normalize referências Jira para `https://szsolucoes.atlassian.net/browse/CHAVE-123`.
- Se uma mídia não puder ser lida, identifique exatamente a fonte faltante e o dado que ela deveria esclarecer.

## Isolamento entre demandas

Um novo assunto cria um novo ledger. Só reutilize uma regra quando o usuário apontar explicitamente uma demanda anterior ou quando ela estiver registrada como regra estável aprovada do BeeStock. Exemplos e Jiras anteriores orientam formato ou comportamento análogo; não tornam automaticamente idênticos os processos.

## Pacote de continuidade

Antes de trocar de harness ou sessão, gere um `HANDOFF.md` contendo:

1. Objetivo e tipo da demanda.
2. Fontes inspecionadas.
3. Fatos confirmados.
4. Decisões tomadas e justificativas.
5. Perguntas ainda abertas e suas dependências.
6. Estado atual da máquina de estados.
7. Próxima ação exata.

O pacote é uma fonte secundária. Sempre que possível, mantenha a conversa original até concluir a auditoria final.
