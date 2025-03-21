"""Commit"""

import os
import pickle
import hashlib


class SnapShot:
    "SnapShot"

    def __init__(self):
        pass

    def add(self, files: list[str]):
        """add"""
        index_files: list = []

        with open(".snap/index", "rb") as f:
            try:
                index_files = pickle.load(f)
            except EOFError:
                pass

        for file in files:
            if file not in index_files:
                index_files.append(file)

        with open(".snap/index", "wb") as f:
            pickle.dump(index_files, f)

    def remove(self, files: list[str]):
        """add"""
        index_files: list = []

        with open(".snap/index", "rb") as f:
            try:
                index_files = pickle.load(f)
            except EOFError:
                pass

        for file in files:
            if file in index_files:
                index_files.remove(file)

        with open(".snap/index", "wb") as f:
            pickle.dump(index_files, f)

    def commit(self, message: str):
        """commit"""
        snap_shot_data = {"files": {}}
        snap_shot_hash = hashlib.sha256()

        with open(".snap/index", "rb") as f:
            files = pickle.load(f)

        for file in files:

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
