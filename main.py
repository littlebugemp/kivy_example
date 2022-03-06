from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "signup_screen"
        # print("Sign Up Clicked")


class SignUpScreen(Screen):
    def add_user(self,username,password):
        print(f"Signing up for {username} and {password}")


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()
        # return Button(text='Hello World')


if __name__ == "__main__":
    MainApp().run()
