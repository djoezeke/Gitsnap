"""Branches"""

import os
import time
from snapshot import SnapShot


class Branch:
    """Branch"""

    def __init__(self, name=""):
        self.name: str = name
        self.snapshot = SnapShot(self.name)
        self.created: str = time.ctime(time.time())
        self.last_edited: str = time.ctime(time.time())
        self.last_commit: str = time.ctime(time.time())
        self.commits: list[str] = []
        self.branch_init()

    def branch_init(self):
        """add"""
        with open(f".snap/branch/{self.name}", "w", encoding="utf-8") as f:
            f.write("")

    def commit_branch(self, message):
        """add"""
        hash_digest = self.snapshot.commit(message)

        if hash_digest is not None:
            self.add_commit(hash_digest)

    def revert_branch(self, hash_str):
        """add"""
        self.snapshot.revert(hash_str)

    def add_index(self, files: list[str]):
        """add"""
        self.snapshot.add(files)

    def remove_index(self, files: list[str]):
        """add"""
        self.snapshot.remove(files)

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

        for root, _, files in os.walk(os.path.join(".snap", "hook")):

            for file in files:
                if file == commit_hash:
                    os.remove(os.path.join(root, file))
