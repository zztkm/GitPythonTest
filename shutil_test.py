import shutil
from pathlib import Path


def copy_all(src: Path, dst: Path):
   for path in src.iterdir():
    if path.is_dir():
        dir_path = dst / path.name
        shutil.copytree(path.resolve(), dir_path)
    else:
        shutil.copy2(str(path.resolve()), str(dst))

copy_all(Path("tmp"), Path("dist"))