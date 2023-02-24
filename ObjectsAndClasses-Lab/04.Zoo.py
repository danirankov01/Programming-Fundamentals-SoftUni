class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species):
        result = []
        if species == "mammal":
            result.append(f"Mammals in {self.name}: {', '.join(self.mammals)}\n")
        elif species == "fish":
            result.append(f"Fishes in {self.name}: {', '.join(self.fishes)}\n")
        elif species == "bird":
            result.append(f"Birds in {self.name}: {', '.join(self.birds)}\n")

        result.append(f"Total animals: {self.__animals}")
        return ' '.join(result)

name_of_the_zoo = input()
zoo = Zoo(name_of_the_zoo)
number_of_animals = int(input())

for i in range(number_of_animals):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

line = input()
print(zoo.get_info(line))