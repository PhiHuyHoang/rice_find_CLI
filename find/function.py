from os import walk, path, system
from multiprocessing import Process

def open_file(link_file):
    system("notepad.exe " + link_file)

def get_list_file(root,search_line):
    for r, d, f in walk(root):
        for file in f:
            link_file = path.join(r, file)
            if search_line in open(link_file, encoding="utf8", errors='ignore').read():
                print(link_file)

    print("Done")