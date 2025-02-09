# CIS12-Lab03

1. Full Function Header, and indicate the function name with a comment.

- def get_peer_node(username): # function name is get_peer_node
- def join_group(node, group): # function name is join_group
- def chat_task(ctx, pipe, n, group): # function name is chat_task
- def get_channel(node, group): # function name is get_channel

2. List all parameters and what you think they are. Put "UNSURE" if you don't have a guess.

- username: the user inputted name that was entered with get_username()
- node: UNSURE
- group: The group the user chooses to join with get_group()
- ctx: UNSURE
- pipe: UNSURE
- n: UNSURE, maybe it connects the user inputted name to something?

3. Note if the function returns anything. If it does, note what you believe it returns, and make a final note about what you believe the function

- def get_peer_node(username): # returns "n" which maybe connects the username to something, but I don't know what the peer_node actually is or what it does so my guess is it makes the initial connection
- def join_group(node, group): # does not return anything but prints a message to the screen indicating success
- def chat_task(ctx, pipe, n, group): # does not return anything but this function looks like it creates a connection to other user groups and prints a message based on the status
- def get_channel(node, group): # returns " zhelper.zthread_fork(ctx, chat_task, n=node, group=group)" but I have no idea what that is. My best guess is that is creates the communication channel users need to communicate to each other