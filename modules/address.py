from rich.console import Console
from engines.nominatim import scan

console = Console()

def run():
    console.clear()

    address = console.input("[cyan]Address[/cyan] > ")

    console.print()

    scan(address)

    input("\nPress ENTER...")