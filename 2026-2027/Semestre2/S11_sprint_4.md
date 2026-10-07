# S11 — Sprint 4 · Capsule : les agents qui agissent

Format : [sprint](../Semestre1/S06_sprint_1.md). Seule la capsule change.

## Capsule (20 min) — Démo d'un agent de code

> **Grande idée** : en 2026, beaucoup d'ingénieurs et de scientifiques n'écrivent presque plus de code à la main.
> Ils décrivent le but à un **agent de code** (Claude Code, Codex, opencode…), qui lit, écrit, lance et teste les programmes
> dans une **boucle**. Leur travail : bien définir l'objectif, fixer les règles, et **vérifier** le résultat.

Démo projetée par l'animateur (agent de code sur son PC, dans un dossier de test, avec git) :

1. **Prédire** : « Je vais demander à l'agent : *Ajoute un score et un chronomètre au jeu du pendu, puis vérifie que ça marche.*
   Quels outils va-t-il utiliser en premier ? »
2. **Observer** l'agent travailler. La classe annonce la pièce du harness à chaque action :
   il lit un fichier (outil) · il lance le programme (outil + boucle) · il demande la permission (permissions) ·
   il lit `AGENTS.md` (contexte) · il annonce « terminé » (arrêt).
3. **Vérifier** : on lit ensemble ce qu'il a changé (`git diff`) et on lance le jeu. A-t-il dit la vérité dans son message final ?
4. Montrer le fichier `AGENTS.md` : des règles écrites par l'humain (« lance les tests après chaque modification »,
   « ne supprime jamais de fichier »). « C'est la même chose que la fiche de règles que vous avez écrite en S08. »

Message à faire passer : **on ne devient pas inutile, on devient chef d'équipe des IA**. Il faut savoir ce qu'on veut,
découper, vérifier — exactement ce que vous faites depuis le début de l'année.

## Atelier

Le projet doit être **presque fini** à la fin de la séance : tout ce qui est dans le « minimum qui compte » marche.
Ce qui n'est pas commencé passe en « si on a le temps ».
