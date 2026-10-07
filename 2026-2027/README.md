# Cours IA 2026-2027 — Guide de l'animateur

**10-12 ans · 2 h par semaine · 14 séances (7 par semestre)**

## L'idée

1. **Semestre 1, début** : on comprend qu'une IA, c'est un **modèle** (un cerveau qui devine la suite d'un texte)
   + un **harness** (tout ce qu'il y a autour : outils, consignes, règles). *Agent = Modèle + Harness.*
2. **Ensuite** : en équipe, chacun réalise un projet qui l'intéresse **et** qui aide quelqu'un (Ikigai),
   en apprenant tout ce qui lui manque **en parlant à une IA**.

## Une séance = toujours les mêmes 3 temps

| | Durée | Quoi |
|---|---|---|
| 🎯 **Le cap** | 10 min | Chaque équipe lit son objectif du jour. |
| 🛠️ **On travaille** | 1 h 20 | 15 min de notion (voir le semestre), puis le projet avec l'IA. |
| 🗣️ **On raconte** | 30 min | Chacun remplit son carnet (10 min), puis chaque équipe parle 2 min. |

À l'oral, le **porte-parole** (une personne différente à chaque séance) répond à 3 questions :
**Qu'avez-vous appris ? L'IA s'est-elle trompée ? Quel est votre prochain objectif ?**

## Les séances

- [Semestre 1](Semestre1/README.md) : comprendre l'IA, choisir son projet, démarrer.
- [Semestre 2](Semestre2/README.md) : construire, tester, présenter.

## À imprimer

| Fiche | Pour qui | Quand |
|---|---|---|
| [Carnet](ressources/a_imprimer/carnet.md) | Chaque élève | Une demi-page par séance |
| [Notre projet](ressources/a_imprimer/projet.md) | Chaque équipe | À partir de S04, reste au club |
| [Mémo IA](ressources/a_imprimer/memo_ia.md) | Affiché sur chaque table | Toute l'année |
| [Mot aux parents](ressources/a_imprimer/mot_aux_parents.md) | Les parents | S01 |

## Les outils de l'animateur

- **Le chat du club** ([chat_du_club/](ressources/chat_du_club/)) : l'IA des élèves. Elle passe par ta clé API et suit les consignes de `coach.txt`.
  ```
  set MISTRAL_API_KEY=ta_cle
  streamlit run chat_du_club.py
  ```
- **La démo du refuge** ([demo/](ressources/demo/)), pour S02 : le même modèle avec 3 harness différents → `python harness_refuge.py`.
- **Les slides** de S01-S02 ([slides/](ressources/slides/modele_et_harness.html)) : ouvrir dans un navigateur, puis flèches ← →.
- **Le notebook** de S08 ([notebook/](ressources/notebook/)) : les élèves construisent leur propre harness.

## Les 3 seules règles à retenir (pour les élèves)

1. **L'IA m'explique, elle ne fait pas à ma place.**
2. **Je vérifie ce qu'elle dit.**
3. **Je ne donne jamais mes infos perso** (ni nom de famille, ni adresse, ni clé API).

## ⚠️ Âge et comptes

Les chatbots grand public demandent 13 ans minimum. Les élèves utilisent donc **le chat du club**,
et l'animateur montre les autres IA en démonstration. Révoquer les clés API en fin d'année.
