import os
import requests
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

console = Console()

API_KEY = os.getenv("NUMVERIFY_API_KEY")


def scan(phone):
    console.rule("[bold green]Phone Investigation")

    if not API_KEY:
        console.print("[red][ERROR][/red] NUMVERIFY_API_KEY tidak ditemukan di file .env")
        return

    try:
        url = "http://apilayer.net/api/validate"

        params = {
            "access_key": API_KEY,
            "number": phone
        }

        response = requests.get(url, params=params, timeout=15)
        data = response.json()

        if not data.get("valid"):
            console.print("[red][-] Nomor tidak valid atau tidak ditemukan.[/red]")
            return

        console.print(f"[cyan]Number     :[/cyan] {data.get('international_format')}")
        console.print(f"[cyan]Country    :[/cyan] {data.get('country_name')}")
        console.print(f"[cyan]Location   :[/cyan] {data.get('location')}")
        console.print(f"[cyan]Carrier    :[/cyan] {data.get('carrier')}")
        console.print(f"[cyan]Line Type  :[/cyan] {data.get('line_type')}")
        console.print(f"[green]Valid      : {data.get('valid')}[/green]")

    except Exception as e:
        console.print(f"[red][ERROR][/red] {e}")