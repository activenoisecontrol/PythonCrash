def sndmsg(msgs, sntmsgs):
    """Moves messages from send to sent"""
    while msgs:
        msg = msgs.pop(0)
        print(msg)
        sntmsgs.append(msg)

msgs = ["Hello!","How are you?", "What's up?"]
sntmsgs = []

sndmsg(msgs[:], sntmsgs)
print(msgs)
print(sntmsgs)