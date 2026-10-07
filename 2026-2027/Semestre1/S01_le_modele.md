# S01 — Le cerveau dans le bocal

> **Grande idée** : un modèle d'IA ne fait qu'une chose — lire du texte et écrire la suite la plus probable.
> Il ne « sait » pas ce qui se passe aujourd'hui, ni ce qui n'est pas dans ses données.

**Matériel** : [slides](../ressources/slides/modele_et_harness.html) (partie 1), chat du club ouvert sur le PC animateur et projeté,
[carnet de bord](../ressources/eleves/carnet_de_bord.md) imprimé (1 par élève), post-its.

## Objectifs

- Savoir dire avec ses mots ce qu'est un **modèle**.
- Comprendre pourquoi une IA peut inventer (**halluciner**).
- Découvrir le carnet de bord et le tour des apprentissages.

## Déroulé (2 h)

| Durée | Activité |
|---|---|
| 15 min | Accueil, présentation de l'année, sondage à main levée |
| 20 min | Jeu 1 : la machine à suite |
| 20 min | Explication : qu'est-ce qu'un modèle ? |
| 30 min | Jeu 2 : piéger le modèle |
| 5 min | Pause |
| 15 min | Carnet de bord (1re page) |
| 15 min | Premier tour des apprentissages |

### Accueil (15 min)

- « Cette année, on ne va pas apprendre à coder comme l'an dernier. On va apprendre à **faire travailler des IA**,
  et à **apprendre avec elles**. En fin d'année, chaque équipe aura réalisé le projet de ses rêves, un projet utile au monde. »
- Sondage : qui a déjà parlé à une IA ? Pour faire quoi ? Qui pense que l'IA *comprend* ce qu'on lui dit ?
  Noter les réponses au tableau — on y reviendra en fin de séance.

### Jeu 1 — La machine à suite (20 min, sans écran)

1. L'animateur écrit au tableau : « Le chat est monté sur le … ». Chaque élève écrit le mot suivant sur un post-it.
2. On colle les post-its et on les regroupe : *toit* (beaucoup), *canapé*, *arbre*… et un « dinosaure » (rires).
3. « Vous venez de faire ce que fait un modèle : choisir la suite **la plus probable** d'après tout ce que vous avez déjà lu. »
4. On rallonge : chaque élève ajoute un mot à la phrase du voisin → on obtient un texte entier, mot après mot.
   « Un modèle écrit **un morceau de mot à la fois** (un *token*), des milliers de fois, très vite. »

### Explication (20 min, slides partie 1)

- Un modèle a « lu » une quantité énorme de textes (des milliards de pages) pendant son **entraînement**.
- Il en a tiré un réflexe : deviner la suite. Il n'a ni yeux, ni mains, ni montre, ni internet.
- Son entraînement s'arrête à une date : après, il ne sait rien.
- **Le cerveau dans le bocal** : imaginer un cerveau très cultivé, enfermé dans un bocal, qui ne peut qu'écrire sur un papier.
  Il est brillant… mais il ne voit rien de ce qui se passe dehors.
- Noms à connaître : Mistral (français 🇫🇷), Claude, GPT, Gemini, Llama, Qwen. « Les chatbots ont des noms
  différents des modèles : *Le Chat* utilise des modèles Mistral, *ChatGPT* des modèles GPT. »

### Jeu 2 — Piéger le modèle (30 min, en groupes de 3)

Sur le chat du club (projeté ou sur leurs postes), les groupes essaient de faire **inventer** le modèle.
Questions de départ (à donner sur un papier) :

- « Comment s'appelle l'animateur du cours d'IA de Microtel91 ? »
- « Qu'est-ce que j'ai mangé ce matin ? »
- « Quel temps fait-il maintenant devant l'association ? »
- « Raconte-moi la biographie de [prénom inventé + nom inventé], le célèbre explorateur. »
- « Combien y a-t-il de lettres "e" dans "l'élève révèle ses rêves" ? » (les modèles se trompent souvent en comptant les lettres : ils voient des morceaux de mots, pas des lettres)

Chaque groupe note :
- la question, la réponse, et **vrai / faux / il a avoué ne pas savoir**.

Mise en commun : « Pourquoi il invente ? » → il est fait pour écrire une suite *plausible*, pas une suite *vraie*.
On appelle ça une **hallucination**.

**Question piège pour finir** : « Quelle est la date d'aujourd'hui ? » → souvent il répond juste ! Comment est-ce possible
si le modèle est dans un bocal ? Laisser chercher… et garder le suspense : **« Réponse la semaine prochaine. »**
(La réponse : quelqu'un a écrit la date dans ses consignes — c'est le *harness*. C'est le sujet de S02.)

### Carnet de bord (15 min)

Distribuer le carnet. Expliquer qu'on le remplira **à chaque séance**, toute l'année, et qu'il sera rendu en fin d'année.
Remplir la page 1 ensemble : « Pour moi, une IA c'est… » (avant) puis la fiche de séance.

### Tour des apprentissages (15 min)

Première fois : l'animateur montre l'exemple, puis 3-4 volontaires. Revenir sur le sondage du début :
« Est-ce que l'IA *comprend* ? » — pas de bonne réponse unique, mais on sait maintenant comment elle fonctionne.

## Points d'attention

- Ne pas dire « l'IA ment » : elle n'a pas l'intention de tromper. Elle *devine*.
- Si un modèle refuse de répondre (« je ne sais pas »), c'est une bonne chose : le féliciter ! Les modèles récents
  inventent moins qu'avant, d'où l'intérêt de varier les questions.
- Retenir les prénoms : c'est la séance où l'on crée la confiance.

## Trace écrite (au tableau, recopiée dans le carnet)

> Un **modèle** est un programme qui a lu énormément de textes et qui devine la suite d'un texte.
> Il peut **inventer** quand il ne sait pas : c'est une **hallucination**.
