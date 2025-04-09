import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def typewriter(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

banner = f"""
{Fore.RED}  ______           _ _____                          
 |  ____|         | |  __ \\                         
 | |__   _ __   __| | |__) |__  _ __ __ _ _ __ _   _ 
 |  __| | '_ \\ / _` |  ___/ _ \\| '__/ _` | '__| | | |
 | |____| | | | (_| | |  | (_) | | | (_| | |  | |_| |
 |______|_| |_|\\__,_|_|   \\___/|_|  \\__,_|_|   \\__, |
                                              __/ |
                                             |___/  v1.0
{Style.BRIGHT}{Fore.CYAN}              Endpoint Wordlist Bruteforcer - By Caio Luchetti
"""

typewriter(banner, 0.002)

# Desenvolvido por Caio Luchetti (@cxiolz)

import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
import requests
import argparse
import csv
from rich.console import Console
from rich.table import Table

console = Console()

def scan_endpoints(base_url, wordlist, timeout, output_file):
    table = Table(title="EndPwner - API Endpoint Scanner")

    table.add_column("Endpoint", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Tempo (s)", style="green")

    results = []

    with open(wordlist, "r") as f:
        endpoints = [line.strip() for line in f.readlines() if line.strip()]

    for endpoint in endpoints:
        url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        try:
            response = requests.get(url, timeout=timeout)
            time = f"{response.elapsed.total_seconds():.2f}"
            status = str(response.status_code)
        except Exception as e:
            status = "ERROR"
            time = "-"
        
        table.add_row(endpoint, status, time)
        results.append([endpoint, status, time])

    console.print(table)

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Endpoint", "Status", "Tempo (s)"])
        writer.writerows(results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EndPwner - API Header & Endpoint Scanner")
    parser.add_argument("-u", "--url", required=True, help="URL base da API")
    parser.add_argument("-w", "--wordlist", required=True, help="Arquivo com lista de endpoints")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="Timeout de requisições (default: 5s)")
    parser.add_argument("-o", "--output", default="resultados.csv", help="Arquivo CSV de saída")
    args = parser.parse_args()

    scan_endpoints(args.url, args.wordlist, args.timeout, args.output)
