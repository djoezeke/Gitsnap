"""Branches"""

import os
import time
import pickle
from snapgit.snapshot import SnapShot


class SnapBranch:
    """SnapBranch"""

    def __init__(self, name=""):
        self.name: str = name
        self.snapshot = SnapShot(self.name)

        if self.branch_exits():
            self.created: str = self.branch_info()[0]
            self.last_updated: str = self.branch_info()[1]
            self.commits: list[str] = self.load_commits()
        else:
            self.created: str = time.ctime(time.time())
            self.last_updated: str = time.ctime(time.time())
            self.branch_init()

    def branch_exits(self):
        """add"""
        return os.path.exists(os.path.join(".snap", "branch", self.name))

    def branch_init(self):
        """add"""
        with open(f".snap/branch/{self.name}", "w", encoding="utf-8") as f:
            f.writelines([self.created, "\n", self.last_updated, "\n"])

        index: dict[str, list[str]] = {}

        with open(".snap/index", "rb") as f:
            try:
                index = pickle.load(f)
            except EOFError:
                return

        index[self.name] = []

        with open(".snap/index", "wb") as f:
            pickle.dump(index, f)

    def branch_info(self):
        """add"""

        created_updated: list = []

        with open(f".snap/branch/{self.name}", "r", encoding="utf-8") as f:
            info = f.readlines()
            created_updated = info[:2]

        return created_updated

    def load_commits(self):
        """add"""

        commits: list[str] = []
        with open(f".snap/branch/{self.name}", "r+", encoding="utf-8") as f:
            branch_commits = f.readlines()
            commits = branch_commits[2:]

        return commits

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
        self.last_updated = time.ctime(time.time())
        self.name = name

    def add_commit(self, commit_hash):
        """add"""

        self.last_updated = time.ctime(time.time())

        if commit_hash not in self.commits:
            self.commits.append(commit_hash)

        with open(f".snap/branch/{self.name}", "w", encoding="utf-8") as f:
            try:
                f.writelines(
                    list(
                        [
                            self.created,
                            self.last_updated,
                            "\n",
                            *["\n" for commit in self.commits],
                        ]
                    )
                )
            except EOFError:
                pass

    def remove_commit(self, commit_hash):
        """remove_commit"""

        self.last_updated = time.ctime(time.time())

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
