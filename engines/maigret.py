import subprocess
from rich.console import Console

console = Console()


def scan(username):
    console.rule("[green]Maigret")

    try:
        subprocess.run(
            [
                "maigret",
                username
            ],
            check=False
        )

    except Exception as e:
        console.print(f"[red]{e}[/red]")