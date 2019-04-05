from colorama import init
import click
import os
from .function import get_list_file

init(autoreset=True)

@click.command()
@click.option("--root","-r",help="Folder name", default=os.getcwd())
@click.argument("line")

def main(root: str, line: str):
     data = get_list_file(root,line)
def start():
    main(obj={})

if __name__ == "__main__":
    start()