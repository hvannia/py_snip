# python #rich
# pip install rich

# summary of rich's functionalities
# python -m rich


# Highlight code based on type

from rich import print, pretty

pretty.install()

print({"num_list1": [1, 2, 3], "num_list2": [3, 4, 5]})
print((1, 2, 3, 4))
print(False, True)

# Better help
from rich import inspect
from sklearn import datasets

# instead of
# help(datasets)
inspect(datasets, methods=True)
# trees
from rich.tree import Tree
from rich import print

tree = Tree("Dog Data")
tree.add("data1")

data2 = tree.add("data2")
data2.add("[red]Winner")
data2.add("[green]Chihuahua")
data2.add("[blue]Greyhound")

print(tree)


# Progress Bar

from rich.progress import track
from time import sleep


def scrape_data():
    sleep(0.1)


for _ in track(range(100), description="[green]Scraping data"):
    scrape_data()

# Progress bar with the  time when a particular task is finished executing, we can use console.status instead
from rich.console import Console
from time import sleep

console = Console()

datas = [1, 2, 3, 4, 5]
with console.status("[bold green]Scraping data...") as status:
    while datas:
        data = datas.pop(0)
        sleep(1)
        console.log(f"[green]Finish scraping data[/green] {data}")

    console.log(f"[bold][red]Done!")

# Spinner options
# `python -m rich.spinner`

# Specify other spinner

from rich.console import Console
from time import sleep

console = Console()

datas = [1, 2, 3, 4, 5]
with console.status("[bold green]Scraping data...", spinner="aesthetic") as status:
    while datas:
        data = datas.pop(0)
        sleep(1)
        console.log(f"[green]Finish scraping data[/green] {data}")

    console.log(f"[bold][red]Done!")
