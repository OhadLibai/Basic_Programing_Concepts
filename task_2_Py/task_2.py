# Skeleton file for HW2 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw2_ID.py).

import random  # loads python's random module in order to use random.random() in question 2

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = ["206843328"]

############
# QUESTION 1
############


# 1a
def risk_factor(n):
    if n<21:
        return  1-(n/42)
    else:
        n= n-21
        return 0.5-(min(n,14)/35)


# 1b
def students_risk_factors(students):
    for key in students.keys():
        if students[key]<21:
            students[key]= 1 - (students[key]/42)
        else:
            students[key]= students[key]-21
            students[key]= 0.5 - (min(students[key],14)/35)

    return students

# 1c
def class_risk_factor(student_factors):
    return sum(student_factors.values())/len(student_factors)

# 1d
def convert_to_list(student_factors):
    tmp_list = [(l, k) for l, k in student_factors.items()]
    final_list= sorted(tmp_list, key= lambda tuple: tuple[1])

    return final_list


# 1e
def partition_class(student_factors, threshold):
    general = convert_to_list(student_factors)
    campus=[]
    home=[]

    for tuple in general:
        campus.append(tuple)
        if ((sum(tuple[1] for tuple in campus)) / len(campus)) < threshold:
            continue
        else:
            campus.remove(tuple)
            home.append(tuple)

    campus= { x:y for (x,y) in campus }
    home=   { x:y for (x,y) in home }
    return (campus,home)

############
# QUESTION 2
############

# 2a
def coin():
    randomness= random.random()
    if randomness < 0.5:
        return True
    else:
        return False

def roll_dice(d):
    randomness = random.random()
    interval_list = [((i - 1) / d, (i / d)) for i in range(1, d + 1)]

    for j in range(len(interval_list)):
        if interval_list[j][0] <= randomness <= interval_list[j][1]:
            return j + 1

def roulette(bet_size, parity):
    num= roll_dice(37) - 1

    if num==0:
        return 0

    if parity%2==0 and num%2==0:
        return bet_size*2

    elif parity%2==1 and num%2==1:
        return bet_size*2

    else:
        return 0


def roulette_repeat(bet_size, n):
    profit = 0

    for i in range(n):
        profit += roulette(bet_size, coin())

    return profit - (bet_size * n)


############
# QUESTION 3
############

# 3a
def inc(binary):
    k=len(binary)-1
    if binary[k]=="0":
        binary_final=binary[:k]+"1"
        return binary_final

    i= len(binary)-1
    while binary[i]==binary[i-1]:
        i -= 1
        if i==1:
            tmp= binary.replace("1","0")
            final="1" + tmp
            return final

    final_binary_1= binary[:i-1]+"1" + ("0"*(len(binary)-i))
    return final_binary_1


# 3b
def dec(binary):
    k=len(binary)-1
    if binary[k]=="1":
        binary_final= binary[:k]+"0"
        return  binary_final

    i=len(binary)-1
    while binary[i]==binary[i-1]:
        i -= 1
        if i==1:
            temp= binary[1:]
            final_1=temp.replace("0","1")
            return final_1

    final_2= binary[:i-1]+"0"+"1"+binary[i+1:]
    return final_2


# 3c
def add(bin1, bin2):
    comb_str=""
    bin1=bin1.zfill(len(bin2))
    bin2=bin2.zfill(len(bin1))
    i=len(bin1)-1
    while i>=0:
        if bin1[i]==bin2[i]=="0":
            comb_str= "0" + comb_str
            i-=1
            continue

        if bin1[i]!= bin2[i]:
            comb_str=  "1" + comb_str
            i-=1
            continue

        if bin1[i]==bin2[i]=="1":
            comb_str= "0" +comb_str
            i-=1
            if i== -1:
                comb_str= "1" + comb_str
                return comb_str

            while (bin1[i]=="1" or bin2[i]=="1") and i>=0:
                if bin1[i]==bin2[i]:
                    comb_str= "1" +comb_str
                    i-=1
                    continue

                if bin1[i]!=bin2[i]:
                    comb_str="0"+comb_str
                    i-=1
                    continue
            if i<0:
                comb_str= "1"+ comb_str
                return comb_str
            comb_str= "1" +comb_str
            i-=1
            continue

    return comb_str




# 3d
def leq(bin1, bin2):
    if bin2==bin1:
        return True
    elif len(bin2)>len(bin1):
        return True
    elif len(bin1)>len(bin2):
        return False
    i=0
    while bin2[i]>=bin1[i]:
        if bin2[i]=="1" and bin1[i]=="0":
            return True
        i+=1

    return False


# 3e
def is_divisor(bin1, bin2):
    if bin1 == bin2:
        return True

    while not leq(bin1, bin2):
        bin2 = add(bin2, bin2)
    if bin1 == bin2:
        return True

    else:
        return False



############
# QUESTION 4
############

# 4a
def has_repeat1(s, k):
    sub_list= [ s[i:i+k] for i in range(len(s)-k+1)]
    for sub in sub_list:
        if sub_list.count(sub)>1:
            return True
    return False


# 4b
def has_repeat2(s, k):
    for i in range(len(s)-k+1):
        tmp= s[i:i+k]
        if s.count(tmp)>=2:
            return True
    return False


############
# QUESTION 5
############

def parse_primes(filename):
    primes = []
    with open(filename, "r") as f:
        for line in f:
            primes += [int(num_str) for num_str in line.split(" ")[:-1] if num_str]
    return set(primes)

# 5a
def check_goldbach_for_num(n, primes_set):
    primes_set_2=primes_set.copy()
    for num_1 in primes_set:
        for num_2 in primes_set_2:
            if num_1+num_2==n:
                return True
    return False

# 5b
def check_goldbach_for_range(limit, primes_set):
    even_set=set([i for i in range(4,limit,2)])
    primes_set_2=primes_set.copy()
    checking=set()

    for even in even_set:
        for num_1 in primes_set:
            for num_2 in primes_set_2:
                if num_1+num_2==even:
                    checking.add(even)
                    break
            continue
        if even not in checking:
            return False

    return True


# 5c1
def check_goldbach_for_num_stats(n, primes_set):
    primes_list=list(primes_set)
    cnt=0
    for i in range(len(primes_list)):
        for j in range(i, len(primes_list)):
            if primes_list[i]+primes_list[j]==n:
                cnt +=1

    return cnt

# 5c2
def check_goldbach_stats(limit, primes_set):
    primes_list = list(primes_set)
    nums_stats = {}
    count_stats = {}
    for i in range(len(primes_list)):
        if primes_list[i] < limit:
            for j in range(i, len(primes_list)):
                prime_sum = primes_list[i] + primes_list[j]
                if prime_sum < limit and prime_sum % 2 == 0:
                    nums_stats[prime_sum] = nums_stats.get(prime_sum, 0) + 1
    for num in nums_stats:
        count_stats[nums_stats[num]] = count_stats.get(nums_stats[num], 0) + 1
    return count_stats



############
# QUESTION 6
############


#6a
def divisors(n):
    dividers=[ i for i in range(1,n) if n%i==0]
    return dividers


# 6b
def perfect_numbers(n):
    cnt=0
    i=1
    final_list=[]
    while cnt < n:
        if sum(divisors(i))==i:
            final_list.append(i)
            cnt+=1
        i+=1
    return final_list



# 6c
def abundant_density(n):
    cnt_abd=0
    for i in range(1,n+1):
        if sum(divisors(i))>i:
            cnt_abd+=1

    return cnt_abd/n

# 6e
def semi_perfect_3(n):
    list_1=divisors(n)
    list_2=list_1.copy()
    list_3=list_1.copy()
    for num_1 in list_1:
        for num_2 in list_2:
            if num_1!=num_2:
                for num_3 in list_3:
                    if num_2!=num_3 and num_1!=num_3:
                        if num_1+num_2+num_3==n:
                            return [num_1,num_2,num_3]

