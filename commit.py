"""Commit"""

import os
import time
import pickle
import hashlib


class SnapShot:
    """SnapShot"""

    def __init__(self, branch):
        self.branch = branch
        self.created = time.ctime(time.time())

    def add(self, files: list[str]):
        """add"""
        index: dict[str, list[str]] = {}
        branch_index_files: list[str] = []

        with open(".snap/index", "rb") as f:
            try:
                index = pickle.load(f)
                branch_index_files = index[self.branch]
            except EOFError:
                pass

        for file in files:
            if file not in branch_index_files:
                branch_index_files.append(file)

        with open(".snap/index", "wb") as f:
            index[self.branch] = branch_index_files
            pickle.dump(index, f)

    def remove(self, files: list[str]):
        """add"""
        index: dict[str, list[str]] = {}
        branch_index_files: list[str] = []

        with open(".snap/index", "rb") as f:
            try:
                index = pickle.load(f)
                branch_index_files = index[self.branch]
            except EOFError:
                return

        for file in files:
            if file in branch_index_files:
                branch_index_files.remove(file)

        with open(".snap/index", "wb") as f:
            index[self.branch] = branch_index_files
            pickle.dump(index, f)

    def commit(self, message: str) -> str | None:
        """commit"""
        snap_shot_data: dict[str, dict[str, str]] = {"files": {}}
        snap_shot_hash = hashlib.sha256()

        index: dict[str, list[str]] = {}
        branch_index_files: list[str] = []

        with open(".snap/index", "rb") as f:
            try:
                index = pickle.load(f)
                branch_index_files = index[self.branch]
            except EOFError:
                return

        for file in branch_index_files:

            if not os.path.exists(file):
                return

            with open(file, "rb") as f:
                content = f.read()
                snap_shot_hash.update(content)
                snap_shot_data["files"][file] = content

        hash_digest = snap_shot_hash.hexdigest()
        snap_shot_data["file_list"] = list(snap_shot_data["files"].keys())

        # write commit message
        with open(f".snap/info/{hash_digest}", "w+", encoding="utf-8") as f:
            f.write(message)

        with open(f".snap/hook/{hash_digest}", "wb") as f:
            pickle.dump(snap_shot_data, f)

        print(f"Snapshot Created with Hash: {hash_digest}")

        return hash_digest

    def revert(self, hash_digest: str):
        """revert_to_snap_shot"""

        snap_shot_path: str = f".snap/hook/{hash_digest}"
        index: dict[str, list[str]] = {}
        branch_shot_files: list[str] = []
        snap_shot_data: str = None

        if not os.path.exists(snap_shot_path):
            print("SnapShot does not exits.")
            return

        with open(".snap/index", "rb") as f:
            try:
                index = pickle.load(f)
                branch_shot_files = index[self.branch]
            except EOFError:
                return

        with open(snap_shot_path, "rb") as f:
            snap_shot_data = pickle.load(f)

        for file in branch_shot_files:
            # os.makedirs(os.path.dirname(file), exist_ok=True)

            with open(file, "wb") as f:
                f.write(snap_shot_data["files"][file])

        current_files = set()

        for root, dirs, files in os.walk(".", topdown=True):
            if ".snap" not in dirs:
                return

            if ".snap" in root:
                continue

            for file in files:
                current_files.add(os.path.join(root, file))

        snap_shot_files = set(branch_shot_files)
        files_to_delete = current_files - snap_shot_files

        for file_path in files_to_delete:
            os.remove(file_path)
            print(f"Removed : {file_path}")

        print(f"Reverted to SnapShot : {hash_digest}")


# # write info for every commit
# def commit(directory):
#     """snap_init"""
#     snap_shot_hash = hashlib.sha256()
#     snap_shot_data = {"files": {}}

#     for root, _, files in os.walk(directory):

#         for file in files:
#             if ".snap" in os.path.join(root, file):
#                 continue

#             file_path = os.path.join(root, file)

#             with open(file_path, "rb") as f:
#                 content = f.read()
#                 snap_shot_hash.update(content)
#                 snap_shot_data["files"][file_path] = content

#     hash_digest = snap_shot_hash.hexdigest()
#     snap_shot_data["file_list"] = list(snap_shot_data["files"].keys())

#     with open(f".snap/{hash_digest}", "wb") as f:
#         pickle.dump(snap_shot_data, f)

#     print(f"Snapshot Created with Hash: {hash_digest}")
