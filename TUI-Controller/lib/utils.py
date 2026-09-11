from rich.console import Console
from rich.text import Text
from .ui.main import TUI
import socket

console = Console()

banner = Text("""
████████╗████████╗████████╗██╗      ██╗███╗   ██╗█████████╗        ██╗████████╗
╚══██╔══╝██╔═════╝██╔═════╝██║      ██║████╗  ██║██║    ██║        ██║╚═════██║
   ██║   ████████╗██║      ███████████║██╔██╗ ██║██║ █╗ ██║███████╗██║      ██║
   ██║   ██╔═════╝██║      ██╔══════██║██║╚██╗██║██║ ╚╝ ██║╚══════╝██║      ██║
   ██║   ████████╗████████╗██║      ██║██║ ╚████║█████████║        ██║      ██║
   ╚═╝   ╚═══════╝╚═══════╝╚═╝      ╚═╝╚═╝  ╚═══╝╚════════╝        ╚═╝      ╚═╝
""", style="purple")

def dev_banner():
  console.print("[purple]Developed By", justify="center")
  console.print(banner, justify="center")

def get_local_ip():
  hostname = socket.gethostname()
  local_ip = socket.gethostbyname(hostname)
  return local_ip

def run_all():
  app = TUI()
  app.run()