# ---------------------------------------------------------------------------
# File:   library.py
# Author: (c) 2024 Jens Kallup - paule32
#
# All rights reserved
# ---------------------------------------------------------------------------
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_directory, "../src/")

if module_path not in sys.path:
    sys.path.append(module_path)

#import TObject
from TObject      import *
from TApplication import *
from TMenuBar     import *
from TStatusBar   import *
