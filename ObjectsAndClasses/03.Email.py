class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender 
        self.receiver = receiver
        self.content = content
        self.isSent = False

    def send(self):
        self.isSent = True

    def getInfo(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.isSent}"

emails = []

while(True):
    line = input().split()
    if(line[0] == "Stop"): break

    sender = line[0]
    receiver = line[1]
    content = line[2]

    email = Email(sender, receiver, content)
    emails.append(email)

sendedEmail = list(map(int, input().split(", ")))

for i in sendedEmail:
    emails[i].send()

for email in emails:
    print(email.getInfo())