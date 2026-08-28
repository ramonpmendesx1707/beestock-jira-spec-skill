# BeeStock Jira Specification Skill

Skill em português para conduzir o levantamento, a sabatina, a redação e a auditoria de especificações funcionais do WMS BeeStock. Recebe textos, áudios, vídeos, prints e documentos; termina em uma issue pronta para o Jira, sem avançar para código-fonte ou arquitetura interna.

O projeto adapta a mecânica de entrevista e divulgação progressiva de contexto de [mattpocock/skills](https://github.com/mattpocock/skills) para o trabalho de Product Owner.

## O que ela faz

- Trata melhoria e bug como fluxos independentes.
- Extrai fatos dos anexos antes de perguntar.
- Trabalha dúvidas como árvore de decisões em rodadas.
- Oferece recomendação em cada decisão relevante.
- Gera o Jira no padrão funcional do BeeStock.
- Audita completude e clareza antes da versão final.
- Muda imediatamente para modo resumido quando o Product Owner pedir um Jira simples ou uma ideia inicial.
- Registra aprendizados como propostas controladas e versionáveis.

## Skills disponíveis

Os três nomes executam o mesmo motor:

- `criar-especificacao` — nome principal.
- `criar` — alias curto.
- `jira` — alias direto.

## Instalação

Linux, macOS ou WSL:

```bash
git clone <URL-DO-SEU-FORK> beestock-jira-spec-skill
cd beestock-jira-spec-skill
./scripts/install.sh
```

Windows PowerShell:

```powershell
git clone <URL-DO-SEU-FORK> beestock-jira-spec-skill
Set-Location beestock-jira-spec-skill
.\scripts\install.ps1
```

O instalador cria links para a cópia Git. Depois de uma atualização publicada, `git pull` atualiza a skill nos harnesses sem reinstalação. O PowerShell aceita `-Copy` como alternativa quando junctions não estiverem disponíveis, mas cópias não recebem atualizações automaticamente.

## Como chamar

| Harness | Invocação principal | Aliases |
|---|---|---|
| ChatGPT Work | `@criar-especificacao` | `@criar`, `@jira` |
| Codex CLI/IDE | `$criar-especificacao` | `$criar`, `$jira` |
| Claude Code | `/criar-especificacao` | `/criar`, `/jira` |
| DeepSeek Harness | `/criar-especificacao` | `/criar`, `/jira` |
| Hermes Harness | `/criar-especificacao` | `/criar`, `/jira` |

Exemplo:

```text
/jira

Vou enviar um vídeo, dois prints e explicar como o processo funciona atualmente.
```

O modo completo é o padrão. Para encerrar as perguntas e abrir somente com o material disponível:

```text
Quero um Jira resumido como ideia inicial. Use apenas o que já enviei e respondi.
```

## Desenvolvimento

Edite somente `skill-src/criar-especificacao`. Os três bundles em `skills/` são gerados:

```bash
python scripts/build_skills.py
python scripts/validate.py
python -m unittest discover -s tests -v
```

Consulte [Arquitetura](docs/ARCHITECTURE.md), [Compatibilidade](docs/HARNESSES.md) e [Manutenção](docs/MAINTENANCE.md).

## Limite de escopo

A entrega padrão é o texto do Jira. A skill não cria a issue no servidor, não escolhe solução interna de software e não implementa código. Qualquer publicação no Jira exige solicitação e integração separadas.

## Licença e atribuição

Distribuído sob licença MIT. Consulte [LICENSE](LICENSE) e [NOTICE](NOTICE).
