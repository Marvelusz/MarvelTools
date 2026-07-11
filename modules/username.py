from rich.console import Console
from rich.panel import Panel

from engines.sherlock import scan as sherlock_scan
from engines.maigret import scan as maigret_scan

console = Console()


def run():
    console.clear()

    console.print(
        Panel.fit(
            "[bold green]USERNAME INVESTIGATION[/bold green]",
            border_style="green",
        )
    )

    username = console.input("\n[cyan]Target Username[/cyan] > ")

    console.print()

    sherlock_scan(username)

    console.print()

    maigret_scan(username)

    console.print("\n[bold green][✓] Investigation Finished[/bold green]")

    input("\nPress ENTER...")