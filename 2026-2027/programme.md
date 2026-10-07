# Programme 2026-2027

## Vue d'ensemble

| # | Séance | Grande idée | Ce que les élèves repartent avec |
|---|---|---|---|
| **Semestre 1 — Comprendre, choisir, démarrer** ||||
| S01 | [Le cerveau dans le bocal](Semestre1/S01_le_modele.md) | Un **modèle** ne fait qu'une chose : lire du texte et écrire la suite. | Leur carnet de bord, 1re trace écrite |
| S02 | [L'armure du cerveau](Semestre1/S02_le_harness.md) | L'intelligence ne vient pas que du modèle : **Agent = Modèle + Harness**. | Les 5 pièces du harness |
| S03 | [Le safari des IA](Semestre1/S03_safari_des_ia.md) | Il existe plein d'IA différentes, chacune avec ses forces, limites et contraintes. Apprendre **avec** une IA, et la **vérifier**. | Fiche safari, cartes-questions, charte |
| S04 | [Mon Ikigai, notre projet](Semestre1/S04_ikigai_et_groupes.md) | Un bon projet = ce que j'aime + ce que je sais (ou veux savoir) faire + ce dont le monde a besoin. | Ikigai perso, groupes formés, idée de projet |
| S05 | [Objectif et feuille de route](Semestre1/S05_feuille_de_route.md) | Un objectif clair, des étapes, des rôles. L'IA peut être notre coach. | Feuille de route du groupe |
| S06 | [Premier sprint](Semestre1/S06_sprint_1.md) | Apprendre juste ce qu'il faut, quand il le faut. | 1re brique du projet |
| S07 | [Démo de mi-parcours](Semestre1/S07_demo_mi_parcours.md) | Montrer tôt, écouter les retours, ajuster. | Prototype montré, feuille de route v2 |
| **Semestre 2 — Construire, tester, montrer** ||||
| S08 | [Je construis mon harness](Semestre2/S08_mon_harness.md) | On passe de l'autre côté : on **construit** l'équipement d'une IA. | Un mini-harness Python qui marche |
| S09 | [Sprint 2 — L'IA peut se tromper](Semestre2/S09_sprint_2.md) | Hallucinations, biais, images truquées : rester le chef. | 2e brique + 1 erreur d'IA documentée |
| S10 | [Sprint 3 — Tester avec de vrais gens](Semestre2/S10_sprint_3.md) | Ce dont le monde a besoin, on le vérifie en demandant au monde. | Retours d'au moins 2 testeurs |
| S11 | [Sprint 4 — Les agents qui agissent](Semestre2/S11_sprint_4.md) | Démo d'un agent de code : il lit, écrit, teste, tout seul… dans un harness. | Projet presque fini |
| S12 | [Sprint 5 — Finitions](Semestre2/S12_sprint_5.md) | Finir, c'est un métier. | Version finale |
| S13 | [Raconter son projet](Semestre2/S13_preparer_la_presentation.md) | Une bonne présentation raconte une histoire. | Présentation répétée |
| S14 | [Le grand jour](Semestre2/S14_presentation_finale.md) | On montre, on célèbre, on fait le bilan. | Badges, bilan du carnet |

Le calendrier est indicatif : si le semestre compte plus de séances, ajouter des sprints (le format
d'un sprint est le même partout, voir S06). S'il en compte moins, fusionner S12 et S13.

## Le fil rouge : Agent = Modèle + Harness

Vocabulaire commun à toute l'année (affiché en salle, couleurs identiques sur les slides) :

| Pièce | Pour les élèves | Exemple |
|---|---|---|
| **Modèle** | Le cerveau. Il lit du texte, il écrit la suite. Il ne *fait* rien d'autre. | Mistral, Claude, GPT, Qwen… |
| 🔁 **Boucle** | Essayer → regarder le résultat → recommencer. | L'IA corrige son code après une erreur |
| 🛠️ **Outils** | Les mains : ce que l'IA peut faire grâce au harness. | Calculer, chercher sur le web, lire un fichier |
| 📖 **Contexte** | Ce que le cerveau a sous les yeux à chaque fois. | Les consignes, la conversation, les documents |
| 🚦 **Permissions** | Feu vert (le faire seul), orange (demander), rouge (interdit). | « Demande avant de supprimer un fichier » |
| 🛑 **Arrêt** | Quand est-ce qu'on s'arrête ? | Réponse trouvée, trop d'essais, l'humain dit stop |

Deux phrases à faire répéter toute l'année :

- « Le modèle ne lance jamais rien lui-même : il **demande**, le harness **décide** et **exécute**. »
- « Même modèle + harness différent = résultat différent. » (Sur un même test d'agents de code,
  Terminal-Bench, un même modèle a obtenu 76 % dans un harness et 58 % dans un autre.)

## Déroulé type d'une séance projet (2 h)

| Durée | Moment | Détail |
|---|---|---|
| 10 min | **Météo & cap** | Chaque groupe relit à voix haute son objectif du jour (écrit à la séance précédente). |
| 15-20 min | **Capsule tronc commun** | Un concept court, démontré (voir la fiche de la séance). |
| 60 min | **Atelier projet** | Les groupes avancent et apprennent avec l'IA. L'animateur passe de groupe en groupe. |
| 15 min | **Carnet de bord** | Chacun note *seul* ce qu'il a appris, puis le groupe écrit son prochain objectif. |
| 15 min | **Le tour des apprentissages** | 2 min par groupe à l'oral (voir ci-dessous). |
| 5 min | Rangement | Clés API : on ferme le chat du club. |

### Le tour des apprentissages (oral, chaque séance)

Le **porte-parole** du jour (rôle tournant : tout le monde parle au moins une fois par mois) répond à :

1. **Ce qu'on a appris** aujourd'hui — expliqué comme à un plus petit.
2. **Comment** on l'a appris — quelle IA, quelle question a marché.
3. **Un piège** — une fois où l'IA s'est trompée ou nous a mal compris (et comment on l'a vu).
4. **Notre prochain objectif** — une phrase.

Le public pose **une** question. L'animateur relance avec : « Et ça, c'est quelle pièce du harness ? »

### Les rôles dans un groupe (tournants)

- **Capitaine** — garde l'objectif du jour en tête, coupe les discussions hors sujet.
- **Scribe** — tient la feuille de route du groupe à jour.
- **Vérificateur** — vérifie ce que dit l'IA (autre source, test, autre IA).
- **Porte-parole** — fait l'oral de fin de séance.

En groupe de 3, le Capitaine est aussi Scribe.

## Règles d'or (affichées en salle)

1. **L'IA est un coach, pas un copieur.** On lui demande d'*expliquer*, pas seulement de *faire*.
2. **Je vérifie.** Une réponse d'IA est une hypothèse, pas une vérité.
3. **Je comprends ce que je montre.** Si je ne peux pas l'expliquer, ce n'est pas encore fini.
4. **Je protège mes infos.** Ni nom de famille, ni adresse, ni photo de quelqu'un sans accord, ni clé API.
5. **Je note ce que j'apprends.** Chaque séance, dans mon carnet.

Version élève détaillée : [eleves/charte_ia.md](ressources/eleves/charte_ia.md).
