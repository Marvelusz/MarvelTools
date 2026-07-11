from rich.console import Console
from engines.phoneinfoga import scan

console = Console()

def run():
    console.clear()

    console.rule("[bold green]Phone Investigation")

    phone = console.input("[cyan]Phone Number[/cyan] > ")

    console.print()

    scan(phone)

    input("\nPress ENTER...") 