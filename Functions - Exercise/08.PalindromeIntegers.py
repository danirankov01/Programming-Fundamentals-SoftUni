def palindrome(numbers):
    for i in numbers:
        isPalindrome = True
        for j in range(len(str(i))):
            if(str(i)[j] != str(i)[-j - 1]):
                isPalindrome = False
        print(isPalindrome)
numbers = list(map(int, input().split(", ")))
palindrome(numbers)