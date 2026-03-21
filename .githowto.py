https://git-scm.com/cheat-sheet


set git=C:\Users\kazarinovav\AppData\Local\GitHubDesktop\app-3.5.6\resources\app\git\cmd\git.exe


#######################################################
#######################################################
################### Forbid to track ###################
#######################################################
#######################################################
echo backup >> .gitignore
%git% rm --cached -r backup
%git% commit -m "Stop tracking backup"

echo session.xml >> .gitignore
%git% rm --cached session.xml
%git% commit -m "Stop tracking session.xml"

#######################################################
#######################################################
##################  Going back  #######################
#######################################################
#######################################################
%git% checkout 281fa33
