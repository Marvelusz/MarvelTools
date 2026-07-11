import nmap
from rich.console import Console

console = Console()

def scan(target):
    try:
        nm = nmap.PortScanner()

        nm.scan(target, arguments="-F")

        console.rule("[bold green]Port Scanner")

        print(f"Target : {target}")
        print()

        for host in nm.all_hosts():
            print(f"Host : {host}")

            for proto in nm[host].all_protocols():
                print(f"Protocol : {proto}")

                ports = sorted(nm[host][proto].keys())

                for port in ports:
                    state = nm[host][proto][port]["state"]
                    service = nm[host][proto][port]["name"]

                    print(f"{port}/tcp  {state:<8} {service}")

    except Exception as e:
        console.print(f"[red]{e}[/red]")