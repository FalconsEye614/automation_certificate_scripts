#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os


def run(bckup):
    subprocess.call(["rsync", "-arq", bckup[0], bckup[1]])


if __name__ == "__main__":
    home = os.path.expanduser("~")
    src = "/data/prod/"
    dest = "/data/prod_backup/"
    src_lst = []

    for root, dirs, files in os.walk(home+src):
        # subprocess.call(["rsync", "-arq", src, dest])
        for name in dirs:
            dest_root = root.replace(src, dest)
            src_lst.append((root, dest_root))

    p = Pool(len(src_lst))
    p.map(run, src_lst)
