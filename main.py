from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

def on_press(msg):
    msg = print("You are sending a console message.\nWelcome to KivyMD!")
    return msg
    
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text="Hello, Thiago !!!",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    on_press=on_press
                )
            )
        )


MainApp().run()