import lab_chat

def main():
    start_chat()

def get_input(message, to_upper=True):
    if to_upper:
        response = input(message).strip().upper()
    else:
        response = input(message).strip()
    return response

def get_username():
    return get_input("Enter a name: ")

def get_group():
    return get_input("Enter a group: ")

def get_message():
    return get_input("Enter a message: ", False)

def initialize_chat():
    user = get_username()
    group = get_group()
    peer_node = lab_chat.get_peer_node(user)
    lab_chat.join_group(peer_node, group)
    channel = lab_chat.get_channel(peer_node, group)
    return channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

main()