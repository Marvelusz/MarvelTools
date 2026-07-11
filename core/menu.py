from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align

console = Console()


def show_menu():

    left = """[bold cyan][01][/] Username Investigation
[bold cyan][02][/] Email Investigation
[bold cyan][03][/] Phone Investigation
[bold cyan][04][/] IP Address Lookup"""

    right = """[bold cyan][05][/] Address Lookup
[bold cyan][06][/] Coordinate Lookup
[bold cyan][07][/] Port Scanner
[bold cyan][08][/] About"""

    body = Columns(
        [
            Align.left(left),
            Align.left(right),
        ],
        equal=True,
        expand=True,
    )

    console.print(
        Panel(
            body,
            title="[bold cyan]MAIN MENU[/]",
            subtitle="[bold red][00][/bold red] Exit",
            border_style="cyan",
            padding=(0, 1),
        )
    )