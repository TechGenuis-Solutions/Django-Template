#!/usr/bin/env python

import subprocess


def setup_git_repository():
    subprocess.call("git init", shell=True)


def setup_git_hooks():
    subprocess.call("mv .hooks/* .git/hooks/", shell=True)


def setup_git_commit():
    subprocess.call("git add .", shell=True)
    subprocess.call("git commit -m 'Initial commit'", shell=True)


if __name__ == "__main__":
    setup_git_repository()
    setup_git_hooks()
    setup_git_commit()
