from rich.console import Console
from engines.nmap import scan

console = Console()

def run():
    console.clear()

    target = console.input("[cyan]Target IP / Domain[/cyan] > ")

    console.print()

    scan(target)

    input("\nPress ENTER...")