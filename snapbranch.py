"""Branches"""

import time


class Branch:
    """Branch"""

    def __init__(self, name="", owner=""):
        self.name: str = name
        self.owner: str = owner
        self.created: str = time.ctime(time.time())
        self.last_edited: str = time.ctime(time.time())
        self.last_commit: str = time.ctime(time.time())
        self.commits: list[str] = []

    def rename_branch(self, name):
        """add"""
        self.last_edited = time.ctime(time.time())
        self.name = name

    def load_commits(self):
        """add"""
        commits: list[str] = []
        with open(f".snap/branch/{self.name}", "r", encoding="utf-8") as f:
            try:
                commits = f.readlines()
            except EOFError:
                return commits
        return commits

    def add_commit(self, commit_hash):
        """add"""
        self.last_edited = time.ctime(time.time())

        if commit_hash not in self.commits:
            self.commits.append(commit_hash)

        with open(f".snap/branch/{self.name}", "w", encoding="utf-8") as f:
            try:
                f.writelines(self.commits)
            except EOFError:
                pass

    def remove_commit(self, commit_hash):
        """remove_commit"""

        self.last_edited = time.ctime(time.time())

        for commit in self.commits:
            if commit == commit_hash:
                self.commits.remove(commit_hash)

        with open(f".snap/branch/{self.name}", "w", encoding="utf-8") as f:
            try:
                f.writelines(self.commits)
            except EOFError:
                pass
