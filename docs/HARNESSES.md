# Compatibilidade com harnesses

Todos os bundles seguem o formato aberto `SKILL.md` com `name` e `description`, referências relativas e recursos autocontidos.

## Codex e ChatGPT Work

- Diretório local: `~/.agents/skills`.
- Codex: menção explícita com `$nome` ou seleção pelo menu de skills.
- ChatGPT Work: seleção com `@nome` quando a skill estiver disponível na conta/projeto.
- `agents/openai.yaml` desativa invocação implícita e fornece metadados de interface.

## Claude Code

- Diretório: `~/.claude/skills`.
- Invocação: `/nome`.
- `disable-model-invocation: true` mantém o uso explícito.

## DeepSeek Harness

- Diretório compartilhado: `~/.agents/skills`.
- Alternativa nativa: `~/.dsh/skills`.
- Invocação: `/nome`.
- A skill fica em um único nível, pois o mecanismo não depende de descoberta recursiva.
- O DeepSeek Harness está em developer preview; execute `scripts/validate.py` depois de atualizações relevantes do harness.

## Hermes Harness

- Diretório: `${HERMES_HOME:-~/.hermes}/skills`.
- Invocação: `/nome`.
- Bundles autocontidos permitem `skill_view` progressivo das referências.
- Instalação por link mantém o checkout Git como fonte compartilhada.

Hermes pode aprender e propor alterações, mas sua memória e seus patches locais não são automaticamente versões oficiais. Use o fluxo de `docs/MAINTENANCE.md`: proposta, aprovação, teste, versão e push. Isso impede que um ajuste circunstancial afete todas as issues sem revisão.

## Portabilidade

A skill não exige um nome específico de ferramenta para ler arquivos, imagens ou vídeos. Ela descreve capacidades (“inspecione o anexo”, “use agente isolado quando disponível”) e oferece fallback sequencial. Assim, diferenças de ferramentas entre harnesses não quebram o processo.
