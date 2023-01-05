###########11111111##########

# listNumbers = []
# numbers = input().split()
# sum = 0
# for i in numbers:
#     if(int(i) % 21 == 0):
#         sum += int(i)
#         listNumbers.append(int(i))

# result = 0
# while sum != 0:
#     lastNumber = sum % 10
#     result += lastNumber
#     sum //= 10

# print(result)









##########2222222222##########


# firstNumbers = input().split()
# secondNumbers = input().split()

# firstList = [int(x) for x in firstNumbers]
# secondList = [int(x) for x in secondNumbers]

# if(len(firstList) >= len(secondList)):
#     for i in range(len(firstList)):
#         if(i >= len(secondList)):
#             print("- " + str(firstList[i]) + " x")
#             continue
#         if(firstList[i] == secondList[i]):
#             print("+ " + str(firstList[i]) + " " + str(secondList[i]))
#         else:
#             print("- " + str(firstList[i]) + " " + str(secondList[i]))
# else:
#     for i in range(len(secondList)):
#         if(i >= len(firstList)):
#             print("- " + "x " + str(secondList[i]))
#             continue
#         if(firstList[i] == secondList[i]):
#             print("+ " + str(firstList[i]) + " " + str(secondList[i]))
#         else:
#             print("- " + str(firstList[i]) + " " + str(secondList[i]))












###########333333333333###########      ######TOP 1 TOP 1 TOP 1 TOP 1 TOP 1###########
date = input().split()

day = int(date[0])
month = date[1]
year = int(date[2])

temperature = int(input()) # + 1 / 20
rain = int(input()) # 30
winter = int(input()) // 7 # 7

optimalTemperature = 20
optimalRain = 30
#leap + 5celsius

currentDay = day
differenceTemperature = temperature - optimalTemperature
differenceRain = abs(rain - optimalRain) // 3

if(temperature >= optimalTemperature):
    differenceTemperature = temperature - optimalTemperature
else:
    differenceTemperature = temperature - optimalTemperature

if(differenceTemperature <= 0):
    difference = differenceTemperature - differenceRain - winter
else:
    difference = differenceTemperature - differenceRain - winter

if(year % 4 != 0 and year % 100 != 0):
    if(difference > 0):
        day -= difference
        if(day <= 0):
            biggerThan = difference - currentDay
            day = 28 - biggerThan
            month = "February"
    else:
        day -= difference
        if(day > 31):
            biggerThan = day - 31
            day = biggerThan
            month = "April"

else:
    if(difference > 0):
        day -= difference
        if(day <= 0):
            biggerThan = difference - currentDay
            day = 29 - biggerThan
            month = "February"
    else:
        day -= difference
        if(day > 31):
            biggerThan = day - 31
            day = biggerThan
            month = "April"
print(day, month, year)






#######BEST BEST BEST#########

# if(temperature >= optimalTemperature):
#     differenceTemperature = temperature - optimalTemperature
# else:
#     differenceTemperature = temperature - optimalTemperature

# if(year % 4 != 0 and year % 100 != 0):
#     day -= differenceTemperature
#     day += differenceRain
#     if(day <= 0 or day > 31):
#         if(day <= 0):
#             difference = abs(currentDay - differenceTemperature - differenceRain)
#             day = 29 - difference - 1
#             if(difference == 0):
#                 day = 29 - difference - 1
#             month = "February"
#         if(day > 31):
#             difference = abs(currentDay) + abs(differenceTemperature) + abs(differenceRain) - 31
#             day = difference
#             month = "April"
# else:
#     day -= differenceTemperature
#     day += differenceRain
#     if(day <= 0 or day > 31):
#         if(day <= 0):
#             difference = abs(currentDay - differenceTemperature - differenceRain)
#             day = 29 - difference
#             if(difference == 0):
#                 day = 29 - difference
#             month = "February"
#         if(day > 31):
#             difference = abs(currentDay) + abs(differenceTemperature) + abs(differenceRain) - 31
#             day = difference
#             month = "April"
# print(day, month, year)







    # if(temperature >= optimalTemperature):
    #     if(day > differenceTemperature):
    #         day -= differenceTemperature
    #     else:
    #         difference = differenceTemperature - day
    #         day = 28 - difference
    #         month = "February"
    # else:
    #     differenceTemperature = optimalTemperature - temperature
    #     if(day + differenceTemperature <= 31):
    #         day += differenceTemperature
    #     else:
    #         difference = day + differenceTemperature - 31
    #         day = 0 + difference
    #         month = "April"

    # if(rain > 30 or rain < 30):
    #     differenceRain = abs(rain - optimalRain) // 3
    # if(day > differenceRain):

    #     if(month == "March"):
    #         if(day + differenceRain <= 31):
    #             day += differenceRain
    #         else:
    #             difference = day + differenceRain - 31
    #             day = 0 + difference
    #             month = "April"
    #     else:
    #         if(month == "February"):
    #             if(day + differenceRain <= 28):
    #                 day += differenceRain
    #             else:
    #                 difference = day + differenceRain - 28
    #                 day = 0 + difference
    #                 month = "April"
    #         else: #april
    #             if(day > differenceRain):
    #                 day -= differenceRain
    #             else:
    #                 difference = differenceRain - day
    #                 day = 31 - difference
    #                 month = "March"
    # else:
    #     if(month == "March"):
    #         difference = differenceRain - rain
    #         day = 28 - difference
    #         month = "February"
    #     else:
    #         if(month == "April"):
    #             difference = 

# else:











##########33333333333333###########

# date = input().split()

# day = int(date[0])
# month = date[1]
# year = int(date[2])

# temperature = int(input())
# rain = int(input())
# winter = int(input()) // 7 #35 = 5

# optimalTemperature = 20 #1
# optimalRain = 30 #3
#leap + 5celsius





# if(year % 4 != 0):
#     differenceTemperature = temperature - optimalTemperature
#     if(day > differenceTemperature):
#         day -= differenceTemperature
#     else:
#         day = 28
#         difference = 



# if(year % 4 != 0):
#     differenceTemperature = temperature - optimalTemperature
#     if(differenceTemperature >= 0):
#         if(day > differenceTemperature):
#             if()
#             day -= differenceTemperature
#         else:
#             difference = differenceTemperature - day
#             day = 28
#             day -= difference
#             month = "February"
#     else:
#         differenceTemperature *= -1
#         if(day + differenceTemperature > 31):
#             difference = differenceTemperature - (31 - day)
#             month = "April"
#             day = 0
#             day += difference
#         else:
#             day += differenceTemperature

#     differenceRain = (rain - optimalRain) // 3
#     if(differenceRain > 0 or differenceRain < 0):
#         day += 1
#     day += winter


# else:
#     differenceTemperature = temperature + 5 - optimalTemperature
#     if(differenceTemperature >= 0):
#         if(day > differenceTemperature):
#             day -= differenceTemperature
#         else:
#             difference = differenceTemperature - day
#             day = 29
#             day -= difference
#             month = "February"
#     else:
#         differenceTemperature *= -1
#         if(day + differenceTemperature > 31):
#             difference = differenceTemperature - (31 - day)
#             month = "April"
#             day = 0
#             day += difference
#         else:
#             day += differenceTemperature
    
#     differenceRain = (rain - optimalRain) // 3
#     if(differenceRain > 0 or differenceRain < 0):
#         day += 1
#     day += winter
# if(day == 20 and month == "March" and year == 2021):
#     print(temperature)
#     print(day)
#     print(winter)
#     print(date)
# print(day, month, year)

# if(year % 4 != 0):
#     differenceTemperature = temperature - optimalTemperature
#     if(differenceTemperature >= 0):
#         if(day > differenceTemperature):
#             if(day + differenceTemperature > 31):
#                 difference = differenceTemperature - (31 - day)
#                 day = 0
#                 day += differenceTemperature
#                 month = "April"
#         else:
#             difference = differenceTemperature - day
#             day = 28
#             day -= difference
#             month = "February"
#     else:
#         differenceTemperature *= -1
#         if(day + differenceTemperature > 31):
#             difference = differenceTemperature - (31 - day)
#             month = "April"
#             day = 0
#             day += difference
#         else:
#             day += differenceTemperature

#     differenceRain = abs(rain - optimalRain) // 3
#     if(differenceRain > 0 or differenceRain < 0):
#         day += 1
#     day += winter


# else:
#     differenceTemperature = temperature + 5 - optimalTemperature
#     if(differenceTemperature >= 0):
#         if(day > differenceTemperature):
#             if(day + differenceTemperature > 31):
#                 difference = differenceTemperature - (31 - day)
#                 day = 0
#                 day += differenceTemperature
#                 month = "April"
#         else:
#             difference = differenceTemperature - day
#             day = 29
#             day -= difference
#             month = "February"
#     else:
#         differenceTemperature *= -1
#         if(day + differenceTemperature > 31):
#             difference = differenceTemperature - (31 - day)
#             month = "April"
#             day = 0
#             day += difference
#         else:
#             day += differenceTemperature
    
#     differenceRain = abs(rain - optimalRain) // 3
#     if(differenceRain > 0 or differenceRain < 0):
#         day += 1
#     day += winter

# print(day, month, year)



