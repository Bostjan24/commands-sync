#!/usr/bin/python
import csv

movementShortcuts="/home/bostjan/Repos/shortcuts-sync/movementShortcuts.txt"
editingShortcuts="/home/bostjan/Repos/shortcuts-sync/editingShortcuts.txt"

ba="/home/bostjan/.bashrc.base"
ra="/home/bostjan/.config/ranger/rc.conf.base"

rang=""
bash=""

with open(ba, 'r') as ba:
    bash+=ba.read()
with open(ra, 'r') as ra:
    rang+=ra.read()

with open(movementShortcuts, 'r') as fold:
    rang+=("\n"+"###MOVEMENT###"+"\n")
    bash+=("###MOVEMENT###"+"\n")
    for line in csv.reader(fold, dialect="excel-tab"):
        #print(line[0])
        rang+=("map g"+line[0]+" cd "+line[1]+"\n")
        rang+=("map t"+line[0]+" tab_new "+line[1]+"\n")
        rang+=("map Y"+line[0]+" shell cp %s "+line[1]+"\n")
        rang+=("map y"+line[0]+" shell mv %s "+line[1]+"\n")
        bash+=("alias "+line[0]+"='cd  "+line[1]+" && ls -l'"+"\n")
    rang+="\n"
    bash+="\n"

with open(editingShortcuts, 'r') as conf:
    rang+=("###EDITING###"+"\n")
    bash+=("###EDITING###"+"\n")
    for line in csv.reader(conf, dialect="excel-tab"):
        rang+=("map "+line[0]+" shell emacs -nw "+line[1]+"\n")
        bash+=("alias "+line[0]+"='emacs -nw "+line[1]+"'"+"\n")

with open("/home/bostjan/.config/ranger/rc.conf", 'w') as orgrang:
    orgrang.write(rang)
with open("/home/bostjan/.bashrc", 'w') as orgbash:
    orgbash.write(bash)
