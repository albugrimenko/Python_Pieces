import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """ Converts score to grade """
    i = bisect.bisect(breakpoints, score)
    return grades[i]


def ttest_basic():
    print("----- Grades -----")
    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])



if __name__ == "__main__":
    ttest_basic()
