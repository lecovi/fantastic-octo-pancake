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
    username = ""
    password = ""

    def compose(self) -> ComposeResult:
        yield Static("Username", classes="label")
        yield Input(placeholder="Username", name="username")
        yield Static("Password", classes="label")
        yield Input(placeholder="Password", name="password", password=True)
        yield Static()
        yield Button("Login", variant="primary")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Event handler called when an input is changed."""
        if event.input.name == "username":
            self.username = event.input.value
            self.log(f"Input username changed: {self.username}")
        if event.input.name == "password":
            self.password = event.input.value
            self.log(f"Input password changed: {self.password}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        #TODO: I'm assuming that the input validation will be done here
        #TODO: I'm assuming that the API request will be done here
        #      perhaps something like:
        #
        #          token = api.login(self.username, self.password)

        self.log(f"Login button pressed ==> U:'{self.username}' P:'{self.password}'")


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