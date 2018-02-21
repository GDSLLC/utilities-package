import sys
if sys.version_info.major < 3:
    sys.exit('Python 3 required but lower version found. Aborted.')

from utilities.api import api_is_up
from utilities.services import service_is_up

if api_is_up():
    print("api looks good")
else:
    print("api looks bad")

if service_is_up(5514):
    print("service looks good")
else:
    print("service looks bad")
