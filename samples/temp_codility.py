

""" 1. BinaryGap: Find longest sequence of zeros in binary representation of an integer.
    32 must give 0, because there is no gaps, there is a single 1 in a binary representation.
"""
def solution_01(N):
    print("--- BinaryGap for {0} ({1:b}):".format(N, N))
    res = 0
    cur = -1 if N % 2 == 0 else 0
    n = N >> 1
    while n > 0:
        if cur > -1 and n % 2 == 0:
            cur = cur + 1
        elif n % 2 == 1:
            if cur > res:
                res = cur
            cur = 0
        n = n >> 1
    return res

""" 2. Arrays: Find value that occurs in odd number of elements. """
def solution_02(A):
    s = set()
    for n in A:
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    return list(s)[0] if len(s) == 1 else 0

""" 3. Rotate an array to the right by a given number of steps. """
def solution_03(A, K):
    if len(A) == 0 or K == 0 or K % len(A) == 0:
        return A
    r = K if K < len(A) else K % len(A)
    res = A[-r:] + A[:(len(A)-r)]
    return res


""" 4. FrogJmp. Count minimal number of jumps from position X to Y."""
def solution_04(X, Y, D):
    return (Y-X)//D + (0 if (Y-X)%D==0 else 1)

""" 5. Find the missing element in a given permutation. """
def solution_05(A):
    a = sorted(A)
    return solution_05_binsearch(a, 0, len(a) - 1)

def solution_05_binsearch(arr, start, end):
    if start < 0: return -1
    if end >= len(arr): return -2

    if start >= end:
        if start < len(arr) and arr[start] == start + 1:
            return start + 2
        else:
            return start + 1
    mid = (start + end) // 2
    if arr[mid] == mid+1:     # right
        return solution_05_binsearch(arr, mid + 1, end)
    else:    # left
        return solution_05_binsearch(arr, start, mid - 1)

def solution_05_bruteforce(A):
    # write your code in Python 3.6
    a = sorted(A)
    for i in range(len(a)):
        if i+1 != a[i]:
            return i+1
    return 1 if len(a) == 0 else len(a)+1

""" 7. Find the smallest positive integer that does not occur in a given sequence
    Values are NOT distinct!
"""
def solution_07(A):
    a = [x for x in A if x > 0]
    if len(a) == 0:
        return 1
    a = sorted(list(set(a)))
    print(a)
    for i in range(len(a)):
        if i+1 != a[i]:
            return i+1
    return 1 if len(a) == 0 else len(a)+1


if __name__ == '__main__':
    #A = [x for x in range(-500, 1000, 1) if x != 354]
    #print(len(A))
    #print(A[-5:])
    #print("--+ result: ", solution_07(A))
    print("--+ result: ", solution_07([1,-1,-2,-100000,45872121,100000,6,4,1,2]))
    #print("--+ result: ", solution_05_bruteforce(A))

    #print("--+ result: ", solution_01(32))
    #print("--+ result: ", solution_02([9,3,9,3,9,7,9]))
    #print("--+ result: ", solution_03([3, 8, 9, 7, 6], 3))
    #print("--+ result: ", solution_04(10, 101, 30))
