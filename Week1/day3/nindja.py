class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        self.call_history.append(call_record)
        print(call_record)

    def show_call_history(self):
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content,
        }
        self.messages.append(message)
        other_phone.messages.append(message)

    def show_outgoing_messages(self):
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"To: {msg['to']} - Content: {msg['content']}")

    def show_incoming_messages(self):
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"From: {msg['from']} - Content: {msg['content']}")

    def show_messages_from(self, other_phone):
        for msg in self.messages:
            if (
                msg["from"] == other_phone.phone_number
                and msg["to"] == self.phone_number
            ):
                print(f"From: {msg['from']} - Content: {msg['content']}")


# Test code
if __name__ == "__main__":
    phone1 = Phone("123456789")
    phone2 = Phone("987654321")

    phone1.call(phone2)
    phone1.show_call_history()

    phone1.send_message(phone2, "Hello, how are you?")
    phone2.send_message(phone1, "I'm fine, thanks!")

    print("\nOutgoing messages for phone1:")
    phone1.show_outgoing_messages()

    print("\nIncoming messages for phone1:")
    phone1.show_incoming_messages()

    print("\nMessages from phone2 to phone1:")
    phone1.show_messages_from(phone2)
