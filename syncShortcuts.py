#!/usr/bin/python
import csv

movementShortcuts="/home/bostjan/Dropbox/Computing/Linux/Shortcuts/movementShortcuts.txt"
editingShortcuts="/home/bostjan/Dropbox/Computing/Linux/Shortcuts/editingShortcuts.txt"
i3keys="/home/bostjan/Dropbox/Computing/Linux/Shortcuts/i3keys.txt"
i3autoStart="/home/bostjan/Dropbox/Computing/Linux/Shortcuts/i3autoStart.txt"
i3execAlways="/home/bostjan/Dropbox/Computing/Linux/Shortcuts/i3execAlways.txt"

ba="/home/bostjan/.bashrc.base"
ra="/home/bostjan/.config/ranger/rc.conf.base"
i3="/home/bostjan/.config/i3/config.base"

rang=""
bash=""
i3c=""

with open(ba, 'r') as ba:
    bash+=ba.read()
with open(ra, 'r') as ra:
    rang+=ra.read()
with open(i3, 'r') as i3:
    i3c+=i3.read()

with open(movementShortcuts, 'r') as fold:
    rang+=("\n"+"###MOVEMENT###"+"\n")
    bash+=("###MOVEMENT###"+"\n")
    for line in csv.reader(fold, dialect="excel-tab"):
        #print(line[0])
        rang+=("map g"+line[0]+" cd "+line[1]+"\n")
        rang+=("map t"+line[0]+" tab_new "+line[1]+"\n")
        rang+=("map Y"+line[0]+" shell cp %s "+line[1]+"\n")
        rang+=("map m"+line[0]+" shell mv %s "+line[1]+"\n")
        bash+=("alias g"+line[0]+"='cd  "+line[1]+" && ls -a'"+"\n")
    rang+="\n"
    bash+="\n"

with open(editingShortcuts, 'r') as conf:
    rang+=("###EDITING###"+"\n")
    bash+=("###EDITING###"+"\n")
    for line in csv.reader(conf, dialect="excel-tab"):
        rang+=("map "+line[0]+" shell emacs -nw "+line[1]+"\n")
        bash+=("alias "+line[0]+"='emacs -nw "+line[1]+"'"+"\n")

with open(i3keys, 'r') as keys:
    i3c+=("\n"+"# Custom keybindings"+"\n")
    for line in csv.reader(keys, dialect="excel-tab"):
        i3c+=("bindsym $mod+"+line[0]+" exec --no-startup-id "+line[1]+"\n")
    i3c+="\n"

with open(i3autoStart, 'r') as i3AS:
    i3c+=("# Auto start programs"+"\n")
    for line in csv.reader(i3AS, dialect="excel-tab"):
        i3c+=("exec --no-startup-id "+line[0]+"\n")
    i3c+="\n"

with open(i3execAlways, 'r') as i3ea:
    i3c+=("# Programs ran when i3 restarted"+"\n")
    for line in csv.reader(i3ea, dialect="excel-tab"):
        i3c+=("exec_always --no-startup-id "+line[0]+"\n")

with open("/home/bostjan/.config/ranger/rc.conf", 'w') as orgrang:
    orgrang.write(rang)
with open("/home/bostjan/.bashrc", 'w') as orgbash:
    orgbash.write(bash)
with open("/home/bostjan/.config/i3/config", 'w') as i3con:
    i3con.write(i3c)
