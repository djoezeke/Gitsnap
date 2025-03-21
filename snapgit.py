"""Snap"""

import os
import pickle
import hashlib

from initailize import SnapInit
from commit import SnapShot

from revert import revert_to_snap

# from commit import commit


if __name__ == "__main__":
    import sys

    command = sys.argv[1]
    snap = SnapInit()
    shot = SnapShot()

    if command == "init":
        snap.init()
    elif command == "add":
        shot.add(sys.argv[2:])
    elif command == "commit":
        shot.commit(sys.argv[2])
    elif command == "revert":
        revert_to_snap(sys.argv[2])
    else:
        print("Unknow Command")
