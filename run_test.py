import os
import shutil
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from commando import Commando


cmd = Commando()


def copy_all(src: Path, dst: Path):
   for path in src.iterdir():
    if path.is_dir():
        dir_path = dst / path.name
        shutil.copytree(path.resolve(), dir_path)
    else:
        shutil.copy2(str(path.resolve()), str(dst))


output_dir = "tmp"
branch = "gh-pages"
repo_url = "https://github.com/zztkm/GitPythonTest.git"

output_dir = Path(output_dir).resolve()

with TemporaryDirectory() as tmpdir:
    os.chdir(tmpdir)
    print(os.getcwd())

    s = f'git clone --depth 1 --branch {branch} "{tmpdir}"'
    res = cmd.run(s)
    print(res.returncode)

    if res.returncode == 0:
        cmd.run("git rm -rf .")
    else:
        cmd.run("git init")
        cmd.run(f"git checkout -b {branch}")
        cmd.run(f"git remote add origin {repo_url}")
    
    copy_all(output_dir, Path(tmpdir))

    cmd.run("git add --all")

    cmd.run('git commit -m "deploy gh-pages"')

    print(os.getcwd())
    res = cmd.run(f"git push --force origin {branch}")
    if res.returncode == 0:
        print("Successful push gh-pages")
    else:
        print(res.args)
        print(res.stderr.decode(sys.getfilesystemencoding()))
        sys.exit(res.returncode)

sys.exit(0)