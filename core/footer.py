from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()


def show_footer():

    footer = (
        "[bold cyan]MARVELUS v1.0[/]"
        " [white]•[/] "
        "[white]Open Source Intelligence Framework[/]"
        " [white]•[/] "
        "[dim]by RzkAelah[/]"
    )

    console.print()

    console.print(
        Panel(
            Align.center(footer),
            border_style="cyan",
            padding=(0, 1),
        )
    )