# Skeleton file for HW6 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw6_ID.py).

# Enter all IDs of participating students as strings, separated by commas.

# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.


import random


############
# QUESTION 1
############

# Q1 a
def prefix_suffix_overlap(lst, k):
    list_indx=[]

    for i in range(len(lst)-1):##from first to last##
        j=i
        s=lst[i][:k]
        i+=1
        while i!=len(lst):
            if s==lst[i][-k:]:
                list_indx.append((j,i))
            i+=1

    for i in range(len(lst)-1,-1): ##the reversed loop, from last to first##
        j=i
        s=lst[i][:k]
        i-=1
        while i!= -1:
            if s==lst[i][-k:]:
                list_indx.append((j,i))
            i-=1

    return list_indx

# Q1 c
class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):
        """ returns ALL values of key as a list, empty list if none """
        i= self.hash_mod(key)
        main_list=[]
        for j in range(len(self.table[i])):
            if self.table[i][j][0]==key:
                main_list.append(self.table[i][j][1])
        return main_list

# Q1 d
def prefix_suffix_overlap_hash1(lst, k):
    d=Dict(len(lst))
    list_indx=[]

    for i in range(len(lst)):
        d.insert(lst[i][:k], i)

    for j in range(len(lst)):
        cand=d.find(lst[j][-k:])
        for m in range(len(cand)):
            if not cand[m]==j:
                list_indx.append((cand[m],j))

    return list_indx


############
# QUESTION 2
############

# Q2 a
def powers_of_2():
    yield 1
    s=1
    while True:
        yield s*2
        s*=2


# Q2 b
def pi_approx_monte_carlo():
    g_exp=powers_of_2()
    sample_size=0
    while True:
        sample_size+=next(g_exp)
        cnt=0
        for j in range(sample_size):
            x=random.random()
            y=random.random()
            if x**2+y**2 <=1.0:
                cnt+=1
        yield 4* (cnt/sample_size)   #the approximation of pi


# Q2 c
def leibniz():
    i=0
    j=1
    while True:
        yield ((-1)**i)*(1/j)
        i+=1
        j+=2

def infinite_series(gen):
    suma=0
    while True:
        suma+=next(gen)
        yield suma

def pi_approx_leibniz():
    g1=infinite_series(leibniz())
    g2=powers_of_2()
    pi_apx=0
    cnt=0

    while True:
        cnt+=next(g2)
        for i in range(cnt):
            pi_apx=next(g1)
        yield 4*pi_apx

# Q2 d
def unit_slicing():
    g2= powers_of_2()
    while True:
        n=next(g2)
        k=0
        final_list=[0.0]
        for j in range(1,n):
            k+=1/n
            final_list.append(k)
        yield final_list

def integral(func, a, b):
    g2=powers_of_2()
    g3=unit_slicing()

    while True:
        sum=0
        n= next(g2) #the number of the partitions
        list_points_uniform= next(g3)
        for i in range(1,n):
            x=a+(list_points_uniform[i]*(b-a)) #x coordinate
            sum+= ((b-a)/n) * func(x)
        yield sum


def pi_approx_integral():
    func1= lambda x: (1-(x**2))**0.5
    g5=integral(func1,-1,1)
    while True:
        yield 2*next(g5)


############
# QUESTION 6
############

# Q6 c
def CYK_d(st, rule_dict, start_var):
    ''' What is the minimal depth of a parse tree that generates st? '''
    n = len(st)
    table = [[None for j in range(n + 1)] for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n + 1):
            table[i][j] = {}

    fill_length_1_cells_d(table, rule_dict, st)

    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length
            fill_cell_d(table, i, j, rule_dict)

    if start_var in table[0][n]:
        return table[0][n][start_var]
    return -1

def fill_length_1_cells_d(table, rule_dict, st):
    n = len(st)
    for i in range(n):
        for lhs in rule_dict:
            if st[i] in rule_dict[lhs]:
                table[i][i+1][lhs] = 1


def fill_cell_d(table, i, j, rule_dict):
    for k in range(i + 1, j):
        for lhs in rule_dict:
            for rhs in rule_dict[lhs]:
                if len(rhs) == 2:
                    X, Y = rhs[0], rhs[1]
                    if X in table[i][k] and Y in table[k][j]:
                        d = max(table[i][k][X], table[k][j][Y]) + 1
                        if lhs in table[i][j]:
                            table[i][j][lhs] = min(table[i][j][lhs], d)
                        else:
                            table[i][j][lhs] = d


########
# Tester
########

def test():
    import math

    ############
    # QUESTION 1
    ############

    # Q1 a
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("error in prefix_suffix_overlap")

    # Q1 c
    d = Dict(3)
    d.insert("a", 56)
    d.insert("a", 34)
    if sorted(d.find("a")) != sorted([56, 34]) or d.find("b") != []:
        print("error in Dict.find")

    # Q1 d
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap_hash1(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("error in prefix_suffix_overlap_hash1")

    ############
    # QUESTION 2
    ############

    # Q2 a
    gen = powers_of_2()
    if [next(gen) for i in range(5)] != [1, 2, 4, 8, 16]:
        print('error in powers_of_2')

    # Q2 b
    gen = pi_approx_monte_carlo()
    first_apporx = next(gen)
    [next(gen) for i in range(8)]
    tenth_approx = next(gen)
    [next(gen) for i in range(9)]
    twentyth_approx = next(gen)
    if abs(first_apporx - math.pi) < abs(tenth_approx - math.pi) or \
            abs(tenth_approx - math.pi) < abs(twentyth_approx - math.pi) or \
            abs(twentyth_approx - math.pi) > 0.01:
        print('error in pi_approx_monte_carlo')

    # Q2 c
    gen = leibniz()
    if [next(gen) for i in range(5)] != [1, -1/3, 1/5, -1/7, 1/9]:
        print('error in leibniz')

    gen = infinite_series(powers_of_2())
    if [next(gen) for i in range(6)] != [1, 3, 7, 15, 31, 63]:
        print('error in infinite_series')

    leibniz_formula = [1, -1/3, 1/5, -1/7, 1/9, -1/11, 1/13, -1/15, 1/17, -1/19, 1/21, -1/23, 1/25, -1/27, 1/29]
    leibniz_sum_powers_of_2 = [4*leibniz_formula[0], 4*sum(leibniz_formula[:3]), 4*sum(leibniz_formula[:7]), 4*sum(leibniz_formula[:15])]
    gen = pi_approx_leibniz()
    first_4_sums = [next(gen) for i in range(4)]
    [next(gen) for i in range(5)]
    tenth_approx = next(gen)
    if first_4_sums != leibniz_sum_powers_of_2 or abs(tenth_approx - math.pi) > 1e-3:
        print('error in pi_approx_leibniz')

    # Q2 d
    gen = unit_slicing()
    if [next(gen) for i in range(4)] != [[0.0], [0.0, 0.5], [0.0, 0.25, 0.5, 0.75], [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]]:
        print('error in unit_slicing')

    b = 10
    true_val = math.log(b)
    gen = integral(lambda x: 1 / x, 1, b)
    first_apporx = next(gen)
    [next(gen) for i in range(8)]
    tenth_approx = next(gen)
    [next(gen) for i in range(9)]
    twentyth_approx = next(gen)
    if abs(first_apporx - true_val) < abs(tenth_approx - true_val) or \
            abs(tenth_approx - true_val) < abs(twentyth_approx - true_val) or \
            abs(twentyth_approx - true_val) > 1e-4:
        print('error in integral')

    gen = pi_approx_integral()
    first_apporx = next(gen)
    [next(gen) for i in range(8)]
    tenth_approx = next(gen)
    [next(gen) for i in range(9)]
    twentyth_approx = next(gen)
    if abs(first_apporx - math.pi) < abs(tenth_approx - math.pi) or \
            abs(tenth_approx - math.pi) < abs(twentyth_approx - math.pi) or \
            abs(twentyth_approx - math.pi) > 1e-5:
        print('error in pi_approx_integral')

    ############
    # QUESTION 6
    ############

    # Q6 c
    rule_dict = {"S": {"AB", "BC"}, "A": {"BA", "a"}, "B": {"CC", "b"}, "C": {"AB", "a"}}
    if CYK_d("baaba", rule_dict, "S") != 4:
        print("Error in CYK_d")
    if CYK_d("baab", rule_dict, "S") != -1:
        print("Error in CYK_d")

