# S02 — Le harness : l'armure du cerveau

**À retenir** : *Agent = Modèle + Harness.* Le modèle **demande**, le harness **exécute**.
Le harness, ce sont 5 pièces : 🔁 boucle · 🛠️ outils · 📖 contexte · 🚦 permissions · 🛑 arrêt.

**Préparer** : le [labo](../ressources/supports/labo_ia.html) (onglet 2), les slides, et `refuge.csv` ouvert sur un PC.

## Déroulé

1. **Réponse au suspense** (10 min, slide 12) : avant ta question, le chatbot écrit en cachette « Nous sommes le … ».
   Le modèle ne connaît pas la date : il la **lit**. Ce programme autour du modèle, c'est le **harness**.
2. **Le jeu du cerveau dans le bocal** (25 min) :
   - un élève est le **Cerveau** : il est dos à l'écran et ne peut qu'écrire des demandes (« Lis-moi la ligne 3 ») ;
   - un autre est le **Harness** : il est devant le PC où `refuge.csv` est ouvert, et répond par écrit ;
   - question : *« Combien de chats attendent d'être adoptés, et comment s'appelle le plus âgé ? »*
   - manche 1 sans rien, manche 2 avec le droit de demander, manche 3 en donnant d'abord le nom du fichier et ses colonnes.
3. **Le labo, onglet 2 « Le cerveau dans le bocal »** (30 min). Les élèves viennent à tour de rôle allumer des pièces. Avant chaque lancement, ils prédisent ce qui va se passer :
   - tout éteint → il invente, ou il avoue ne pas savoir ;
   - + outil → il cherche le fichier au hasard : c'est la **boucle** ;
   - + contexte → il trouve tout de suite ;
   - petit modèle → il répond Gribouille… On clique sur « Vérifier dans le fichier » : Gribouille est déjà adopté !
   - + permission → c'est l'élève qui autorise ou refuse. Que fait le modèle si on refuse ?
   - arrêt à 2 étapes → il n'a pas le temps de finir.
4. **Slides 13 à 22** (10 min) : « Le Chat, ChatGPT, Claude Code… sont tous des harness autour d'un modèle. »

Variante en vrai : `python harness_refuge.py` ([démo](../ressources/demo/)) fait la même chose avec un vrai modèle.

## Pour finir

Chacun nomme une pièce du harness et dit ce qui se passe quand on l'enlève.
