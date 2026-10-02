# Contribuer à Boutik

## Le workflow (GitHub Flow)

1. **Une issue** décrit chaque tâche. Assigne-toi l'issue avant de commencer.
2. **Une branche** par issue, créée depuis `main` à jour :
   ```bash
   git switch main
   git pull
   git switch -c fix/3-tva
   ```
3. **Des petits commits** au format Conventional Commits.
4. **Les tests passent** en local : `python -m pytest` (ou `python run_tests.py`).
5. **Une Pull Request** vers `main`, avec `Closes #<n°>` dans la description.
6. **Une review** par un coéquipier : il teste la branche, commente, puis approuve.
7. **Squash and merge**, puis **Delete branch**. Tout le monde fait `git pull` sur `main`.

## Conventions

| Quoi | Convention | Exemple |
| --- | --- | --- |
| Branche de bug | `fix/<n°>-<description>` | `fix/3-tva` |
| Branche de fonctionnalité | `feature/<n°>-<description>` | `feature/9-code-promo` |
| Branche de documentation | `docs/<description>` | `docs/equipe-lea` |
| Correctif urgent | `hotfix/<n°>-<description>` | `hotfix/17-crash-panier` |
| Commit | `type(portée): description` | `fix(pricing): corrige le calcul de la TVA` |

Types de commit : `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.

## Définition de « terminé »

- [ ] Les tests passent (en local **et** sur GitHub Actions)
- [ ] La PR est liée à son issue (`Closes #<n°>`)
- [ ] La PR a été relue et approuvée par au moins une personne
- [ ] La branche est supprimée après le merge

## Règles d'or

- On ne pousse **jamais** directement sur `main`.
- On fait `git pull` avant de créer une branche.
- En cas de conflit : on garde le travail de **tout le monde**, on relance les tests, puis on pousse.
