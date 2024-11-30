# ---------------------------------------------------------------------------
# File:   example1.py
# Author: (c) 2024 Jens Kallup - paule32
#
# All rights reserved
# ---------------------------------------------------------------------------
from library import *

if __name__ == "__main__":
    app = TApplication.TApplication()
    try:
        print(f"ExeName: {app.ExeName}")
        app.run()
    finally:
        print("finally: app.free")
        app.Free()
