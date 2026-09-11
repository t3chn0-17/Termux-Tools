from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class TUI(App):

  TITLE = "CONTROLLER"

  def compose(self) -> ComposeResult:
    yield Header()
    yield Footer()