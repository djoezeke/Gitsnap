"""INit"""

import os

class SnapInit:
    "SnapInit"

    def __init__(self):
        pass

    def make_snap_folder(self):
        """make_folder"""
        os.makedirs(".snap", exist_ok=True)

    def make_info_folder(self):
        """make_folder"""
        os.makedirs(".snap/info", exist_ok=True)

    def make_hook_folder(self):
        """make_folder"""
        os.makedirs(".snap/hook", exist_ok=True)

    def make_branch_folder(self):
        """make_folder"""
        os.makedirs(".snap/branch", exist_ok=True)

    def create_config_file(self):
        """make_folder"""
        with open(".snap/config", "w", encoding="utf-8") as f:
            f.write("")

    def create_head_file(self):
        """make_folder"""
        with open(".snap/head", "w", encoding="utf-8") as f:
            f.write("")

    def create_index_file(self):
        """make_folder"""
        with open(".snap/index", "w", encoding="utf-8") as f:
            f.write("")

    def create_descri_file(self, description):
        """make_folder"""
        with open(".snap/description", "w", encoding="utf-8") as f:
            f.write(description)

    def init(self, description=""):
        """init"""
        self.make_snap_folder()
        self.make_info_folder()
        self.make_hook_folder()
        self.make_branch_folder()
        self.create_head_file()
        self.create_index_file()
        self.create_config_file()
        self.create_descri_file(description)
