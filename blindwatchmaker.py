import string
import os
import sys
import random
import time

CharList = string.ascii_lowercase + string.ascii_uppercase + string.digits + '|()_`.-,;*.+/    \\\''
target = ['              (()          ',
'              ())          ',
'              (()          ',
'              ())          ',
'              (()          ',
'              ())          ',
'              (()          ',
'              ())          ',
'              (()          ',
'              .+.          ',
'          _.-//_\\\\-._      ',
'        .\'.-\' XII \'-.\'.    ',
'      /`.\'*         *\'.`\\  ',
'     / /*        /    *\\ \\ ',
'    | ;        _/       ; |',
'    | |IX     (_)    III| |',
'    | ;         \\       ; |',
'     \\ \\*        \\    */ / ',
'      \\ \'.*       \\ *.\'./  ',
'       \'._\'-.__VI_.-\'_.\'   ',
'          \'-.,___,.-\'      ']
generation =[ ''.join(random.choice(CharList) for i in range(27)) for j in range(21)]
nxgen = ''
completed = False

while completed == False:
	os.system('clear')
	for x in generation:
		print(x)
	completed = True
	for i in range(21):
		nxgen = ''
		for j in range(27):
			if generation[i][j] != target[i][j]:
				completed = False
				nxgen += random.choice(CharList)
			else:
				nxgen += target[i][j]
		generation[i] = nxgen
	time.sleep(0.1)

