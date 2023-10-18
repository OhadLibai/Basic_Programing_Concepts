# Skeleton file for HW4 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include the ID number of the student submitting the solution (hw4_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# The first ID should be the ID of the student submitting the solution
# For example: SUBMISSION_IDS = ["123456000", "987654000"]

############
# QUESTION 2
############

# a
def best_mat_mult_time(L):
    min_list=[]
    return best_mat_mult_time_calc(L, min_list)

def best_mat_mult_time_calc(L, min_list): #no memoization- launching every recursive call a new list of multiplication!
    if len(L)==3:
        min_elem=L[0]*L[1]*L[2]
        min_list.append(min_elem)
        return sum(min_list)

    dynm_list=[]

    for i in range(len(L)-2):
        dynm_list.append(L[i]*L[i+1]*L[i+2])
    min_elem=min(dynm_list)
    for j in range(len(L)-2):
        if L[j]*L[j+1]*L[j+2]== min_elem:
            L.pop(j+1)
            break
    min_list.append(min_elem)

    return best_mat_mult_time_calc(L,min_list)

# b
def best_mat_mult_time_fast(L):
    T= [[0 for x in range(len(L))] for y in range(len(L))]
    i=0
    j= len(L) - 1
    return best_mult_time_fast_calc(L, i, j, T)

def best_mult_time_fast_calc(L, i, j, T):
    if j <= i + 1: #base
        return 0

    min_cand = float('Inf')

    if T[i][j] == 0: #calculation hasn't appeared
        for k in range(i + 1, j):  #take the minimum over each possible position at which the sequence of matrices can be split
            cost = best_mult_time_fast_calc(L, i, k, T)
            cost += best_mult_time_fast_calc(L, k, j, T)
            cost += L[i] * L[k] * L[j]

            if cost < min_cand:
                min_cand = cost

        T[i][j] = min_cand

    return T[i][j]   # return the minimum cost to multiply


# c
def best_mat_mult_order(L):
    return None


def mult_order_to_str(mult_order):
    if type(mult_order) is int:
        return str(mult_order)

    return f"({mult_order_to_str(mult_order[0])}) * ({mult_order_to_str(mult_order[1])})"


############
# QUESTION 3
############

# b
def had_local(n, i, j):
    if n == 0:
        return 0
    two_power = 2 ** (n - 1)
    if i >= two_power and j >= two_power:
        return 1 - had_local(n - 1, i - two_power, j - two_power)
    elif i >= two_power:
        return had_local(n - 1, i - two_power, j)
    elif j >= two_power:
        return had_local(n - 1, i, j - two_power)
    else:
        return had_local(n - 1, i, j)


# d
had_complete = lambda n: [[had_local(n, i, j) for i in range(2 ** n)] for j in range(2 ** n)]


############
# QUESTION 4
############
# To store cell coordinates of the matrix
class Node:
    def __init__(self, first, second):
        self.first = first
        self.second = second

# function that returns false if pt is not a valid position, or it is already visited
def isValid(path, pt, n):
    return 0 <= pt.first < n and 0 <= pt.second < n and \
           not any(x for x in path if x.first == pt.first and x.second == pt.second)

# a
def grid_escape1(B):
    # two possible movements from a cell
    row_1 = [0, 1]
    col_1 = [1, 0]

    path=[]
    source=Node(0,0)
    n=len(B)

    return findPath1(B, path, source, n, row_1, col_1)

def findPath1(B, path, curr, n,row_1,col_1):
    # include current node in the path
    path.append(curr)

    # if the destination is found, return true
    if curr.first == n - 1 and curr.second == n - 1:
        return True

    # get the value of the current cell
    mat_ij = B[curr.first][curr.second]

    # check all two possible movements from the current cell
    # and recur for each valid movement
    for i in range(2):

        # get the next position using the value of the current cell
        x = curr.first + row_1[i] * mat_ij
        y = curr.second + col_1[i] * mat_ij

        next = Node(x, y)

        # check if it is possible to go to a position `(x, y)`
        # from the current position
        if isValid(path, next,n) and findPath1(B, path, next, n,row_1,col_1):
            return True

    # exclude the current cell from the path
    path.pop()
    return False


# b
def grid_escape2(B):
    # all four possible movements from a cell
    row_2 = [-1, 0, 0, 1]
    col_2 = [0, -1, 1, 0]

    path=[]
    source=Node(0,0)
    n=len(B)

    return findPath2(B, path, source, n, row_2, col_2)

def findPath2(B, path, curr, n, row_2, col_2):
    # include current node in the path
    path.append(curr)

    # if the destination is found, return true
    if curr.first == n - 1 and curr.second == n - 1:
        return True

    # get the value of the current cell
    mat_ij = B[curr.first][curr.second]

    # check all four possible movements from the current cell
    # and recur for each valid movement
    for i in range(4):

        # get the next position using the value of the current cell
        x = curr.first + row_2[i] * mat_ij
        y = curr.second + col_2[i] * mat_ij

        next = Node(x, y)

        # check if it is possible to go to a position `(x, y)`
        # from the current position
        if isValid(path, next, n) and findPath2(B, path, next, n, row_2, col_2):
            return True

    # exclude the current cell from the path
    path.pop()
    return False


############
# QUESTION 5
############

# a
def partition(S):
    n=len(S)
    sum_s=sum(S)

    if sum_s%2 == 1: #sum cannot be reached
        return None

    return subset_sum(S, n, sum_s//2)

def subset_sum(S,n, suma):
    if suma == 0:
        return True
    if n == 0:
        return None

    with_last = subset_sum(S, n - 1, suma - S[n - 1])
    without_last = subset_sum(S, n-1, suma)

    if with_last:
        return True
    if without_last:
        return True

    return None


# b
def n_to_k(n,k):
    d={}
    return n_to_k_mem(n,k,d)

def n_to_k_mem(n, k, d):
    if n==k or k==1:
        return 1
    if k>n or k==0 or n==0:
        return 0

    if (n,k) not in d:
        case_1= k * n_to_k_mem(n - 1, k, d) #putting the n'th element in each cell
        case_2 = n_to_k_mem(n - 1, k - 1, d)  # launching new cell with the n'th element
        d[(n, k)]= case_1 + case_2

    return d[(n, k)]


############
# QUESTION 6
############

def distance(s1, s2):
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        return distance(s1[1:], s2[1:])
    else:
        return 1 + min(distance(s1[1:], s2[1:]), distance(s1[1:], s2), distance(s1, s2[1:]))


def distance_fast(s1, s2):
    d = {}
    return distance_mem(s1, s2, d)


def distance_mem(s1, s2, d):
    key = (s1, s2)
    if key in d:
        return d[key]
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        d[key] = distance(s1[1:], s2[1:])
    else:
        d[key] = 1 + min(distance(s1[1:], s2[1:]), distance(s1[1:], s2), distance(s1, s2[1:]))
    return d[key]

