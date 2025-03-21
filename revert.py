"""Revert"""

import os
import pickle


def revert_to_snap(hash_digest):
    """revert_to_snap_shot"""
    snap_shot_path = f".snap/{hash_digest}"
    snap_shot_data = None

    if not os.path.exists(snap_shot_path):
        print("SnapShot does not exits.")
        return

    with open(snap_shot_path, "rb") as f:
        snap_shot_data = pickle.load(f)

    for file_path, content in snap_shot_data["files"].items():
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(content)

    current_files = set()

    for root, dirs, files in os.walk(".", topdown=True):
        if ".snap" not in dirs:
            return

        if ".snap" in root:
            continue

        for file in files:
            current_files.add(os.path.join(root, file))

    snap_shot_files = set(snap_shot_data["file_list"])
    files_to_delete = current_files - snap_shot_files

    for file_path in files_to_delete:
        os.remove(file_path)
        print(f"Removed : {file_path}")

    print(f"Reverted to SnapShot : {hash_digest}")
