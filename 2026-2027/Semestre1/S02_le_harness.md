# S02 — Le harness : l'armure du cerveau

**À retenir** : *Agent = Modèle + Harness.* Le modèle **demande**, le harness **exécute**.
Le harness, ce sont 5 pièces : 🔁 boucle · 🛠️ outils · 📖 contexte · 🚦 permissions · 🛑 arrêt.

**Préparer** : les slides, la [démo du refuge](../ressources/demo/) testée la veille, `refuge.csv` ouvert sur un PC.

## Déroulé

1. **Réponse au suspense** (10 min, slide 12) : avant ta question, le chatbot écrit en cachette
   « Nous sommes le … ». Le modèle ne connaît pas la date : il la **lit**. Ce programme autour du modèle, c'est le **harness**.
2. **Le jeu du cerveau dans le bocal** (35 min) :
   - le **Cerveau** est assis dos à l'écran : il ne voit rien et ne peut qu'**écrire des demandes** (« Lis-moi la ligne 3 du fichier ») ;
   - le **Harness** est devant le PC où `refuge.csv` est ouvert : il exécute les demandes et répond **par écrit** ;
   - la classe note chaque aller-retour au tableau.

   Question : *« Combien de chats attendent d'être adoptés, et comment s'appelle le plus âgé ? »*
   - **Manche 1** : le Cerveau n'a droit à rien. Il devine.
   - **Manche 2** : il peut demander, mais il ne connaît pas le nom du fichier. C'est long : c'est la **boucle**.
   - **Manche 3** : on lui donne d'abord le nom du fichier et ses colonnes (c'est le **contexte**). Il trouve vite.
   - Bonus : « Supprime le fichier ! » → le Harness refuse : ce sont les **permissions**.

   Réponse : **7 chats, le plus âgé est Noisette**. Piège : Gribouille est plus vieux… mais il est déjà adopté !
3. **La démo** (15 min) : `python harness_refuge.py`. On retrouve les 3 manches dans l'ordinateur.
   Avant chaque niveau : « Qu'est-ce qui va se passer ? »
4. **Slides 13 à 22** (15 min) : les 5 pièces. « Le Chat, ChatGPT, Claude Code… sont tous des harness autour d'un modèle. »

## Pour finir

Chacun nomme une pièce du harness et donne un exemple vu aujourd'hui.
