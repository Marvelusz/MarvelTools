from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align
from rich.table import Table
from datetime import datetime

console = Console()


def show_banner():
    now = datetime.now()
    console.clear()

    logo = r"""
███╗   ███╗ █████╗ ██████╗ ██╗   ██╗███████╗██╗     ██╗   ██╗███████╗
████╗ ████║██╔══██╗██╔══██╗██║   ██║██╔════╝██║     ██║   ██║██╔════╝
██╔████╔██║███████║██████╔╝██║   ██║█████╗  ██║     ██║   ██║███████╗
██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ██║     ██║   ██║╚════██║
██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗╚██████╔╝███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝ ╚══════╝
"""

    console.print(
        Panel(
            Align.center(
                f"[bold cyan]{logo}[/]\n"
                "[white]Open Source Intelligence Framework[/]\n"
                "[bold cyan]Version 1.0[/] [white]•[/] [dim]by RzkAelah[/]"
            ),
            title="[bold cyan]MARVELUS[/]",
            border_style="cyan",
            padding=(0, 1),
        )
    )

    target = Table.grid(padding=0)
    target.add_column()

    for item in [
        "• Username",
        "• Email",
        "• Phone",
        "• IP",
        "• Domain",
    ]:
        target.add_row(f"[cyan]{item}[/]")

    system = Table.grid(padding=0)
    system.add_column(width=6)
    system.add_column(width=1)
    system.add_column()

    system.add_row("Date", ":", now.strftime("%d %b %Y"))
    system.add_row("Time", ":", now.strftime("%H:%M"))
    system.add_row("Status", ":", "[green]READY[/]")

    console.print(
        Columns(
            [
                Panel(
                    target,
                    title="[bold cyan]TARGETS[/]",
                    border_style="cyan",
                    padding=(0, 1),
                ),
                Panel(
                    system,
                    title="[bold cyan]SYSTEM[/]",
                    border_style="cyan",
                    padding=(0, 1),
                ),
            ],
            equal=False,
            expand=False,
        )
    )

    console.print(
        Panel(
            Align.center(
                "[white]Sherlock[/] • "
                "[white]Maigret[/] • "
                "[white]Holehe[/] • "
                "[white]NumVerify[/] • "
                "[white]Nmap[/]"
            ),
            title="[bold cyan]FRAMEWORK[/]",
            border_style="cyan",
            padding=(0, 1),
        )
    )