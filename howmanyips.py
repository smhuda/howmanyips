import ipaddress
import sys
from rich.console import Console
from rich.progress import Progress
from time import sleep

console = Console()

def calculate_hosts_from_cidr(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return network.num_addresses
    except ValueError:
        console.print(f"Invalid CIDR notation: [bold red]{cidr}[/bold red]")
        return 0

def process_single_cidr(cidr):
    return calculate_hosts_from_cidr(cidr)

def process_file(file_path):
    total_hosts = 0
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            with Progress() as progress:
                task = progress.add_task("[green]Calculating hosts...", total=len(lines))
                for line in lines:
                    total_hosts += calculate_hosts_from_cidr(line.strip())
                    progress.update(task, advance=1)
                    sleep(0.1)  # Just to visualize the progress bar; can be removed for faster execution
    except FileNotFoundError:
        console.print(f"File not found: [bold red]{file_path}[/bold red]")
    return total_hosts

def main():
    console.print("[bold magenta]HowManyIPs[/bold magenta] - IP Range Host Calculator", justify="center")
    if len(sys.argv) != 2:
        console.print("Usage: [bold yellow]python script.py <CIDR or file path>[/bold yellow]")
        sys.exit(1)

    input_arg = sys.argv[1]

    if '/' in input_arg:
        total_hosts = process_single_cidr(input_arg)
    else:
        total_hosts = process_file(input_arg)

    console.print(f"Total hosts: [bold green]{total_hosts}[/bold green]")

if __name__ == "__main__":
    main()
