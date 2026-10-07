# Cours IA 2026-2027 — Guide de l'animateur

**Microtel91 · 10-12 ans (ont déjà fait du Python) · 2 h par semaine · 14 séances**

## L'idée

Comme dans la vraie vie en 2026 : **on apprend beaucoup grâce aux IA, et les IA font une bonne partie du travail**.
Pour avancer avec elles, il faut comprendre comment elles marchent, quand elles se trompent, et ce qu'on doit retenir soi-même.

1. **Peu de cours** : 3 séances de tronc commun sur le modèle, le harness, et la façon de travailler avec l'IA.
2. **Beaucoup de projet** : en équipe, sur un sujet qui les intéresse et qui aide quelqu'un.
   Chaque équipe suit un **parcours de 6 jalons**, à son rythme.
3. **Plusieurs IA** : des **missions** courtes pour en essayer d'autres, quand le projet en a besoin.

## L'année en un coup d'œil

| Séances | Phase | Pour tous ou à son rythme ? |
|---|---|---|
| S01 – S03 | [1 · Tronc commun](1_tronc_commun/) : [le modèle](1_tronc_commun/S01_le_modele.md), [le harness](1_tronc_commun/S02_le_harness.md), [travailler avec l'IA](1_tronc_commun/S03_travailler_avec_l_ia.md) | pour tous |
| S04 – S05 | [2 · Lancement](2_projets/1_lancement.md) : Ikigai, équipes, dossier d'équipe | pour tous |
| S06 – S13 | [Le parcours](2_projets/2_parcours.md), en [séances projet](2_projets/3_seance_projet.md), avec des [missions IA](3_missions_ia/README.md) | **à son rythme** |
| S07 | [Démo de mi-parcours](2_projets/4_rendez_vous.md#s07--la-démo-de-mi-parcours-fin-du-semestre-1) (fin du semestre 1) | pour tous |
| S13 – S14 | [Répétition et grand jour](2_projets/4_rendez_vous.md) | pour tous |

## 4 façons de travailler avec l'IA

| | Façon | Quand ? | Ce qu'on attend |
|---|---|---|---|
| 🤖 | **L'IA fait** | Une chose qu'on ne refera sans doute pas | Savoir dire en une phrase ce qu'elle a fait |
| 🤝 | **L'IA fait, je comprends** | La plupart du temps | Savoir expliquer chaque partie, et en modifier une seul |
| 🧑 | **Je fais, l'IA m'aide** | Le cœur du projet, ce qui m'intéresse | L'IA donne des indices, c'est moi qui écris |
| 🧠 | **Je retiens** | Quand le même problème **revient** | Le noter dans « À retenir », et savoir le refaire sans IA |

> **Je dois pouvoir expliquer tout ce que je montre. Et si un problème revient, je le retiens.**

## Ce qui sert toute l'année

| | Quoi | Utilisé en |
|---|---|---|
| [Labo IA](ressources/supports/labo_ia.html) | Page interactive : le modèle choisit la suite (onglet 1), on équipe le cerveau d'un harness (onglet 2) | S01, S02, capsules, S14 |
| [Slides](ressources/supports/modele_et_harness.html) | Modèle et harness, en images | S01, S02 |
| [Chat du club](ressources/chat_du_club/) | L'IA des élèves (ta clé API, les consignes de `coach.txt`) : `set MISTRAL_API_KEY=ta_cle` puis `streamlit run chat_du_club.py` | toute l'année |
| [Dossier d'équipe](ressources/dossier_equipe/) | `projet.md` (le contexte de l'équipe) et `journal.md` (une entrée par séance, plus « À retenir »), à copier sur le réseau pour chaque équipe | à partir de S05 |
| [Démo du refuge](ressources/demo/) | La même chose que le labo, avec un vrai modèle : `python harness_refuge.py` | S02 (variante) |
| [Notebook](ressources/notebook/) | Construire son propre harness | mission M7 |

## Sécurité

- Les élèves ne donnent jamais à une IA leur nom de famille, leur adresse, une photo ou une clé API.
- Les chatbots grand public demandent 13 ans minimum : les élèves utilisent **le chat du club**, et l'animateur montre les autres IA avec son compte.
- Révoquer les clés API à la fin de l'année.
