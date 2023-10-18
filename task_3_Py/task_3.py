# Skeleton file for HW3 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.

# Q2 - A
def hex_to_float(s):
    part_1= ((-1)**int(s[0]))*(16**(int(s[1:4],16)-2047)) #part one in formula from the excercise
    fraction= s[4:]
    sum_frac= 0

    for i,j in enumerate(fraction):  #calculating the fraction based on floating point represntation, from lecture
        sum_frac+= int(j, 16)*(1/(16**i))

    return part_1*sum_frac


# Q2 - B
import math

# Pad with zeros on the left side
def left_fill_zeros(bin_str, output_len):
    return '0' * (output_len - len(bin_str)) + bin_str

def float_to_hex(num):
    # Edge case
    if num == 0:
        return '0' * 16

    # Compute sign and force positive
    sgn = '0'
    if num < 0:
        sgn = '1'
        num = abs(num)

    # Compute shift
    shift = math.floor(math.log(num,16))
    bexp = hex(shift + 2047)[2:]
    bexp = left_fill_zeros(bexp, 3)

    # Shift the number
    num = num * (16 ** -shift)

    # Compute mantissa
    num = int(num * (16 ** 12))
    bfraction = hex(num)[2:]
    bfraction = left_fill_zeros(bfraction, 12)

    return sgn + bexp + bfraction

print(float_to_hex( 1166.161616))
print(hex_to_float("080148e295faa8a82"))
# Q3 - A
def search_combined(lst, key):
    #even
    left=0
    right=len(lst)-2
    while right - left > 2:
        mid= (right+left)//2
        if mid%2 ==1:
            mid+=1
        if lst[mid]==key:
            return mid
        if lst[mid]<key:
            left=mid
        if lst[mid]>key:
            right=mid
    if lst[right]==key:
        return right
    if lst[left]==key:
        return left
    #odds now
    left=len(lst)-1
    right=1
    while left - right >2 :
        mid= (left + right)//2
        if mid%2==0:
            mid-=1
        if lst[mid]==key:
            return mid
        if lst[mid]<key:
            left=mid
        if lst[mid]>key:
            right=mid
    if lst[right]==key:
        return right
    if lst[left]==key:
        return left

    return None


# Q3 - B
def sort_combined(lst):
    #i for even, j for odd
    i=0
    j=len(lst)-1
    final_list=[]

    while i <= (len(lst)-2) and j>= 1:
        if lst[i]<lst[j]:
          final_list.append(lst[i])
          i+=2
        elif lst[j]<lst[i]:
            final_list.append(lst[j])
            j-=2
        elif lst[i]==lst[j]:
            final_list.append(lst[i])
            final_list.append(lst[j])
            i+=2
            j-=2

    if j<1:    #odd is empty
        for m in range(i,len(lst)-1,2):
            final_list.append(lst[m])

    elif i > len(lst)-2 :     #even is empty
        for k in range(j,0,-2):
            final_list.append(lst[k])

    return final_list

# Q3 - C
def find_duplicate(lst):
    #look for even
    left=0
    right=len(lst)-2

    while right -left >2:
        mid=(right+left)//2
        if mid%2==1:
            mid+=1
        if lst[mid]==lst[mid+1]:
            return mid
        elif lst[mid]<lst[mid+1]:
            left=mid
        elif lst[mid]>lst[mid+1]:
            right=mid
    if lst[right]==lst[right+1]:
        return right
    elif lst[left]==lst[left+1]:
        return left

    return None


# Q4 - A, a
def find(lst, s):
    left=0
    right=len(lst)-1

    while left<right:
        mid= (right+left)//2
        if lst[mid]==s:
            return mid
        if lst[mid+1]==s:
            return mid+1
        if lst[mid-1]==s:
            return mid-1

        elif lst[mid+1]<s or lst[mid]<s:
            left=mid+1
        elif lst[mid-1]>s or lst[mid]>s:
            right= mid-1
    return None



# Q4 - A, b
def sort_from_almost(lst):
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            continue
        elif lst[i+1]<lst[i]:
            m=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=m
    return lst


# Q4 - B
def find_local_min(lst):
    left=0
    right=len(lst)-1
    while right>left:
        mid=(right+left)//2
        if lst[mid+1]>lst[mid] and lst[mid-1]>lst[mid]:
            return mid
        elif lst[mid+1]<lst[mid]:
            left= mid+1
        elif lst[mid-1]<lst[mid]:
            right=mid-1
    if lst[left]<lst[right]:
        return left
    else:
        return right

# Q5 - a
def string_to_int(s):
    alph_dict={"a":0 , "b":1 , "c":2 , "d":3 , "e":4}
    k=len(s)
    cnt=0
    for i in range(1, k+1):
        cnt+= alph_dict[s[-i]]*(5**(i-1))

    return cnt

# Q5 - b
def int_to_string(k, n):
    alph_dict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}
    sum=0
    string=""
    for i in range(1,k+1):
        x = (n-sum) // (5**(k-i))
        string= string+ str(alph_dict[x])
        sum+= x * (5**(k-i))

    return string



# Q5 - c
def sort_strings1(lst, k):
    table = [0]* (5**k)
    result = []
    for s in lst:
        table[string_to_int(s)] += 1
    for i in range(len(table)):
        if table[i]:
            result.extend([int_to_string(k, i)])
    return result

# Q5 - e
def sort_strings2(lst, k):
    result = []
    for i in range(5 ** k):
        for s in lst:
            if string_to_int(s) == i:
                result.append(s)
    return result


# Q6 - A
def code(string):
    s_num = "0123456789"
    numeric_dict = {s_num[i]: "0" + str(bin(i)[2:]).zfill(4) for i in range(len(s_num))}
    s = "abcdefghijklmnopqrstuvwxyz"
    alphabetic_dict = {s[i]: "1" + str(bin(i)[2:]).zfill(5) for i in range(len(s))}
    numeric_dict.update(alphabetic_dict)

    stri=""

    for elem in string:
        stri= stri + str(numeric_dict[elem])

    return stri


# Q6 - B
def decode(bin_str):
    s_num = "0123456789"
    s = "abcdefghijklmnopqrstuvwxyz"
    numeric_dict_vs = {"0" + str(bin(i)[2:]).zfill(4): s_num[i] for i in range(len(s_num))}
    alphabetic_dict_vs = {"1" + str(bin(i)[2:]).zfill(5): s[i] for i in range(len(s))}
    numeric_dict_vs.update(alphabetic_dict_vs)
    empty = ""
    i = 0

    while i < len(bin_str):
        if bin_str[i] == "0":  # nums
            empty = empty + str(numeric_dict_vs[bin_str[i:i + 5]])
            i += 5

        elif bin_str[i] == "1":
            empty = empty + str(numeric_dict_vs[bin_str[i:i + 6]])
            i += 6

    return empty
