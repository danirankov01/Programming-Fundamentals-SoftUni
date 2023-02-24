class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes




word = "danibananicecoskakaleco"
counter = 0
if(word.count("dani")): counter += 1
if(word.count("skakaleco")): counter += 1

print(counter)