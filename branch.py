"""Branches"""

import os
import time
import pickle


class Branch:
    "Branch"

    def __init__(self, name="", owner=""):
        self.name = name
        self.owner = owner
        self.created = time.ctime(time.time())
        self.last_edited = time.ctime(time.time())
        self.last_commit = time.ctime(time.time())
        self.commits = []

    def rename_branch(self, name):
        """add"""
        self.last_edited = time.ctime(time.time())
        self.name = name

    def load_commits(self):
        """add"""
        with open(".snap/index", "rb") as f:
            try:
                files = pickle.load(f)
            except EOFError:
                pass

        for file in files[self.name]:

            if not os.path.exists(file):
                return

    def add_commit(self, commit_hash):
        """add"""
        self.last_edited = time.ctime(time.time())
        self.commits.append(commit_hash)

    def remove_commit(self, commit_hash):
        """add"""
        self.last_edited = time.ctime(time.time())
        for commit in self.commits:
            if commit == commit_hash:
                self.commits.remove(commit_hash)
