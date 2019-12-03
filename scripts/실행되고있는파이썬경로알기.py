import inspect
import os

script_relpath = inspect.getfile(inspect.currentframe())
script_abspath = os.path.abspath(script_abspath)