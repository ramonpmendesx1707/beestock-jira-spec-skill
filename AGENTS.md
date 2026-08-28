# Instruções do repositório

Este repositório distribui uma skill funcional do WMS BeeStock para múltiplos harnesses.

- Edite a fonte somente em `skill-src/criar-especificacao`.
- Gere `skills/` com `python scripts/build_skills.py` depois de qualquer alteração.
- Mantenha Codex, Claude Code, DeepSeek Harness e Hermes Harness compatíveis; use apenas capacidades com fallback descrito.
- Preserve o limite funcional: negócio, comportamento esperado e testes; não acrescente desenvolvimento de código ao fluxo da skill.
- Trate cada demanda Jira como independente.
- O modo completo é padrão; um pedido explícito de Jira resumido interrompe a sabatina.
- Aprendizados permanentes exigem aprovação, teste, changelog e versão.
- Antes de concluir mudanças, execute `python scripts/validate.py` e `python -m unittest discover -s tests -v`.
