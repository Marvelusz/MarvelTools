from rich.console import Console

console = Console()

def run():
    console.clear()

    console.print("""
[bold cyan]
╔══════════════════════════════════════════════════════╗
║                     MARVELUS                         ║
║               OSINT Framework v1.0                  ║
╚══════════════════════════════════════════════════════╝
[/bold cyan]
""")

    console.print("[bold green]Developer[/bold green]")
    console.print("• Name     : Rzkaelah (Marvelus)")
    console.print("• Language : Python 3")
    console.print("• Framework: Rich")
    console.print("• Version  : 1.0\n")

    console.print("[bold yellow]Features[/bold yellow]")
    console.print("• Username Investigation")
    console.print("• Email Investigation")
    console.print("• Phone Investigation")
    console.print("• IP Address Lookup")
    console.print("• Address Geolocation")
    console.print("• Coordinate Lookup")
    console.print("• Port Scanner")
    console.print("• OSINT Engines Integration\n")

    console.print("[bold magenta]Disclaimer[/bold magenta]")
    console.print(
        "MARVELUS dibuat untuk tujuan edukasi, penelitian, "
        "dan aktivitas keamanan siber yang sah. "
        "Segala bentuk penyalahgunaan tool ini menjadi "
        "tanggung jawab pengguna sepenuhnya."
    )

    console.print("\n[bold cyan]© 2026 Rzkaelah. All Rights Reserved.[/bold cyan]")

    input("\nPress ENTER to return...")