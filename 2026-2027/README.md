# Cours IA — Microtel91 · 2026-2027

**Apprendre l'IA en parlant aux IA, en équipe, sur un projet qui compte pour le monde.**

Public : 10-12 ans, bases de Python déjà vues. Rythme : 2 h par semaine, 2 semestres × 7 séances.

## L'idée en 4 phrases

1. **Tronc commun** (séances 1 à 3) : on comprend ce qu'est un *modèle*, pourquoi
   l'intelligence ne vient pas que du modèle, et ce qu'est un *harness* (l'équipement autour du modèle).
2. **Ikigai** (séance 4) : chacun cherche ce qu'il aime, ce qu'il sait faire, ce dont le monde a besoin
   → les élèves choisissent un projet et leurs coéquipiers.
3. **Projet** (séances 5 à 14) : chaque groupe a un objectif, une feuille de route, et apprend
   **tout ce qui lui manque en le demandant à des IA**.
4. **Rituel à chaque séance** : on note ce qu'on a appris, on le dit à l'oral, on se fixe le prochain objectif.

Pourquoi ce format : en 2026, les meilleurs ingénieurs ne tapent presque plus de code eux-mêmes — ils
décrivent ce qu'ils veulent, pilotent des agents, et **vérifient**. Le savoir-faire qui compte devient :
savoir définir un objectif, savoir apprendre vite avec une IA, savoir juger si l'IA a raison, savoir
travailler en équipe et expliquer ce qu'on a fait.

## Contenu du dossier

| Dossier | Pour qui | Quoi |
|---|---|---|
| [programme.md](programme.md) | Animateur | Progression des 14 séances, déroulé type d'une séance, rituels |
| [Semestre1/](Semestre1/) · [Semestre2/](Semestre2/) | Animateur | Une fiche minutée par séance (S01 → S07, S08 → S14) |
| [slides/](ressources/slides/) | Projeté | Slides des séances 1-2 (modèle, harness) — ouvrir le `.html` dans un navigateur |
| [eleves/](ressources/eleves/) | Élèves (à imprimer) | Carnet de bord, Ikigai, feuille de route, cartes-questions, charte, fiche safari |
| [coach/](ressources/coach/) | IA | Le prompt « Coach de projet » à donner à l'IA des élèves |
| [demo/](ressources/demo/) | Animateur | `harness_refuge.py` : même modèle, 3 harness, 3 résultats |
| [outils/](ressources/outils/) | Élèves | `chat_du_club.py` : le chatbot du club (Streamlit + clé API de l'animateur) |
| [notebooks/](ressources/notebooks/) | Élèves (S08) | Construire son propre mini-harness, pas à pas |
| [animateur/](ressources/animateur/) | Animateur | Badges, grille d'observation, constitution des groupes, mot aux parents |

## Matériel

- PC du réseau de l'association avec **Anaconda** (Python, Jupyter, `requests` déjà inclus).
- Clés API Mistral créées par l'animateur pour la durée des séances (les révoquer après).
- Streamlit pour le chat du club : `pip install streamlit` si absent d'Anaconda.
- Optionnel : Ollama sur le PC de l'animateur pour montrer une IA locale (sans internet).

## ⚠️ Comptes et âge

La plupart des chatbots grand public exigent **13 ans minimum** (avec accord parental) dans leurs
conditions d'utilisation. Pour des 10-12 ans, la voie propre est :

- l'IA principale des élèves = **le chat du club** (`ressources/outils/chat_du_club.py`), qui passe par les clés API
  de l'animateur — c'est lui le titulaire du compte, et c'est un harness qu'il contrôle (consignes adaptées
  aux enfants, choix du modèle) ;
- les chatbots publics (Le Chat, ChatGPT, Gemini…) **en démonstration projetée** ou avec le compte de
  l'animateur lors du « safari des IA » (S03) ;
- un mot aux parents en début d'année : [animateur/mot_aux_parents.md](ressources/animateur/mot_aux_parents.md).

## Édition précédente

L'édition 2025-2026 (« Cours Chatbot » : Python → LangChain → Streamlit) est dans
[../2025-2026/Semestre2/](../2025-2026/Semestre2/).
