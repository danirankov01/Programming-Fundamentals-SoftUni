class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []    
        self.fishes = []
        self.birds = []

    def addAnimal(self, species, name):
        if(species == "mammal"):
            self.mammals.append(name)
        elif(species == "fishes"):
            self.fishes.append(name)
        elif(species == "birds"):
            self.birds.append(name)

        Zoo.__animals += 1

    def getInfo(self, species):
        result = ""
        if(species == "mammal"):
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif(species == "fishes"): 
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif(species == "birds"):
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result 

name = input()
number = int(input())
zoo = Zoo(name)

for i in range(number):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.addAnimal(species, name)

speciesInfo = input()
print(zoo.getInfo(speciesInfo))