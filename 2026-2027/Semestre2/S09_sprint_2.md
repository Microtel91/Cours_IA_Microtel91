# S09 — Sprint 2 · Capsule : l'IA peut se tromper

Format : [sprint](../Semestre1/S06_sprint_1.md). Seule la capsule change.

## Capsule (20 min) — Rester le chef

> **Grande idée** : une IA peut se tromper (hallucinations), avoir des **biais** (reproduire des clichés de ses données),
> et fabriquer des images ou des voix **truquées**. C'est à l'humain de vérifier.

1. **Le piège de Gribouille** (5 min) — rejouer `python harness_refuge.py --niveau 2 --modele ministral-3b-latest`
   (ou `--local --modele qwen3.5:2b`). Le petit modèle répond souvent « Gribouille »… qui est déjà adopté.
   La réponse a l'air sûre d'elle et elle est fausse. Comment le Vérificateur aurait-il pu le voir ? (relire la question, ouvrir le fichier, demander à une autre IA)
2. **Le biais** (7 min) — générer « un scientifique », « une personne qui fait le ménage », « un chef d'entreprise » en images.
   Que remarque-t-on ? D'où ça vient ? (des images qu'elle a vues). Que peut-on faire ? (le préciser dans la demande, en parler)
3. **Vrai ou truqué ?** (8 min) — 6 images projetées, dont 3 générées par IA. Vote à main levée. Indices : mains, textes, reflets, ombres…
   Mais attention : les IA de 2026 font presque parfait → **la vraie défense, c'est de vérifier la source**.

Les 3 réflexes du Vérificateur (à ajouter au carnet) :
- **Relire** : la réponse répond-elle vraiment à ma question ?
- **Recouper** : une autre source (livre, site sérieux, adulte, autre IA) dit-elle la même chose ?
- **Tester** : si c'est du code, je le lance ; si c'est un calcul, je le refais.

## Atelier

Objectif du jour de la feuille de route. **Mission bonus** : chaque groupe doit documenter **au moins une erreur d'IA**
dans la liste des pièges (ce que l'IA a dit, pourquoi c'était faux, comment on l'a vu) → badge *Vérificateur*.
