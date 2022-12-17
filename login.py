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
        self.username = Input(placeholder="Username", name="username")
        yield self.username
        yield Static("Password", classes="label")
        self.password = Input(placeholder="Password", name="password", password=True)
        yield self.password
        yield Static()
        yield Button("Login", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        #TODO: I'm assuming that the input validation will be done here
        #TODO: I'm assuming that the API request will be done here
        #      perhaps something like:
        #
        #          token = api.login(self.username, self.password)

        self.log(f"Login button pressed ==> U:'{self.username.value}' P:'{self.password.value}'")


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