#Skeleton file for HW1 - Spring 2021 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include the ID number of the student submitting the solution (hw1_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#The first ID should be the ID of the student submitting the solution
#For example: SUBMISSION_IDS = ["123456000", "987654000"]

# Question 4a
def num_different_letters(text):
    chars = "abcdefghijklmnopqrstuvwxyz"
    cnt = 0

    for letter in chars:
        if letter in text:
            cnt += 1

    return cnt


# Question 4b
def max_letter(text):
    char = "abcdefghijklmnopqrstuvwxyz"
    list = []

    for letter in char:
        letter_num = text.count(letter)
        list.append(letter_num)

    return max(list)


# Question 4c
def is_legal(text):
    char = "abcdefghijklmnopqrstuvwxyz"
    num_set = "0123456789"
    new_list = text.split()

    for object in new_list:
        for symbol in object:
            if symbol in char:
                if symbol in num_set:
                    return False

    return True


# Question 4d
def is_palindrome(text):
    n = len(text)
    left = 0
    right = n - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


# Question 5
def calc(expression):
    exp_list = expression.split("'")
    exp_str = str(exp_list[1])

    for i in range(2, len(exp_list), 2):
        if exp_list[i] == "*":
            exp_str = exp_str * int(exp_list[i + 1])
        elif exp_list[i] == "+":
            exp_str = exp_str + str(exp_list[i + 1])

    return exp_str


# Question 6
def max_div_seq(n, k):
    list = []
    empty = ""
    injected_num = str(k ** 2 + 1)
    str_n = str(n) + injected_num

    if k == 1:
        return (len(str_n) - 1)

    for num in str_n:
        if int(num) % k == 0:
            empty = empty + str(num)

        elif int(num) % k != 0:
            list.append(empty)
            empty = ""

    if len(list) == len(str_n):  # the case of 1 or 0
        for i in list:
            if i != '':
                return 1
        return 0

    return len(max(list, key=len))
