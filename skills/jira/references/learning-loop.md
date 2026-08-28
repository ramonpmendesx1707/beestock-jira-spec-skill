# Aprendizado controlado e versionado

O aprendizado deve melhorar execuções futuras sem transformar um caso isolado em regra universal.

## Classificação da correção

Quando o usuário corrigir a saída ou o processo, classifique:

- `FATO DO CASO`: pertence apenas à demanda atual. Atualize o ledger do caso.
- `REGRA ESTÁVEL DO BEESTOCK`: comportamento de domínio reutilizável, confirmado como geral.
- `PREFERÊNCIA DO PRODUCT OWNER`: convenção de escrita, estrutura ou condução aplicável às próximas issues.
- `FALHA DO MÉTODO`: a skill perguntou mal, presumiu algo, perdeu informação ou aprovou um gap.
- `VARIAÇÃO`: preferência circunstancial sem evidência para virar padrão.

## Candidato a aprendizado

Um candidato reutilizável deve registrar:

```markdown
## AAAA-MM-DD — título

- Classificação:
- Situação observada:
- Comportamento atual da skill:
- Comportamento proposto:
- Evidência ou exemplos:
- Escopo da regra:
- Risco de generalização:
- Teste de regressão sugerido:
- Estado: PROPOSTO | APROVADO | REJEITADO | INCORPORADO
```

Não altere o comportamento permanente durante a execução da issue. Ao final, apresente o candidato ao usuário quando ele for material. Se aprovado, registre-o no repositório da skill, adicione ou ajuste um teste comportamental e incremente a versão conforme `docs/MAINTENANCE.md` do projeto.

## Hermes Harness

Hermes pode propor ou aplicar patches em skills. Mantenha esta skill instalada a partir do checkout Git e trate o diff como proposta revisável. O histórico Git é a fonte de verdade compartilhada entre todos os harnesses; a memória ou cópia local do Hermes não substitui uma versão publicada.

Uma evolução é concluída somente quando:

1. A regra foi aprovada pelo usuário.
2. O arquivo correto foi alterado na fonte canônica.
3. Os aliases foram reconstruídos.
4. Validadores e testes comportamentais passaram.
5. A mudança recebeu commit, versão e publicação no GitHub.
