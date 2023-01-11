# def result(a, b, c):
#     listNumbers = [a, b, c]
#     if(0 in listNumbers):
#         print("zero")
#         exit()

#     isPositive = True
#     for i in listNumbers:
#         if(isPositive and i < 0):
#             isPositive = False
#             continue
#         if(isPositive == False and i < 0):
#             isPositive = True
#     if(isPositive):
#         print("positive")
#     else:
#         print("negative")

# first = int(input())
# second = int(input())
# third = int(input())
# result(first, second, third)





def check_numbers(first, second, third):
    if (first > 0 and second > 0 and third > 0) or\
            (first > 0 and second < 0 and third < 0) or \
            (second > 0 and first < 0 and third < 0) or \
            (third > 0 and first < 0 and second < 0):
        return "positive"
    elif first < 0 or second < 0 or third < 0:
        return "negative"
    elif first == 0 or second == 0 or third == 0:
        return "zero"


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(check_numbers(first_num, second_num, third_num))