from rich.console import Console
from engines.ipinfo import scan

console = Console()

def run():
    console.clear()
    ip = console.input("[cyan]IP Address[/cyan] > ")
    console.print()

    scan(ip)

    input("\nPress ENTER...")