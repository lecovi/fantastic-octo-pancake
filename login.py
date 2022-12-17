from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import (
    Header,
    Footer,
    Static,
    Input,
    Button,
)


class LoginForm(Container):
    def compose(self) -> ComposeResult:
        yield Static("Username", classes="label")
        yield Input(placeholder="Username")
        yield Static("Password", classes="label")
        yield Input(placeholder="Password", password=True)
        yield Static()
        yield Button("Login", variant="primary")


class Pancake(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> None:
        yield Header(show_clock=True)
        yield LoginForm()
        yield Footer()


if __name__ == "__main__":
    app = Pancake()
    app.run()