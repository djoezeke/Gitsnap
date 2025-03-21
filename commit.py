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
        with open(".snap/index", "a", encoding="utf-8") as f:
            pickle.dump(files, f)

    def commit(self, message: str):
        """commit"""
        snap_shot_data = {"files": {}}
        snap_shot_hash = hashlib.sha256()

        # write commit message
        with open(f".snap/info/{snap_shot_hash}", "w", encoding="utf-8") as f:
            f.write(message)

        with open(".snap/index", "r", encoding="utf-8") as f:
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
