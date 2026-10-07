# S08 — Je construis mon harness

> **Grande idée** : on passe de l'autre côté. Jusqu'ici on *utilisait* des harness. Aujourd'hui, on en **construit** un,
> en Python, pièce par pièce : le modèle, le contexte, un outil, la boucle, une permission, un arrêt.

**Matériel** : [notebooks/S08_mon_harness.ipynb](../ressources/notebooks/S08_mon_harness.ipynb) copié sur les postes avec `refuge.csv`,
une clé API par groupe (à révoquer après la séance), Jupyter (Anaconda Navigator → Jupyter Notebook).

## Objectifs

- Appeler un modèle depuis Python (une requête = une étape).
- Ajouter du **contexte** (les consignes système) et voir le comportement changer.
- Ajouter un **outil** et une **boucle**, puis une **permission** et un **arrêt**.
- Repartir avec l'idée : « le chat du club, c'est exactement ça, en un peu plus joli ».

## Déroulé (2 h)

| Durée | Activité |
|---|---|
| 10 min | Rappel : les 5 pièces (quiz couleurs) |
| 10 min | Mise en route : ouvrir Jupyter, coller la clé |
| 70 min | Le notebook, en binômes (6 étapes) |
| 5 min | Pause |
| 10 min | Carnet de bord |
| 15 min | Tour des apprentissages |

### Le notebook (70 min)

Les élèves travaillent **en binômes** (un au clavier, un qui lit les consignes ; on échange à chaque étape).
Ils ont le droit — et c'est encouragé — de demander au chat du club d'expliquer une ligne qu'ils ne comprennent pas.

1. **Le modèle seul** — envoyer une question, lire la réponse.
2. **Le contexte** — ajouter un message `system` : « Tu es un pirate. » puis « Tu es un prof de maths qui ne donne jamais la réponse. »
3. **Le défi du refuge sans outil** — la même question qu'en S02 : il ne peut pas savoir.
4. **L'outil** — donner au modèle l'outil `executer_python` et regarder sa **demande** (il ne lance rien lui-même !).
5. **La boucle** — exécuter la demande, renvoyer le résultat, recommencer jusqu'à la réponse.
6. **Permissions & arrêt** — demander « o/n » avant d'exécuter, et limiter à 5 étapes.

**Défi bonus** (pour les rapides) : transformer le harness en assistant de **leur projet** : écrire le message `system`
qui décrit leur projet et leurs règles (« ne donne jamais le code entier », « réponds comme à un enfant de 11 ans »).
C'est l'équivalent du fichier `AGENTS.md` des agents de code professionnels.

### Lien avec le projet

Les groupes dont le projet est un chatbot (révision, recettes, guide…) repartent avec la base de leur projet.
Pour les autres : « Quelles règles donneriez-vous à l'IA qui vous aide ? » → ils écrivent leur **fiche de règles**
dans la feuille de route, et l'utilisent en début de chaque conversation avec le Coach.

## Points d'attention

- Le code du notebook est fourni : l'objectif n'est pas de tout écrire, c'est de **comprendre chaque pièce** et de **modifier**.
- Une clé API ne se partage pas, ne se met pas dans une capture d'écran, ne se colle jamais dans un chatbot.
- Si l'API ne répond pas (réseau) : faire la séance en projetant le notebook avec Ollama en local (`URL` dans la 1re cellule).
