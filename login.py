import requests
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
        if self.is_input_valid():
            self.log(f"Login button pressed ==> U:'{self.username.value}' P:'{self.password.value}'")
            self.send_credentials()

    def is_input_valid(self):
        if not self.username.value:
            self.username.add_class("error")
            self.log("Username is required")
            return False
        if not self.password.value:
            self.password.add_class("error")
            self.log("Password is required")
            return False
        return True

    def send_credentials(self):
        #FIXME: Error handling
        response = requests.post("https://dummyjson.com/auth/login", json={
            "username": self.username.value,
            "password": self.password.value,
        })
        self.token = response.json()["token"]
        self.log(f"Sending credentials to API ==> T:'{self.token}'")


class Pancake(App):

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    def compose(self) -> None:
        yield Header(show_clock=True)
        yield LoginForm()
        yield Footer()


if __name__ == "__main__":
    app = Pancake()
    app.run()