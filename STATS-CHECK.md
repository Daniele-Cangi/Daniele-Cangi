# Temporary GitHub Stats Check

> Diagnostic page only. This file is not the profile README and can be removed after inspection.

## Verified result — best current public configuration

The live probe on 2026-10-02 compared the same account against four GitHub Stats Extended configurations.

**Best public result:** broader roles, without `include_all_commits=true`.

![GitHub Stats Extended Best Public Result](https://github-stats-extended.vercel.app/api?username=Daniele-Cangi&show_icons=true&theme=transparent&role=OWNER,ORGANIZATION_MEMBER,COLLABORATOR&rank_icon=percentile)

- Rank: **A+**
- Percentile: **Top 12.2%**
- Stars counted: **194**
- Commits counted: **3,735**
- PRs counted: **624**
- Issues counted: **79**
- Contributed to: **40**

## Private Access test

GitHub Stats Extended can include private contributions after the account authorizes **GitHub Private Access** in its Wizard.

The test card intentionally keeps the best-performing public query unchanged:

![GitHub Stats Extended Private Access Test](https://github-stats-extended.vercel.app/api?username=Daniele-Cangi&show_icons=true&theme=transparent&role=OWNER,ORGANIZATION_MEMBER,COLLABORATOR&rank_icon=percentile)

After Private Access is authorized service-side, this same card is the one to re-check. No private repository names or credentials are stored in this Markdown.

Wizard: https://github-stats-extended.vercel.app/frontend

## Public comparison

| Configuration | Rank | Percentile | Stars | Commits | PRs | Issues |
|---|---:|---:|---:|---:|---:|---:|
| Default | A+ | Top 12.5% | 185 | 3,735 | 624 | 79 |
| `include_all_commits=true` | A | Top 13.9% | 185 | 3,569 | 624 | 79 |
| Broader roles | **A+** | **Top 12.2%** | **194** | **3,735** | **624** | **79** |
| All commits + broader roles | A | Top 15.3% | 185 | 2,558 | 574 | 77 |

## Cards used for comparison

### Default

![GitHub Stats Extended Default](https://github-stats-extended.vercel.app/api?username=Daniele-Cangi&show_icons=true&theme=transparent&rank_icon=percentile)

### All commits

![GitHub Stats Extended All Commits](https://github-stats-extended.vercel.app/api?username=Daniele-Cangi&show_icons=true&theme=transparent&include_all_commits=true&rank_icon=percentile)

### Broader public roles

![GitHub Stats Extended Broader Roles](https://github-stats-extended.vercel.app/api?username=Daniele-Cangi&show_icons=true&theme=transparent&role=OWNER,ORGANIZATION_MEMBER,COLLABORATOR&rank_icon=percentile)

### All commits + broader public roles

![GitHub Stats Extended All Commits And Roles](https://github-stats-extended.vercel.app/api?username=Daniele-Cangi&show_icons=true&theme=transparent&include_all_commits=true&role=OWNER,ORGANIZATION_MEMBER,COLLABORATOR&rank_icon=percentile)

> Note: the non-monotonic result from `include_all_commits=true` is intentional to keep visible for diagnosis. It should not be assumed to mean “more history = more counted activity” on this service without checking its query behavior.
