from rich.console import Console
from engines.coordinate import scan

console = Console()

def run():
    console.clear()

    lat = console.input("[cyan]Latitude[/cyan] > ")
    lon = console.input("[cyan]Longitude[/cyan] > ")

    console.print()

    scan(lat, lon)

    input("\nPress ENTER...")