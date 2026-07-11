from rich.console import Console

console = Console()


class Engine:

    def header(self, text):
        console.rule(f"[bold bright_green]{text}")

    def success(self, text):
        console.print(f"[green][+][/green] {text}")

    def error(self, text):
        console.print(f"[red][-][/red] {text}")

    def warning(self, text):
        console.print(f"[yellow][!][/yellow] {text}")

    def info(self, text):
        console.print(f"[cyan][*][/cyan] {text}")