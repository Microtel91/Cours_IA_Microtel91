# Semestre 1 — Comprendre, choisir, démarrer

Chaque séance suit les [3 temps](../README.md#une-séance--toujours-les-mêmes-3-temps). Ici : seulement ce qui change.

---

## S01 — Le cerveau dans le bocal

**À retenir** : un modèle devine la suite d'un texte. Quand il ne sait pas, il peut inventer (on dit qu'il **hallucine**).

1. **Jeu du mot suivant** : écrire au tableau « Le chat est monté sur le … ». Chacun écrit la suite sur un post-it.
   → « C'est ce que fait un modèle : il choisit la suite la plus probable. »
2. **Slides 1 à 10** ([slides](../ressources/slides/modele_et_harness.html)).
3. **Piéger le modèle** (chat du club, mode Libre) : « Qu'est-ce que j'ai mangé ce matin ? », « Raconte la vie de l'explorateur Bartholomé Pivoine ».
   Est-ce qu'il invente ?
4. **Suspense** : « Il connaît la date d'aujourd'hui… alors qu'il est dans un bocal. Comment ? Réponse la semaine prochaine. »

Distribuer le carnet et le mot aux parents.

## S02 — L'armure du cerveau (le harness)

**À retenir** : *Agent = Modèle + Harness.* Le modèle **demande**, le harness **exécute**.

1. **Réponse au suspense** : le chatbot écrit la date dans les consignes, en cachette (slide 12).
2. **Jeu de rôle** : un élève est le **Cerveau** (dos à la classe, il ne peut qu'écrire des demandes sur papier),
   un autre est le **Harness** (il a le fichier `refuge.csv` imprimé et répond par écrit).
   Question : « Combien de chats attendent d'être adoptés, et comment s'appelle le plus âgé ? »
   - Manche 1 : sans rien → le Cerveau devine.
   - Manche 2 : on lui dit le nom du fichier et ses colonnes → il trouve.
   - Réponse : **7 chats, Noisette**. (Piège : Gribouille est plus vieux… mais il est déjà adopté !)
3. **Démo** : `python harness_refuge.py` → la même chose dans l'ordinateur.
4. **Slides 11 à 22** : les 5 pièces (boucle, outils, contexte, permissions, arrêt).

## S03 — Apprendre avec une IA

**À retenir** : on demande à l'IA de nous **expliquer**, pas de faire à notre place. Et on **vérifie**.

1. **Démo projetée**, deux façons de demander :
   - ❌ « Fais-moi un jeu du pendu en Python. »
   - ✅ « J'ai 11 ans, je veux *apprendre* à faire un pendu. Explique-moi la première étape seulement. »
2. **Tour des IA** (projeté, 20 min) : un chatbot avec internet ou sans, une IA qui dessine, une IA locale (Ollama).
   Pour chacune : « Qu'est-ce qu'elle sait faire ? Qu'est-ce qu'elle rate ? »
3. Chacun choisit un sujet qui l'intéresse et l'apprend avec le chat du club, en utilisant le [mémo](../ressources/a_imprimer/memo_ia.md).
   Le voisin vérifie qu'il sait le réexpliquer.

## S04 — Mon Ikigai, notre projet

**À retenir** : un bon projet = ce que j'aime + ce que je sais (ou veux savoir) faire + ce dont le monde a besoin.

1. Chacun remplit la partie Ikigai de la fiche [Notre projet](../ressources/a_imprimer/projet.md), **sans IA** d'abord.
2. Puis il demande des idées au chat du club, et garde son idée préférée.
3. **Affichage des idées** : chacun écrit la sienne en une phrase sur une grande feuille. Chacun met 3 gommettes sur les idées des autres.
4. **Les groupes** : chaque élève écrit 3 vœux de projet et 1 prénom. L'animateur forme des équipes de 3-4, sans laisser personne seul.

Idées si ça bloque : un jeu sur le tri des déchets, un site pour un refuge, un chatbot de révision des tables,
une BD contre le harcèlement, un quiz vrai/faux sur les fausses infos.

## S05 — Notre objectif et nos étapes

**À retenir** : un bon objectif, on peut le **montrer** et on sait quand il est **fini**.

1. Chaque équipe écrit sa mission : « Nous voulons aider ___ à ___ grâce à ___. »
2. Elle dessine ce qu'elle montrera à la fin.
3. Avec le chat du club : « Découpe notre projet en 5 étapes, une par séance. » L'équipe garde ce qui lui plaît.
4. L'animateur valide : **la première étape doit pouvoir être finie en une séance**.

## S06 — On démarre !

**À retenir** : on apprend ce qu'il faut, quand il le faut. J'essaie → je regarde → je redemande.

Notion (10 min) : montrer comment coller une vraie erreur dans le chat et demander « Explique-moi pourquoi » avant de corriger.
Puis travail sur l'étape 1.

## S07 — On montre ce qu'on a

Chaque équipe montre son projet en 5 minutes : la mission, ce qui marche déjà, ce qu'elle a appris.
Le public dit **une chose réussie** et **une idée**. Les équipes ajustent ensuite leurs étapes pour le semestre 2.
