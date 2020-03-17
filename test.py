# git init : initialise le dossier courant comme repository git

# git add nomfichier : ajoute un fichier à l'index du repository
# git add . : ajoute tous les fichiers du dossier courant à l index

# git commit -m "message": enregistre les modifs du repository et ajoute un message

# git log : affiche l'historique des commit, ligne du haut : dernier commit réalisé, ligne du bas : 1er commit
# infos visibles du log : SHA : id unique du commit / auteur / date du commit / message
# la touche q permet de quitter le log

# git commit -a -m "message" : met a jour tous les fichiers existants préalablement ajoutés à l'index

# git checkout SHAducommit : permet de se repositionner sur le commit choisi
# git checkout master : repositionne au commit principal (le plus récent)

# git revert SHAducommit : créé un nouveau commit qui annule les mises à jour du commit précedent

# git commit --ammend -m "message" : remplace le message du dernier commit