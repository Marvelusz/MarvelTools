import subprocess
from rich.console import Console

console = Console()


def scan(username):
    console.rule("[green]Sherlock")

    try:
        subprocess.run(
            [
                "python",
                "-m",
                "sherlock_project",
                username
            ],
            check=False
        )

    except Exception as e:
        console.print(f"[red]{e}[/red]")