from typing import List
from git.repo.base import Repo


repo = Repo("./tmp")
repo.git.rm(".", r=True)