"""Snap"""

import os
from snapinit import SnapInit
from snapbranch import Branch


class SnapGit:
    """SnapGit"""

    def __init__(self):
        self.branch: str = self.get_branch()
        self.branches: list[Branch] = self.load_branches()

    def init(self, description):
        """add"""
        snapinit = SnapInit()
        snapinit.init(description)
        self.branches.append(Branch("main"))
        self.checkout("main")

    def get_branch(self):
        """add"""
        branch = ""
        try:
            with open(os.path.join(".snap", "head"), "r", encoding="utf-8") as f:
                branch = f.read()
        except OSError:
            pass
        return branch

    def load_branches(self):
        """add"""
        branches: list[Branch] = []

        for _, _, files in os.walk(os.path.join(".", ".snap", "branch"), topdown=True):
            for file in files:
                print(file)
                branches.append(Branch(file))

        return branches

    def checkout(self, branch):
        """add"""
        try:
            with open(os.path.join(".snap", "head"), "w", encoding="utf-8") as f:
                f.write(branch)
        except OSError:
            pass

    def add(self, files):
        """add"""
        for branch in self.branches:
            if branch.name == self.branch:
                branch.add_index(files)

    def commit(self, message=""):
        """add"""
        for branch in self.branches:
            if branch.name == self.branch:
                branch.commit_branch(message)

    def revert(self, hash_digest):
        """add"""
        for branch in self.branches:
            if branch.name == self.branch:
                branch.revert_branch(hash_digest)


if __name__ == "__main__":
    import sys

    snap = SnapGit()
    command = sys.argv[1]

    if command == "init":
        snap.init("SnapGit")
    elif command == "add":
        snap.add(sys.argv[2:])
    elif command == "commit":
        snap.commit(sys.argv[2])
    elif command == "revert":
        snap.revert(sys.argv[2])
    else:
        print("Unknow Command")
