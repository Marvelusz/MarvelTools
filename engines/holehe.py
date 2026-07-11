import subprocess
from rich.console import Console

console = Console()

def scan(email):
    console.print("\n[cyan][*][/cyan] Running Holehe...\n")

    try:
        subprocess.run(
            ["holehe", email],
            check=True
        )
    except Exception as e:
        console.print(f"[red]{e}[/red]")

    console.print("\n[green][✓] Email Investigation Finished[/green]")
    input("\nPress ENTER...")