class Message:
    def __init__(self, message):
        self.message = message

    def print_message(self):
        print("{} {}".format(self.message, "bruh"))

message_object = Message("Hello Class")

message_object.print_message()