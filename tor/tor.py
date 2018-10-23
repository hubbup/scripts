import sys
import os

mag = sys.argv[1]
command = 'transmission-cli -u 0 -w ~/Downloads ' + mag# + ' > tor.log'
print (command)
os.system (command)
