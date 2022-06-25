from typing import List
from git.repo.base import Repo
from git.exc import GitCommandError
from tempfile import TemporaryDirectory


repo = Repo(".")
remote_url = repo.remote().url
remote = "origin"
deployment_branch = "gh-pages"

with TemporaryDirectory() as tmpdir:
    try:
        tmp_repo = Repo.clone_from(remote_url, tmpdir, branch=deployment_branch)
        tmp_repo.git.rm(tmpdir, r=True)
    except GitCommandError:
        tmp_repo = Repo.init(tmpdir)
        tmp_repo.git.checkout("-b", deployment_branch)
        tmp_repo.git.remo


    print("temp remote: ", tmp_repo.remote().url)
    current_branch_name = tmp_repo.active_branch.name

    names: List[str] = []
    for b in tmp_repo.branches:
        names.append(b.name)
    
    print(names)
    
    if deployment_branch in names:
        print("gh-pages ari")
        tmp_repo.git.checkout(deployment_branch)
    else:
        print("nasi")
        print("active branch name: ", current_branch_name)
        print(tmp_repo.active_branch.name)
        tmp_repo.git.push("origin", deployment_branch)

        print(tmpdir)