from rich.console import Console
from engines.holehe import scan

console = Console()

def run():
    email = console.input("[cyan]Email : [/cyan]")
    scan(email)