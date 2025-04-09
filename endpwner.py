#!/usr/bin/env python3
import requests
import argparse
import time
import sys
import os
import random
import csv
from urllib.parse import urljoin
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

SEC_HEADERS = [
    'Content-Security-Policy',
    'Strict-Transport-Security',
    'X-Content-Type-Options',
    'X-Frame-Options',
    'X-XSS-Protection',
    'Referrer-Policy',
    'Permissions-Policy',
]

CVSS_SCORE_MAP = {
    7: "A - Alto",
    5: "B - Médio",
    3: "C - Baixo",
    1: "D - Fraco",
    0: "F - Nenhum"
}

def hacker_typewriter(lines, min_delay=0.005, max_delay=0.01, beep=False):
    for line in lines:
        color = random.choice(["\033[91m", "\033[92m", "\033[96m", "\033[93m"])
        sys.stdout.write(color)
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(min_delay, max_delay))
        sys.stdout.write("\n")
        if beep:
            sys.stdout.write("\a")
            sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\033[0m")  # Reset cor

def clear_screen():
    os.system("clear")

def banner():
    banner_lines = [
        "@@@@@@@@  @@@  @@@  @@@@@@@   @@@@@@@   @@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@  ",
        "@@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@ ",
        "@@!       @@!@!@@@  @@!  @@@  @@!  @@@  @@!  @@!  @@!  @@!@!@@@  @@!       @@!  @@@ ",
        "!@!       !@!!@!@!  !@!  @!@  !@!  @!@  !@!  !@!  !@!  !@!!@!@!  !@!       !@!  @!@ ",
        "@!!!:!    @!@ !!@!  @!@  !@!  @!@@!@!   @!!  !!@  @!@  @!@ !!@!  @!!!:!    @!@!!@!  ",
        "!!!!!:    !@!  !!!  !@!  !!!  !!@!!!    !@!  !!!  !@!  !@!  !!!  !!!!!:    !!@!@!   ",
        "!!:       !!:  !!!  !!:  !!!  !!:       !!:  !!:  !!:  !!:  !!!  !!:       !!: :!!  ",
        ":!:       :!:  !:!  :!:  !:!  :!:       :!:  :!:  :!:  :!:  !:!  :!:       :!:  !:! ",
        " :: ::::   ::   ::   :::: ::   ::        :::: :: :::    ::   ::   :: ::::  ::   ::: ",
        ": :: ::   ::    :   :: :  :    :          :: :  : :    ::    :   : :: ::    :   : : ",
        "",
        "             \033[95m[ Endpwner v1.0 - API Bruteforcer & Security Scanner ]",
        "                  by Caio Luchetti aka cxiolz",
    ]
    hacker_typewriter(banner_lines)

def load_wordlist(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

def calculate_security_score(headers):
    present = sum(1 for h in SEC_HEADERS if headers.get(h))
    percent = (present / len(SEC_HEADERS)) * 10
    if percent >= 9:
        return "A+ - Excelente"
    elif percent >= 7:
        return "A - Alto"
    elif percent >= 5:
        return "B - Médio"
    elif percent >= 3:
        return "C - Baixo"
    elif percent >= 1:
        return "D - Fraco"
    else:
        return "F - Nenhum"

def scan_endpoint(base_url, endpoint, timeout):
    url = urljoin(base_url, endpoint)
    try:
        start = time.time()
        response = requests.get(url, timeout=timeout)
        elapsed = round(time.time() - start, 2)
        status = response.status_code
        headers = {h: response.headers.get(h, '') for h in SEC_HEADERS}
        rank = calculate_security_score(headers)
        return endpoint, status, elapsed, headers, rank
    except requests.exceptions.RequestException:
        return endpoint, 'ERR', '-', {}, "F - Nenhum"

def save_results(results, output):
    with open(output, 'w', newline='') as csvfile:
        fieldnames = ['Endpoint', 'Status', 'Response Time (s)', 'Security Rank'] + SEC_HEADERS
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for res in results:
            row = {
                'Endpoint': res[0],
                'Status': res[1],
                'Response Time (s)': res[2],
                'Security Rank': res[4]
            }
            row.update(res[3])
            writer.writerow(row)

def print_results(results):
    table = Table(title="EndPwner - Resultados do Scanner de API")
    table.add_column("Endpoint")
    table.add_column("Status")
    table.add_column("Tempo (s)")
    table.add_column("Segurança")
    for ep, status, t, _, rank in results:
        table.add_row(ep, str(status), str(t), rank)
    console.print(table)

def main():
    clear_screen()
    banner()
    parser = argparse.ArgumentParser(description="[EndPwner] Scanner de endpoints e análise de headers de segurança em APIs REST")
    parser.add_argument("-u", "--url", required=True, help="URL base da API")
    parser.add_argument("-w", "--wordlist", required=True, help="Caminho da wordlist de endpoints")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="Timeout em segundos (padrão: 5)")
    parser.add_argument("-o", "--output", default="resultados.csv", help="Arquivo de saída (CSV)")
    args = parser.parse_args()

    endpoints = load_wordlist(args.wordlist)
    results = []

    console.print(f"[bold cyan]EndPwner rodando em:[/] {args.url}")

    for ep in track(endpoints, description="[green]Escaneando endpoints..."):
        result = scan_endpoint(args.url, ep, args.timeout)
        results.append(result)

    print_results(results)
    save_results(results, args.output)
    console.print(f"\n[bold green]Scan finalizado. Resultados salvos em:[/] {args.output}")

if __name__ == '__main__':
    main()
