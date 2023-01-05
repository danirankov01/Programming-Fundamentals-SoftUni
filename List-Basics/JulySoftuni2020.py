###11111111### - 100

# companyName = input()
# ticketsForAdults = int(input())
# ticketsForKids = int(input())
# priceForAdult = float(input())
# taxService = float(input())

# priceForKids = priceForAdult * 0.3
# priceForAdultWithTax = priceForAdult + taxService
# priceForKidsWithTax = priceForKids + taxService
# wholeTickets = (ticketsForKids * priceForKidsWithTax) + (ticketsForAdults * priceForAdultWithTax)
# profit = 0.2 * wholeTickets

# print(f"The profit of your agency from {companyName} tickets is {profit:.2f} lv.")




###22222222### - 90

# priceOfLuggageOver20 = float(input()) #30
# kilogramsOfLuggage = float(input()) #18
# daysToTravel = int(input()) #15
# numberOfLuggage = int(input()) #2

# price = 0
# if(kilogramsOfLuggage <= 10):
#     price += 0.2 * priceOfLuggageOver20
# elif(kilogramsOfLuggage > 10 and kilogramsOfLuggage <= 20):
#     price += 0.5 * priceOfLuggageOver20
# else:
#     price += priceOfLuggageOver20

# if(daysToTravel > 30):
#     price += price * 0.10
# elif(daysToTravel >= 7 and daysToTravel <= 30):
#     price += price * 0.15
# else:
#     price += price * 0.4

# print(f"The total price of bags is: {price * numberOfLuggage:.2f} lv.")




###33333333### - 72

# numberOfDograma = int(input())
# kindOfDograma = input()
# deliveryOrNo = input()

# price = 0
# if(kindOfDograma == "90X130"):
#     kindOfDograma = 110
#     if(numberOfDograma >= 30 and numberOfDograma <= 60):
#         price += (numberOfDograma * kindOfDograma)
#         price -= price * 0.05
#     if(numberOfDograma > 60):
#         price += (numberOfDograma * kindOfDograma)
#         price -= price * 0.08
# elif(kindOfDograma == "100X150"):
#     kindOfDograma = 140
#     if(numberOfDograma >= 40 and numberOfDograma <= 80):
#         price += (numberOfDograma * kindOfDograma)
#         price -= price * 0.06
#     if(numberOfDograma > 80):
#         price += (numberOfDograma * kindOfDograma)
#         price -= price * 0.1
# elif(kindOfDograma == "130X180"):
#     kindOfDograma = 190
#     if(numberOfDograma >= 20 and numberOfDograma <= 50):
#         price += (numberOfDograma * kindOfDograma)
#         price -= price * 0.07
#     if(numberOfDograma > 50):
#         price += (numberOfDograma * kindOfDograma)
#         price -= price * 0.12
# else:
#     kindOfDograma = 250
#     if(numberOfDograma >= 25 and numberOfDograma <= 50):
#         price += (numberOfDograma * kindOfDograma)
#         price -= price * 0.09
#     if(numberOfDograma > 50):
#         price += (numberOfDograma * kindOfDograma)
#         price -= price * 0.14

# if(deliveryOrNo == "With delivery"):
#     price += 60
#     if(numberOfDograma >= 100):
#         price -= price * 0.04


# if(numberOfDograma < 10):
#     print("Invalid order")
# else:
#     print(f"{price:.2f} BGN")



###44444444### - 100

# from math import floor

# numberOfBalls = int(input())
# listOfColors = []
# for i in range(numberOfBalls):
#     listOfColors.append(input())
# points = 0

# red = 0
# orange = 0
# yellow = 0
# white = 0
# black = 0
# otherColors = 0

# for i in listOfColors:
#     if(i == "red"):
#         points += 5
#         red += 1
#     elif(i == "orange"):
#         points += 10
#         orange += 1
#     elif(i == "yellow"):
#         points += 15
#         yellow += 1
#     elif(i == "white"):
#         points += 20
#         white += 1
#     elif(i == "black"):
#         points = floor(points // 2)
#         black += 1
#     else:
#         otherColors += 1

# print(f"Total points: {points}")
# print(f"Red balls: {red}")
# print(f"Orange balls: {orange}")
# print(f"Yellow balls: {yellow}")
# print(f"White balls: {white}")
# print(f"Other colors picked: {otherColors}")
# print(f"Divides from black balls: {black}")




###55555555### - 100

# bestName = ""
# bestGoals = ""
# counter = 0
# while(True):
#     name = input()
#     if(name == "END"):
#         break
#     goals = int(input())
#     if(counter == 0):
#         counter += 1
#         bestName = name
#         bestGoals = goals
#     if(goals >= 10):
#         bestName = name
#         bestGoals = goals
#         print(f"{bestName} is the best player!")
#         print(f"He has scored {bestGoals} goals and made a hat-trick !!!")
#         break
#     if(bestGoals < goals):
#         bestName = name
#         bestGoals = goals
# if(bestGoals < 3):
#     print(f"{bestName} is the best player!")
#     print(f"He has scored {bestGoals} goals.")
# if(bestGoals >= 3 and bestGoals < 10):
#     print(f"{bestName} is the best player!")
#     print(f"He has scored {bestGoals} goals and made a hat-trick !!!")



###66666666###

firstNumber = int(input())
secondNumber = int(input())
newNumber = ""
while(firstNumber != 0):
    lastNumber = firstNumber % 10
    if(lastNumber % 2 != 0):
        newNumber += str(lastNumber)
    firstNumber //= 10

while(secondNumber != 0):
    lastNumber = secondNumber % 10
    if(lastNumber % 2 != 0):
        newNumber += str(lastNumber)
    secondNumber //= 10

print(newNumber)









###result 462