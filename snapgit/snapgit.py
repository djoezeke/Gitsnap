"""SnapGit Class"""

import os
from snapgit.snapbasic import SnapInit
from snapgit.snapbranch import SnapBranch


class SnapGit:
    """SnapGit"""

    def __init__(self):
        self.branch: str = self.get_branch()
        self.branches: list[SnapBranch] = self.load_branches()

    def init(self, description):
        """add"""
        snapinit = SnapInit()
        snapinit.init(description)
        self.branches.append(SnapBranch("main"))
        self.checkout("main")

    def new_branch(self, name):
        """add"""
        self.branches.append(SnapBranch(name))

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
        branches: list[SnapBranch] = []

        for _, _, files in os.walk(os.path.join(".", ".snap", "branch"), topdown=True):
            for file in files:
                branches.append(SnapBranch(file))

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
