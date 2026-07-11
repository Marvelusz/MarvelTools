import requests
from rich.console import Console

console = Console()

def scan(address):
    try:
        url = "https://nominatim.openstreetmap.org/search"

        headers = {
            "User-Agent": "MARVELUS/1.0"
        }

        params = {
            "q": address,
            "format": "json",
            "limit": 1,
            "addressdetails": 1
        }

        r = requests.get(url, headers=headers, params=params, timeout=10)
        data = r.json()

        if not data:
            console.print("[red]Address not found.[/red]")
            return

        info = data[0]
        addr = info.get("address", {})

        console.rule("[bold green]Address Investigation")

        print(f"Address     : {info.get('display_name')}")
        print(f"Latitude    : {info.get('lat')}")
        print(f"Longitude   : {info.get('lon')}")
        print(f"Country     : {addr.get('country','-')}")
        print(f"Province    : {addr.get('state','-')}")
        print(f"City        : {addr.get('city') or addr.get('town') or addr.get('village','-')}")
        print(f"Postal Code : {addr.get('postcode','-')}")

    except Exception as e:
        console.print(f"[red]{e}[/red]")