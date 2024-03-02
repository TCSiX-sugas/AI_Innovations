class ChatGPT:
    def reply(self, message):
        return "ChatGPT: " + message

class CodeGPT:
    def generate_code(self, task):
        return "CodeGPT generated code for task: " + task

# 默认使用ChatGPT
current_model = ChatGPT()

while True:
    print("Please choose models:")
    print("1. ChatGPT")
    print("2. CodeGPT")
    choice = input()

    if choice == "1":
        current_model = ChatGPT()
        print("Now has been Chatgpt")
    elif choice == "2":
        current_model = CodeGPT()
        print("Now has been CodeGPT")
    else:
        print("UNKNOWN")
        continue

    user_input = input("Please enter:")
    
    if isinstance(current_model, ChatGPT):
        print(current_model.reply(user_input))
    elif isinstance(current_model, CodeGPT):
        print(current_model.generate_code(user_input))
