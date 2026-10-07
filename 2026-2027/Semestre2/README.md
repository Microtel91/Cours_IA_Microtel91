# Semestre 2 — Construire, tester, présenter

Chaque séance suit les [3 temps](../README.md#une-séance--toujours-les-mêmes-3-temps). Ici : la notion de 15 min,
puis les équipes avancent sur leur projet.

| Séance | Notion du jour (15 min) | Objectif des équipes |
|---|---|---|
| **S08** | **Je construis mon harness** (la séance entière, voir plus bas) | — |
| **S09** | **L'IA peut se tromper** : rejouer la démo du refuge avec un petit modèle (`--modele ministral-3b-latest`). Il répond souvent « Gribouille »… qui est déjà adopté. Les 3 réflexes : **relire, recouper, tester**. | Étape suivante |
| **S10** | **Tester avec de vrais gens** : faire essayer son projet par quelqu'un, sans l'aider. Noter ce qui le bloque. | Faire tester par une autre équipe |
| **S11** | **Les agents qui codent** : l'animateur montre un agent de code (Claude Code, opencode…) qui modifie un petit jeu tout seul. La classe nomme les pièces du harness qu'elle voit. « Les ingénieurs ne tapent presque plus de code : ils décident, ils vérifient. » | Projet presque fini |
| **S12** | **Finir** : ça marche 3 fois de suite sur un autre PC, et chaque membre sait l'expliquer. | Plus de nouveautés, seulement des corrections |
| **S13** | **Raconter son projet** : le problème → notre idée → ce qu'on a appris → la démo. Tout le monde parle. | Répétition devant une autre équipe |
| **S14** | **Le grand jour** : présentation aux parents (7 min par équipe), puis le public essaie les projets. | Bilan du carnet, diplômes 🎉 |

---

## S08 — Je construis mon harness

En binômes, dans Jupyter : ouvrir [S08_mon_harness.ipynb](../ressources/notebook/S08_mon_harness.ipynb) (avec `refuge.csv` dans le même dossier).

Les élèves ajoutent les pièces une par une :
1. le **modèle** seul ;
2. des **consignes** (« Tu es un pirate ») → la réponse change ;
3. un **outil** (exécuter du Python) → le modèle *demande*, il ne lance rien lui-même ;
4. la **boucle** → il trouve la réponse du refuge tout seul ;
5. la **permission** (« Autoriser ? o/n ») et l'**arrêt** (5 étapes maximum).

Bonus : écrire les consignes idéales pour une IA qui aiderait *leur* projet.

Donner une clé API par binôme, et la révoquer après la séance.

## Après S14

Révoquer toutes les clés API. Garder les conseils des élèves pour l'an prochain (dernière question du carnet).
