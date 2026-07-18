import argparse
import os
import subprocess
import sys


def verify_efs(folder_path):
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder does not exist:\n{folder_path}")
        sys.exit(1)

    try:
        result = subprocess.run(
            ["cipher", "/c", folder_path],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode != 0:
            print("[ERROR] Failed to check EFS status.")
            print(result.stderr)
            sys.exit(result.returncode)

        print("\n========== EFS VERIFICATION ==========")
        print(f"Target Folder : {folder_path}")
        print("--------------------------------------")
        print(result.stdout)
        print("======================================")

    except FileNotFoundError:
        print("[ERROR] 'cipher' command was not found.")
        print("This tool only works on Windows NTFS systems.")
        sys.exit(1)

    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Verify Windows Encrypting File System (EFS) status of a folder."
    )

    parser.add_argument(
        "folder",
        help="Path of the folder to verify"
    )

    args = parser.parse_args()

    verify_efs(args.folder)


if __name__ == "__main__":
    main()
