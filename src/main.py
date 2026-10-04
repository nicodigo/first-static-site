import os
import shutil


def copy_files(src: str, dst: str) -> None:
    for item in os.listdir(src):
        if os.path.isfile(os.path.join(src, item)):
            shutil.copy(os.path.join(src, item), os.path.join(dst, item))
            print(f"copying... {os.path.join(src, item)} to {os.path.join(dst, item)}")
        else:
            os.makedirs(os.path.join(dst, item), exist_ok=True)
            copy_files(os.path.join(src, item), os.path.join(dst, item))


def copy_contents(src: str, dst: str) -> None:
    if not os.path.exists(src):
        raise FileNotFoundError("source directory not found")

    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.makedirs(dst)
    print("calling copy files")

    copy_files(src, dst)


def main() -> None:
    copy_contents("./static", "./public")


if __name__ == "__main__":
    main()
