import requests
from rich.console import Console

console = Console()

def scan(ip):
    console.rule("[bold green]IP Investigation")

    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()

        if r["status"] != "success":
            console.print("[red]IP tidak valid![/red]")
            return

        console.print(f"IP Address : {r['query']}")
        console.print(f"Country    : {r['country']}")
        console.print(f"Region     : {r['regionName']}")
        console.print(f"City       : {r['city']}")
        console.print(f"ISP        : {r['isp']}")
        console.print(f"Timezone   : {r['timezone']}")
        console.print(f"ASN        : {r['as']}")

        proxy = r.get("proxy", False)
        console.print(f"VPN        : {proxy}")

    except Exception as e:
        console.print(f"[red]{e}[/red]")