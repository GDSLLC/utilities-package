import sys
if sys.version_info.major < 3:
    sys.exit('Python 3 required but lower version found. Aborted.')

from termcolor import colored

def abort(message):
    sys.exit(colored(''.join(['ABORTED - ', message]), 'red', attrs=['bold']))
