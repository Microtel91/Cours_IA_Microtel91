# S03 — Le safari des IA (et comment apprendre avec elles)

> **Grande idée** : il n'y a pas « une » IA. Il y a des IA de texte, d'images, de voix, des IA locales, des IA avec
> outils… Chacune a ses forces, ses limites et ses contraintes. Et toutes peuvent devenir un **professeur particulier**,
> à condition de bien leur parler et de les **vérifier**.

**Matériel** : 5 stations (PC), [fiche safari](../ressources/eleves/fiche_safari.md) et [cartes-questions](../ressources/eleves/cartes_questions.md)
imprimées, [charte](../ressources/eleves/charte_ia.md) à signer, chat du club ouvert sur les postes élèves.

## Objectifs

- Tester plusieurs types d'IA et comparer leurs capacités et contraintes (internet, compte, coût, vie privée, énergie).
- Découvrir les **cartes-questions** pour apprendre avec une IA (et pas seulement lui faire faire).
- Signer la charte IA du club.

## Déroulé (2 h)

| Durée | Activité |
|---|---|
| 10 min | Rappel S02 : « quelle pièce du harness ? » (quiz éclair) |
| 50 min | Safari : 5 stations × 10 min |
| 5 min | Pause |
| 25 min | Apprendre avec une IA : les cartes-questions |
| 15 min | La charte + carnet de bord |
| 15 min | Tour des apprentissages |

### Quiz éclair (10 min)

L'animateur lit une situation, les élèves lèvent la couleur de la pièce du harness :
- « Le chatbot cherche sur internet » → outils · « Il se souvient de mon prénom dit plus tôt » → contexte ·
  « Il me demande "Veux-tu vraiment supprimer ?" » → permissions · « Il réessaie après une erreur » → boucle ·
  « Il s'arrête après 10 essais » → arrêt.

### Safari — 5 stations (50 min)

Groupes de 3-4, rotation toutes les 10 min. À chaque station, la fiche safari : *ce qu'elle sait faire / ce qu'elle rate /
ce qui m'a surpris / ses contraintes*.

| Station | IA | Mission |
|---|---|---|
| 1. Le comparateur | Chat du club : `mistral-small` vs `mistral-large` (menu du chat) | Même question aux deux modèles (« Explique les volcans à un enfant de 8 ans »). Lequel est meilleur ? Plus rapide ? |
| 2. L'artiste | Génération d'images (compte animateur, Le Chat) | Faire dessiner « un robot qui arrose un jardin sur un toit de Paris ». Que rate l'IA ? (mains, texte écrit, détails) |
| 3. L'explorateur | Chatbot **avec** recherche web vs chat du club **sans** | « Quel temps fera-t-il demain chez nous ? » Pourquoi un seul y arrive ? (outil !) |
| 4. Le local | Ollama sur le PC animateur, sans internet | Lui poser une question et chronométrer. Avantages : privé, gratuit, sans internet. Limites : plus lent, moins fort. |
| 5. Le traducteur & la voix | Mode vocal / dictée d'un chatbot (compte animateur) | Faire traduire une phrase en 3 langues, puis la faire lire à voix haute. |

Mise en commun (5 min intégrées) : tableau géant « capacités / contraintes ». Faire émerger :
**internet**, **compte et âge** (13 ans minimum pour la plupart → c'est pourquoi on utilise le chat du club),
**coût** (chaque question coûte un peu d'argent sur la clé API de l'animateur), **vie privée** (où partent mes questions ?),
**énergie** (les gros modèles tournent dans des centres de données qui consomment beaucoup d'électricité et d'eau).

### Apprendre avec une IA (25 min)

Démonstration projetée — deux façons de demander :

- ❌ « Fais-moi un jeu du pendu en Python. » → l'IA donne 60 lignes. Qui a appris quelque chose ?
- ✅ « Je veux apprendre à faire un jeu du pendu en Python. J'ai 11 ans et je connais les variables et les boucles.
  Ne me donne pas tout le code : explique-moi les étapes une par une, et pose-moi une question pour vérifier que j'ai compris
  avant de passer à la suivante. »

Distribuer les [cartes-questions](../ressources/eleves/cartes_questions.md). Chaque élève choisit un sujet qui l'intéresse
(« comment marche un volcan », « comment on fait un jeu vidéo »…) et utilise **au moins 3 cartes** avec le chat du club.
Le voisin vérifie qu'il sait réexpliquer.

### Charte + carnet (15 min)

Lire la charte ensemble, chacun la signe (une copie au classeur de l'animateur). Carnet de bord.

## Trace écrite

> Il existe beaucoup d'IA différentes. Chacune a des **capacités** et des **contraintes** (internet, compte, coût, vie privée, énergie).
> Pour **apprendre** avec une IA, je lui demande d'**expliquer** et de me **questionner**, pas seulement de faire à ma place.
