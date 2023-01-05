#######200 points########


# number = input().replace("-","").replace(".","")
# numbers = int(number)
# sum = 0

# while(numbers > 9):
#     for i in range(len(number)):
#         lastNumber = number[-i - 1]
#         sum += int(lastNumber)
#     number = str(sum)
#     numbers = sum
#     sum = 0

# print(numbers)




# inputNumber = int(input())
# primeNumbers = [1]
# notPrimeNumbers = []

# for number in range (1, inputNumber + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:
#                 notPrimeNumbers.append(number)
#                 break  
#         else:  
#             primeNumbers.append(number) 
        
#         for i in range(1, len(primeNumbers) + 1):
#             for j in primeNumbers:
#                 if(i <= j):
#                     print(i,end=" ")
#                 else:
#                     break
#                 break
#             print()
# twoElements = []
# for i in range(0, len(primeNumbers)):
#     for j in range(0, len(primeNumbers)):
#         if(i >= j):
#             if(i == j + 1):
#                 lastNumber = primeNumbers[i]
#                 afterLastNumber = primeNumbers[j]
#                 if(lastNumber - afterLastNumber >= 2):
#                     for k in range(lastNumber - afterLastNumber - 1):
#                         print(0, end=" ")
#             print(primeNumbers[j],end=" ")
#         else:
#             break            
#     print()

 




inputNumber = int(input())
primeNumbers = [1]

for number in range (1, inputNumber + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:
                break  
        else:  
            primeNumbers.append(number) 

for i in primeNumbers:
    for j in range(0, i):
        if(j + 1 in primeNumbers):
            print(1,end="")
        else:
            print(0,end="")
    print()










# sum = 0

# for i in range(1000):
#     number = int(input())

#     hundreds = number // 100 % 10
#     tens = number // 10 % 10
#     ones = number % 10

#     if(hundreds + ones == tens):
#         sum += number
#         continue
#     else:
#         print(sum)
#         break