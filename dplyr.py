# Usage:


import sys
import os
import logging
from subprocess import call

__CURPATH__   = os.path.abspath(os.getcwd()) + '/'
__DPLYRPATH__ = __CURPATH__ 				 + '.dplyr/'
__LOGPATH__   = __DPLYRPATH__ 				 + 'logs/'
__CFGPATH__   = __DPLYRPATH__ 				 + 'conf/'
__LOGFILE__   = __LOGPATH__					 +'/dyplr.log'
__ARGS__	  = []

for arg in sys.argv:
	if not arg == 'dplyr':
		__ARGS__.append(arg)

if len(__ARGS__) <= 0:
	print 'You must pass atleast one argument, please look in the documentation'
	exit()

class Dplyr:
	def __init__(self):
		self.data = []		
		logging.debug('dplyr was initialised with arguments: ' + ' ,'.join(__ARGS__))			
	def newProject(self, projectname):
		if not os.path.isdir(__DPLYRPATH__):
			os.mkdir(__DPLYRPATH__) 
			os.mkdir(__LOGPATH__)
			os.mkdir(__CFGPATH__)
			handler = open(__CFGPATH__ + 'default.cfg', "w")
			handler.close()
		logging.basicConfig(filename=__LOGFILE__, level=logging.DEBUG, format='%(asctime)s %(message)s')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

# Go power rangers!
dplyr = Dplyr();
if __ARGS__[0] == 'new':	
	if __ARGS__[1] != 'from':
		print bcolors.OKBLUE + "Dplyr creating new project..." + bcolors.ENDC
		call('git init', shell=True)
		call('git add ' + __ARGS__[1], shell=True)
		call('git commit -am "Initialised project using dplyr"', shell=True)
		print bcolors.OKGREEN + "Project successfully created!" + bcolors.ENDC
	elif __ARGS__[2] == 'existing':
		print "Creating new project from existing repository: " + __ARGS__[3]	
		call('git clone ' + __ARGS__[3], shell=True)
	dplyr.newProject(__ARGS__[1])	
if __ARGS__[0] == 'get':		
	print "Getting from: " + __ARGS__[1]
