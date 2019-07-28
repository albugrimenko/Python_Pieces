
""" 2. Recover matrix M based on :
    U - sum of integers in the U (upper) row
    L - sum of integers in the L (lower) row
    C - sum of integers in the K-th column
"""
def solution_02(U, L, C):
    print("--- U: ", U)
    print("--- L: ", L)
    print("--- C: ", C)

    if U + L != sum(C):
        return 'IMPOSSIBLE'

    # all possible choices
    um = [[]]
    lm = [[]]
    for c in C:
        if c == 2:
            add_val(um, 1)
            add_val(lm, 1)
        elif c == 0:
            add_val(um, 0)
            add_val(lm, 0)
        else:
            add_choice(um, lm)

    #print('-- um:\n', um)
    #print('-- lm:\n', lm)

    # solutions
    s = ""
    for i in range(len(um)):
        if sum(um[i]) == U and sum(lm[i]) == L:
            s += get_result(um[i]) + "," + get_result(lm[i]) + ";"

    return s if len(s) > 0 else 'IMPOSSIBLE'

def add_val(ar_list, value):
    for l in ar_list:
        l.append(value)

def add_choice(a, b):
    for i in range(len(a)):
        na = a[i].copy()
        na.append(0)
        a.append(na)
        a[i].append(1)
        nb = b[i].copy()
        nb.append(1)
        b.append(nb)
        b[i].append(0)

def get_result(ar):
    return "".join([str(x) for x in ar])

if __name__ == '__main__':
    print("--+ result: ", solution_02(3, 2, [2, 1, 1, 0, 1]))
    print("--+ result: ", solution_02(2, 3, [0, 0, 1, 1, 2]))
    print("--+ result: ", solution_02(2, 2, [2, 0, 2, 0]))
