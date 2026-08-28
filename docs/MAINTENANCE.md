# Manutenção e aprendizado

## Regra principal

Edite somente `skill-src/criar-especificacao`. Nunca altere manualmente `skills/criar`, `skills/jira` ou `skills/criar-especificacao`; eles são gerados.

## Ciclo de melhoria

1. Registre a correção observada e classifique-a conforme `references/learning-loop.md`.
2. Confirme com o Product Owner se é regra geral, preferência permanente ou caso isolado.
3. Edite a menor fonte capaz de corrigir o comportamento.
4. Adicione ou ajuste um caso em `evals/cases/` e um teste de contrato quando possível.
5. Execute:

   ```bash
   python scripts/build_skills.py
   python scripts/validate.py
   python -m unittest discover -s tests -v
   ```

6. Faça uma execução comportamental independente usando apenas o caso de avaliação e a skill gerada.
7. Atualize `CHANGELOG.md` e a versão do frontmatter.
8. Commit, tag e push.

## Versionamento

Use SemVer:

- `PATCH`: correção de redação ou comportamento sem mudar o contrato de uso.
- `MINOR`: nova capacidade compatível, rubrica ou modo.
- `MAJOR`: mudança incompatível no fluxo, formato da issue ou invocação.

As versões dos três aliases devem ser idênticas, pois são o mesmo produto.

## Política para aprendizado no Hermes

- Instale por junction/symlink a partir do clone Git.
- Trate toda alteração feita pelo Hermes como diff proposto.
- Não permita auto-commit ou auto-push durante uma execução de Jira.
- Não transforme fato de cliente, regra de uma demanda ou preferência temporária em padrão global.
- Publique apenas depois do gate completo.

## Atualização nos harnesses

Com instalação por link:

```bash
git pull --ff-only
python scripts/validate.py
```

Reinicie apenas o harness que não detectar a alteração automaticamente.
