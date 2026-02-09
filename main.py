from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class ChatLayout(BoxLayout):
    chat_text = StringProperty("ربات: سلام! 👋\n\n")

    def send_message(self, user_message):
        if not user_message.strip():
            return

        self.chat_text += f"شما: {user_message}\n"
        response = self.get_response(user_message)
        self.chat_text += f"ربات: {response}\n\n"

    def get_response(self, text):
        text = text.lower()

        if "سلام" in text:
            return "سلام! خوشحالم می‌بینمت 😊"
        elif "خوبی" in text:
            return "ممنون، خوبم 🌸 تو چطوری؟"
        elif "اسمت" in text:
            return "من PersianChatGPT هستم 🤖"
        elif "خداحافظ" in text:
            return "خداحافظ! روز خوبی داشته باشی 👋"
        else:
            return "فعلاً فقط می‌تونم سلام و احوال‌پرسی کنم 🙂"


class PersianChatGPTAndroid(App):
    def build(self):
        return ChatLayout()


if __name__ == "__main__":
    PersianChatGPTAndroid().run()
