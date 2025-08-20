from kivy.app import App
from kivy.uix.label import Label

class FriendsNotes(App):
    def build(self):
        return Label(text="Hello, Friends Notes!", font_size=40)

if __name__ == "__main__":
    FriendsNotes().run()
