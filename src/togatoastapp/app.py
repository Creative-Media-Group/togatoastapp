"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga_toast import show_toast


class TogaToastApp(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(
            children=[
                toga.Button(
                    text="Trigger toastmessage",
                    on_press=lambda _: show_toast(self=self, message="Hello World"),
                )
            ]
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return TogaToastApp()
