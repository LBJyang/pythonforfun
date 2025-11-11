import os
import sys
import stat
import time


def dir_l(path="."):
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        st = os.stat(full_path)
        mode = "d" if stat.S_ISDIR(st.st_mode) else "-"
        perms = "".join(
            [
                "r" if st.st_mode & stat.S_IRUSR else "-",
                "w" if st.st_mode & stat.S_IWUSR else "-",
                "x" if st.st_mode & stat.S_IXUSR else "-",
                "r" if st.st_mode & stat.S_IRGRP else "-",
                "w" if st.st_mode & stat.S_IWGRP else "-",
                "x" if st.st_mode & stat.S_IXGRP else "-",
                "r" if st.st_mode & stat.S_IROTH else "-",
                "w" if st.st_mode & stat.S_IWOTH else "-",
                "x" if st.st_mode & stat.S_IXOTH else "-",
            ]
        )
        size = st.st_size
        mtime = time.strftime("%b %d %H:%M", time.localtime(st.st_mtime))
        print(f"{mode}{perms}{size:8}{mtime}{name}")


def find_files(keyword, path="."):
    for root, _, files in os.walk(path):
        for f in files:
            if keyword in f:
                print(os.path.relpath(os.path.join(root, f), path))


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-l":
        dir_l()
    elif len(sys.argv) == 3 and sys.argv[1] == "-f":
        find_files(sys.argv[2])
    else:
        print(
            "用法:\n  python dir-t.py -l   # 列出目录\n  python dir-t.py -f s # 搜索文件名包含's'的文件"
        )
