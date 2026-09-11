import click
from rich.text import Text
from .utils import (
  console, dev_banner, get_local_ip,
  run_all
)

def print_version(ctx, param, value):
  if not value or ctx.resilient_parsing:
    return

  console.print("[cyan]Tool Version: 1.0.0")
  dev_banner()
  ctx.exit()

@click.group()
@click.option(
  "-v", "--version", 
  is_flag=True, 
  callback=print_version, 
  expose_value=False, 
  is_eager=True, 
  help="Show the version and exit."
)
def cli_args(): pass

@cli_args.command(
  help="Run the server."
)
@click.option(
  "-p", "--port", default=9000,
  type=int
)
def run(port):
  dev_banner()
  console.print(f"[green]\[+] Server is running on 127.0.0.1:{port}")
  console.print(f"[cyan]\[!] Access it on the LAN {get_local_ip()}:{port}")
  console.print("[cyan]Press Enter To Start The TUI");input()
  run_all()