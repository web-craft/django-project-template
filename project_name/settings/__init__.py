from .base import *
try:
    from .local import *
except ImportError, e:
    e.args = tuple(['%s (did you copy settings/local.py.template to settings/local.py?)' % e.args[0]])
    raise e