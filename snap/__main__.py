"""__main__"""

import argparse
from snapgit.snapgit import SnapGit


def main(command=None):
    """main"""

    parser = argparse.ArgumentParser(
        prog="SnapGit",
        description="SnapGit Version Control System",
        usage="snap [-v | --version] [-h | --help] <command> [<args>]",
    )

    # These are common Git commands used in various situations:
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="GitSnap v1.0.0",
        help="Print Version Info",
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Print Debug Info")

    parser.add_argument("--checkout", help="Checkout To Branch...")
    parser.add_argument("--revert", help="Revert To...")

    # start a working area
    parser.add_argument(
        "--init",
        nargs="?",
        help="Create an Empty SnapGit Repository or Reinitialize An Existing One",
    )
    parser.add_argument("--clone", help="Clone SnapGit Repository into A New Directory")

    # work on the current change
    parser.add_argument(
        "--add",
        nargs="*",
        help="Add file contents to the index",
    )
    parser.add_argument("--mv", nargs=2, help="Move or rename a file, a directory")
    parser.add_argument("--rm", help="Restore working tree files")
    parser.add_argument("--restore", nargs="*", help="Remove files from the index")

    # examine the history and state
    parser.add_argument(
        "--bisect", action="store_true", help="Find the commit that introduced a bug"
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Show changes between commits and working tree",
    )
    parser.add_argument("--grep", help="Print lines matching a pattern")
    parser.add_argument("--log", action="store_true", help="Show commit logs")
    parser.add_argument(
        "--show", action="store_true", help="Show various types of objects"
    )
    parser.add_argument(
        "--status", action="store_true", help="Show the working tree status"
    )

    # grow, mark and tweak your common history
    parser.add_argument("--branch", nargs="?", help="List, create, or delete branches")
    parser.add_argument(
        "--commit", action="store_true", help="Record changes to the repository"
    )
    parser.add_argument(
        "--merge", help="Join two or more development histories together"
    )
    parser.add_argument("--rebase", help="Reapply commits on top of another base tip")
    parser.add_argument(
        "--reset", action="store_true", help="Reset current HEAD to the specified state"
    )
    parser.add_argument("--switch", help="Switch branches")
    parser.add_argument(
        "--tag",
        help="Create, list, delete or verify a tag object signed with GPG",
    )

    # collaborate
    parser.add_argument(
        "--fetch", help="Download objects and refs from another repository"
    )
    parser.add_argument(
        "--pull",
        help="Fetch from and integrate with another repository or a local branch",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Update remote refs along with associated objects",
    )

    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        print("Catching an argumentError")

    if args.debug:
        print("debug: \n\t" + str(args))

    elif args.init:
        SnapGit().init("SnapGit")

    elif args.add:
        SnapGit().add(args.add)

    elif args.branch:
        SnapGit().new_branch(args.branch)

    elif args.checkout:
        SnapGit().checkout(args.checkout)

    elif args.commit:
        SnapGit().commit(args.commit)

    elif args.revert:
        SnapGit().revert(args.revert)


if __name__ == "__main__":
    main()
