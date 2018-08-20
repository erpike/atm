from .base import *

try:
    from .local import *
    live = True
except:
    live = True

if live:
    from .production import *