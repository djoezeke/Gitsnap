"""Snap"""

from initailize import SnapInit
from commit import SnapShot
from revert import revert
from branch import Branch


class SnapGit:
    """SnapGit"""

    def __init__(self):
        self.branches: list[Branch] = []

    def add(self):
        """add"""


if __name__ == "__main__":
    import sys

    command = sys.argv[1]
    snap = SnapInit()
    shot = SnapShot()

    if command == "init":
        snap.init("SnapGit")
    elif command == "add":
        shot.add(sys.argv[2:])
    elif command == "commit":
        shot.commit(sys.argv[2])
    elif command == "revert":
        revert(sys.argv[2])
    else:
        print("Unknow Command")
