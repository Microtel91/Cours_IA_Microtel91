# S02 — L'armure du cerveau : le harness

> **Grande idée** : l'intelligence ne vient pas que du modèle. **Agent = Modèle + Harness.**
> Le harness, c'est tout ce qu'on met *autour* du cerveau : une boucle, des outils, du contexte, des règles, un arrêt.
> 2026 est l'année des harness : Claude Code, Codex, opencode, OpenClaw… ce sont des harness.

**Matériel** : [slides](../ressources/slides/modele_et_harness.html) (partie 2), [demo/harness_refuge.py](../ressources/demo/harness_refuge.py) prêt sur le PC
animateur (clé API testée la veille !), `refuge.csv` imprimé en 3 exemplaires, cartes vertes/orange/rouges, un minuteur.

## Objectifs

- Connaître les **5 pièces** du harness : boucle, outils, contexte, permissions, arrêt.
- Comprendre que le modèle **demande** et que le harness **exécute**.
- Constater que le même modèle donne des résultats différents selon son harness.

## Déroulé (2 h)

| Durée | Activité |
|---|---|
| 10 min | Réponse au suspense de S01 : la date |
| 40 min | Jeu de rôle : le cerveau dans le bocal (3 manches) |
| 15 min | Les 5 pièces du harness (slides) |
| 5 min | Pause |
| 20 min | Démo : la même chose dans la machine |
| 15 min | Carnet de bord |
| 15 min | Tour des apprentissages |

### Le suspense de S01 (10 min)

« Comment le modèle connaît-il la date ? » → Le chatbot n'est pas *que* le modèle. Avant votre question, le programme
autour du modèle a écrit en cachette : « Nous sommes le 14 octobre 2026. Tu es un assistant gentil… ».
Ce programme autour, c'est le **harness** (en français : le *harnais*, l'équipement).
Le modèle ne connaît pas la date : il **lit** la date qu'on lui a donnée.

### Jeu de rôle — Le cerveau dans le bocal (40 min)

**Rôles** (renouveler les volontaires à chaque manche) :

- **Le Cerveau** (le modèle) : assis dos au groupe, il ne voit rien. Il ne peut **qu'écrire** sur des papiers.
  Pour agir, il écrit une **demande** : `OUTIL : lire la ligne 3 du fichier refuge.csv`.
- **Le Harness** : seul à avoir le fichier `refuge.csv` imprimé, une calculatrice et les cartes de couleur.
  Il porte les papiers, exécute les demandes autorisées et rapporte le résultat **par écrit**.
- **L'Humain** : pose la question au Cerveau.
- **Le reste de la classe** : observe et note chaque aller-retour au tableau (c'est la **trace**).

**Question** : « Combien de chats du refuge attendent encore d'être adoptés, et comment s'appelle le plus âgé ? »

**Manche 1 — Le cerveau seul.** Le Cerveau n'a pas le droit aux outils. Il doit répondre directement.
→ Il invente ou dit « je ne sais pas ». *C'est le modèle seul.*

**Manche 2 — Avec un outil et une boucle.** Le Cerveau peut faire des demandes, mais **personne ne lui dit comment
s'appelle le fichier ni ce qu'il contient**. Il doit deviner : « OUTIL : ouvre le fichier chats.txt » → le Harness
répond « Erreur : ce fichier n'existe pas ». Il recommence, recommence… Minuteur 5 minutes.
→ Ça peut marcher, mais c'est long : c'est la **boucle** (essayer → regarder le résultat → recommencer).

**Manche 3 — Avec du contexte et des règles.** Avant la question, le Harness donne au Cerveau une fiche :
« Le fichier s'appelle refuge.csv. Colonnes : nom, espece, age_ans, poids_kg, arrivee, adopte, caractere. »
→ En 2-3 demandes, le Cerveau trouve. C'est le **contexte**.

**Bonus permissions** : l'animateur souffle au Cerveau d'écrire « OUTIL : jeter le fichier à la poubelle ».
Le Harness lève la **carte rouge** : interdit. Puis « OUTIL : envoyer le fichier à tout le monde » → **carte orange** :
on demande à l'Humain. Ce sont les **permissions** (feu vert / orange / rouge).

**Bonus arrêt** : quand le minuteur sonne ou quand le Cerveau écrit sa réponse finale, c'est fini : c'est l'**arrêt**.

> ⚠️ **Le piège du fichier** : Gribouille (13 ans) est le plus vieux chat… mais il est **déjà adopté**.
> La bonne réponse est **7 chats, le plus âgé est Noisette (11 ans)**. Si un groupe répond Gribouille : parfait,
> c'est le meilleur moment pour parler du **Vérificateur**.

### Les 5 pièces (15 min, slides)

Relire la trace du tableau et colorier chaque aller-retour avec la couleur de sa pièce :
🔁 Boucle · 🛠️ Outils · 📖 Contexte · 🚦 Permissions · 🛑 Arrêt.

Phrase à faire répéter : **« Le modèle ne lance jamais rien lui-même : il demande, le harness décide et exécute. »**

### Démo machine (20 min)

```
python harness_refuge.py --niveau 0
python harness_refuge.py --niveau 1
python harness_refuge.py --niveau 2
python harness_refuge.py --niveau 2 --demander
```

Avant chaque niveau : **« Que va-t-il se passer ? »** (prédire, puis observer).
Faire remarquer que les lignes affichées sont exactement les manches du jeu : la demande du modèle, le résultat du harness, la réponse.

Pour aller plus loin (si le temps) : `--modele mistral-large-latest` (gros modèle) vs `--modele ministral-3b-latest`
(petit modèle) avec le même harness. **Même harness + modèle différent = résultat différent aussi.**
Avec un petit modèle, il arrive qu'il réponde « Gribouille » : il a oublié de filtrer les chats adoptés.

Version locale, sans internet (Ollama sur le PC animateur) : `python harness_refuge.py --local --modele qwen3.5:2b`
— beaucoup plus lent, on voit l'IA « réfléchir ». Bon moment pour dire : un modèle local est privé, gratuit, mais plus petit.

### Le monde réel (2 min, slides)

Le Chat, ChatGPT, Claude… ne sont pas des modèles : ce sont des harness autour d'un modèle (recherche web,
mémoire, exécution de code, création d'images). Les **agents de code** de 2026 (Claude Code, Codex, opencode)
sont des harness qui donnent au modèle des outils pour lire, écrire et tester des programmes. Sur un même test,
un même modèle a obtenu **76 %** dans un harness et **58 %** dans un autre.

## Trace écrite

> **Agent = Modèle + Harness.**
> Le harness, c'est l'équipement autour du modèle : une **boucle**, des **outils**, du **contexte**, des **permissions**, un **arrêt**.
> Le modèle demande, le harness décide et exécute.
