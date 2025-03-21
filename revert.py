"""Revert"""

import os
import pickle


def revert(hash_digest):
    """revert_to_snap_shot"""

    snap_shot_path = f".snap/hook/{hash_digest}"
    snap_shot_data = None
    shot_file_list = []

    if not os.path.exists(snap_shot_path):
        print("SnapShot does not exits.")
        return

    with open(".snap/index", "rb") as f:
        shot_file_list = pickle.load(f)

    with open(snap_shot_path, "rb") as f:
        snap_shot_data = pickle.load(f)

    for file in shot_file_list:
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

    snap_shot_files = set(shot_file_list)
    files_to_delete = current_files - snap_shot_files

    for file_path in files_to_delete:
        os.remove(file_path)
        print(f"Removed : {file_path}")

    print(f"Reverted to SnapShot : {hash_digest}")
