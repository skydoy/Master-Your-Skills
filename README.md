# Master Your Skills

Um único plugin para o Claude Code com regras de trabalho unificadas (`AGENTS.md`) e 60 skills
de engenharia, juntando o melhor de três projetos:

- **[ponytail](https://github.com/DietrichGebert/ponytail)**: menos código, menos tokens (a mudança mais pequena que resolve).
- **[agent-skills](https://github.com/addyosmani/agent-skills)**: fluxo completo spec → plano → build → teste → revisão → ship.
- **[mattpocock/skills](https://github.com/mattpocock/skills)**: hábitos de engenharia real (TDD em seams, módulos profundos, debugging com feedback loop).

## Instalar (Claude Code)

```
/plugin marketplace add skydoy/Master-Your-Skills
/plugin install master-your-skills@master-your-skills
```

Se já tens `ponytail`, `agent-skills` ou `mattpocock-skills` instalados, desinstala-os para não teres skills a dobrar:

```
/plugin uninstall ponytail
/plugin uninstall agent-skills
```

## Usar o AGENTS.md

- **Num projeto:** copia `AGENTS.md` para a raiz do projeto (o Claude Code também lê `CLAUDE.md`).
- **Em todos os projetos:** copia o conteúdo para `C:\Users\<tu>\.claude\CLAUDE.md` (Windows) ou `~/.claude/CLAUDE.md`.
- Também está disponível como a skill `master-your-skills`.

## O que vem incluído

| Tipo | Itens |
|---|---|
| Regras | `AGENTS.md`, skill `master-your-skills` |
| Comandos | `/spec` `/plan` `/build` `/test` `/review` `/ship` `/constraints` `/code-simplify` `/a11y` `/webperf` |
| Agentes | code-reviewer, security-auditor, test-engineer, accessibility-auditor, web-performance-auditor |
| Skills ponytail | ponytail, ponytail-review, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help |
| Skills agent-skills | spec-driven-development, planning-and-task-breakdown, incremental-implementation, test-driven-development, debugging-and-error-recovery, code-review-and-quality, code-simplification, git-workflow-and-versioning, security-and-hardening, performance-optimization, frontend-ui-engineering, api-and-interface-design, e mais |
| Skills mattpocock | tdd, diagnosing-bugs, codebase-design, domain-modeling, code-review, grilling, grill-me, to-spec, to-tickets, prototype, handoff, e mais |

Os hooks do ponytail (badge e quadro de custos) não estão incluídos; instala o plugin original se os quiseres.

## Créditos e licença

MIT. As skills são cópias dos projetos originais, também MIT: ver [NOTICE.md](NOTICE.md) e `licenses/`.
Para atualizar, volta a copiar das fontes indicadas no NOTICE.
