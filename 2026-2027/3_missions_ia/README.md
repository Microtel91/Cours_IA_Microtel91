# Les missions IA

Des explorations courtes (30 à 45 min) pour découvrir **d'autres IA** et voir le harness de plus près.
Une équipe choisit une mission **quand elle sert son projet**. Objectif : **au moins 4 missions dans l'année**, dont la M6.

Après une mission, l'équipe :
1. écrit dans son journal ce que cette IA **sait faire**, ce qu'elle **rate**, et quelle **pièce du harness** fait la différence ;
2. inscrit son nom sur le **mur des experts**.

| | Mission | Pièce du harness | Utile si le projet… |
|---|---|---|---|
| M1 | [Chercher sur internet](#m1--chercher-sur-internet) | 🛠️ outils | a besoin d'infos récentes ou vérifiées |
| M2 | [Créer des images](#m2--créer-des-images) | 🧠 modèle | a besoin de dessins, d'un logo, d'illustrations |
| M3 | [La voix et les langues](#m3--la-voix-et-les-langues) | 🧠 modèle | parle, lit à voix haute, traduit |
| M4 | [Une IA sans internet](#m4--une-ia-sans-internet) | 🧠 modèle | doit rester privé, ou marcher sans connexion |
| M5 | [Petit ou gros modèle ?](#m5--petit-ou-gros-modèle-) | 🧠 modèle | utilise un chatbot |
| M6 | [Donner des règles à son IA](#m6--donner-des-règles-à-son-ia) | 📖 contexte · 🚦 permissions | **tous les projets** |
| M7 | [Construire son harness](#m7--construire-son-harness) | toutes | est un chatbot ou un assistant |
| M8 | [Regarder un agent coder](#m8--regarder-un-agent-coder) | 🔁 boucle · 🚦 permissions | contient du code |

---

## M1 — Chercher sur internet

Poser la même question d'actualité (« Quel temps fera-t-il demain ici ? », « Quel est le dernier film sorti au cinéma ? ») à une IA **avec** recherche web, puis au chat du club **sans**.
Pourquoi une seule y arrive ? Ensuite, ouvrir une des sources qu'elle cite : dit-elle vraiment la même chose ?

## M2 — Créer des images

Avec l'animateur (compte de démonstration), créer une image pour le projet. Essayer de faire écrire un mot dans l'image, et de dessiner des mains. Que rate l'IA ?
Puis demander « un scientifique », « une personne qui fait le ménage » : qui l'IA dessine-t-elle ? Ce sont des **biais**, qui viennent des images qu'elle a vues.

## M3 — La voix et les langues

Faire traduire une phrase du projet en 3 langues, puis la faire lire à voix haute. Demander à quelqu'un qui parle la langue si c'est juste.

## M4 — Une IA sans internet

Sur le PC de l'animateur, avec Ollama, ou dans le chat du club → « Qwen local ». Poser la même question qu'au chat normal et chronométrer.
Elle est plus lente et moins forte… mais rien ne quitte l'ordinateur. Quand est-ce que c'est important ?

## M5 — Petit ou gros modèle ?

Dans le chat du club, poser la même question du projet à « Ministral 3B » puis à « Mistral Large ». Lequel répond le mieux ? Le plus vite ?
Même harness, modèle différent : **résultat différent**. Puis refaire le labo onglet 2 avec le petit modèle.

## M6 — Donner des règles à son IA

Compléter « Nos règles pour l'IA » dans `projet.md` (« réponds en 5 phrases maximum », « explique chaque ligne de code », « ne change jamais nos textes sans demander »…).
Comparer : la même question **sans** coller `projet.md`, puis **avec**. Ce qui change, c'est le **contexte**. Les pros font pareil avec un fichier `AGENTS.md`.

## M7 — Construire son harness

En binôme, dans Jupyter : le [notebook](../ressources/notebook/mon_harness.ipynb). On ajoute les pièces une par une (modèle, consignes, outil, boucle, permission, arrêt).
Bonus : y mettre les règles de `projet.md`. C'est le début d'un vrai chatbot pour le projet.

## M8 — Regarder un agent coder

Avec l'animateur, qui utilise un agent de code (Claude Code, opencode…) sur une copie du projet.
1. Prédire : « Qu'est-ce qu'il va faire en premier ? »
2. Observer, en nommant la pièce du harness à chaque action.
3. Vérifier : on lance le projet. A-t-il fait ce qu'il dit ?

Les ingénieurs travaillent comme ça : **ils décident, l'agent fait, ils vérifient.**
