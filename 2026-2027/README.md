# Cours IA 2026-2027 — Guide de l'animateur

**Microtel91 · 10-12 ans (ont déjà fait du Python) · 2 h par semaine · 14 séances, 7 par semestre**

## L'idée

1. **Comprendre** (S01-S03) : une IA, c'est un **modèle** (un cerveau qui devine la suite d'un texte)
   + un **harness** (tout ce qu'il y a autour : outils, consignes, règles). *Agent = Modèle + Harness.*
2. **Construire** (S04-S14) : en équipe, chacun réalise un projet qui lui plaît **et** qui aide quelqu'un (Ikigai).
   Tout ce qui manque, on l'apprend **avec l'IA**.

Les vrais ingénieurs de 2026 font écrire leur code par des IA. Ce qu'on apprend ici, c'est leur métier :
**dire clairement ce qu'on veut, comprendre ce que l'IA a fait, vérifier, et retenir ce qui compte.**

## Le cœur du cours : 4 façons de travailler avec l'IA

| | Façon | Quand ? | Ce qu'on attend |
|---|---|---|---|
| 🤖 | **L'IA fait** | Une chose qu'on ne refera sans doute pas | Savoir dire en une phrase ce qu'elle a fait |
| 🤝 | **L'IA fait, je comprends** | La plupart du temps | Savoir expliquer chaque partie, et en modifier une seule tout seul |
| 🧑 | **Je fais, l'IA m'aide** | Le cœur du projet, ce qui m'intéresse | L'IA donne des indices, c'est moi qui écris |
| 🧠 | **Je retiens** | Quand le même problème **revient** | Le noter dans « À retenir », et savoir le refaire sans IA |

Aucune façon n'est interdite. La règle est simple :

> **Je dois pouvoir expliquer tout ce que je montre. Et si un problème revient, je le retiens.**

Les questions à poser souvent : *« Qu'est-ce que l'IA a fait, là ? »*, *« Si je supprime cette ligne, que se passe-t-il ? »*,
*« Tu l'as déjà demandé la semaine dernière : tu sais le faire, maintenant ? »*

## Une séance = toujours les mêmes 3 temps

| | Durée | Quoi |
|---|---|---|
| 🎯 **Le cap** | 10 min | Chaque équipe relit son prochain objectif dans son journal. |
| 🛠️ **On travaille** | 1 h 20 | Une notion de 15 min (voir la fiche de la séance), puis le projet avec l'IA. |
| 🗣️ **On raconte** | 30 min | Chaque équipe complète son journal (10 min), puis parle 2 min à l'oral. |

À l'oral, le **porte-parole** (une personne différente à chaque séance) répond à 3 questions :
1. **Qu'avez-vous appris ?**
2. **Qu'a fait l'IA pour vous, et l'avez-vous compris ?**
3. **Quel est votre prochain objectif ?**

## Les séances

| Semestre 1 — Comprendre et démarrer | Semestre 2 — Construire et présenter |
|---|---|
| [S01 Le cerveau dans le bocal](Semestre1/S01_le_modele.md) | [S08 Je construis mon harness](Semestre2/S08_mon_harness.md) |
| [S02 Le harness](Semestre1/S02_le_harness.md) | [S09 L'IA peut se tromper](Semestre2/S09_l_ia_se_trompe.md) |
| [S03 Les 4 façons de travailler avec l'IA](Semestre1/S03_quatre_facons.md) | [S10 Faire tester son projet](Semestre2/S10_tester.md) |
| [S04 Mon Ikigai, notre projet](Semestre1/S04_ikigai.md) | [S11 Les agents qui codent](Semestre2/S11_agents.md) |
| [S05 Notre mission et nos étapes](Semestre1/S05_mission.md) | [S12 Finir](Semestre2/S12_finir.md) |
| [S06 On démarre](Semestre1/S06_on_demarre.md) | [S13 Raconter son projet](Semestre2/S13_raconter.md) |
| [S07 On montre ce qu'on a](Semestre1/S07_mi_parcours.md) | [S14 Le grand jour](Semestre2/S14_grand_jour.md) |

## Organisation sur les PC du club

Chaque équipe a **un dossier** sur le réseau (par exemple `Equipes/Les_Recycleurs/`), créé en S05 en copiant
[ressources/dossier_equipe/](ressources/dossier_equipe/) :

- `projet.md` : la mission, les étapes, les règles pour l'IA. C'est **le contexte** de l'équipe : on le colle au Coach en début de séance.
- `journal.md` : une entrée par séance, plus la liste **« À retenir »**.
- le code et les fichiers du projet.

## Les outils de l'animateur

| Outil | Pour quoi | Lancer |
|---|---|---|
| [Chat du club](ressources/chat_du_club/) | L'IA des élèves, avec ta clé API et les consignes de `coach.txt` | `set MISTRAL_API_KEY=ta_cle` puis `streamlit run chat_du_club.py` |
| [Démo du refuge](ressources/demo/) | S02 et S09 : un même modèle avec 3 harness | `python harness_refuge.py` |
| [Slides](ressources/slides/modele_et_harness.html) | S01-S02 | Ouvrir dans un navigateur, puis les flèches ← → |
| [Notebook](ressources/notebook/) | S08 : les élèves construisent un harness | Jupyter (Anaconda) |

## Sécurité

- Les élèves ne donnent jamais à une IA leur nom de famille, leur adresse, une photo ou une clé API.
- Les chatbots grand public demandent 13 ans minimum : les élèves utilisent **le chat du club**, et l'animateur montre les autres IA en démonstration.
- Révoquer les clés API à la fin de l'année.
