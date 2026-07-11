import requests
from rich.console import Console

console = Console()

def scan(lat, lon):
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"

        headers = {
            "User-Agent": "MARVELUS/1.0"
        }

        r = requests.get(url, headers=headers, timeout=10)
        data = r.json()

        addr = data.get("address", {})

        console.rule("[bold green]Coordinate Investigation")

        print(f"Latitude    : {lat}")
        print(f"Longitude   : {lon}")
        print(f"Address     : {data.get('display_name','-')}")
        print(f"Country     : {addr.get('country','-')}")
        print(f"Province    : {addr.get('state','-')}")
        print(f"City        : {addr.get('city') or addr.get('town') or addr.get('village','-')}")
        print(f"Postal Code : {addr.get('postcode','-')}")

    except Exception as e:
        console.print(f"[red]{e}[/red]")