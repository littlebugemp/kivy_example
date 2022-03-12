import random
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
from pathlib import Path
import glob

Builder.load_file("design.kv")


class ForgotPassword(Screen):
    pass


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "signup_screen"
        # print("Sign Up Clicked")

    def forgot_password(self):
        self.manager.current = "forgot_pass"
        # print("Forget Password??")

    def login(self, username, password):
        if username and password:
            # print("Value")
            with open("users.json") as file:
                users = json.load(file)
            if username in users and users[username]['password'] == password:
                # print("login successful")
                self.manager.transition.direction = 'right'
                self.manager.current = 'login_success'
                self.ids.username.text = ""
                self.ids.password.text = ""
            else:
                self.ids.loginmessage.text = "Wrong Username or Password"
            # print("wrong username or password")
            # print(username, password)
        else:
            self.ids.loginmessage.text = "Please Enter Username or Password"


class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def enlighten_me(self, usrinput):
        usrinput = usrinput.lower()
        available_feelings = glob.glob("quotes/*txt")  # fetching all present files in the given path
        # print(available_feelings)  # will give all files name with path present in given path
        available_feelings = [Path(filename).stem for filename in
                              available_feelings]  # extracting filename from file path
        # print(available_feelings)
        if usrinput in available_feelings:
            with open(f"quotes/{usrinput}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote_text.text = random.choice(quotes)
            # print(quotes)
        else:
            self.ids.quote_text.text = "Try Another Feeling :)"


class SignUpScreen(Screen):
    def add_user(self, username, password):
        if username and password:
            # print("hello")
            with open("users.json") as file:  # opening a json file
                users = json.load(file)  # converting file content to json object
                # print(users)
                users[username] = {'username': username, 'password': password,
                                   'created': datetime.now().strftime("%Y=%m-%d %H-%M-%S")}  # adding a new user
                # print(users)
            with open("users.json", 'w') as file:
                json.dump(users, file)  # writing user to new file
            self.manager.current = "sign_up_success"
            self.ids.username.text = ""
            self.ids.password.text = ""
            # print(f"Signing up for {username} and {password}")
        else:
            self.ids.signupmsg.text = "Username and password can not be null or empty."
            # print("Username and password can not be null or empty.")


class SignUpScreenSuccess(Screen):
    def move_to_login_page(self):
        self.manager.transition.direction = 'right'  # screen transition right by default its left to right
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()
        # return Button(text='Hello World')


if __name__ == "__main__":
    MainApp().run()
