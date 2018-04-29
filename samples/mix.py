from time import time
import bisect

IS_DEBUG = True

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """ Converts score to grade """
    i = bisect.bisect(breakpoints, score)
    return grades[i]


def ttest_basic():
    print("----- Grades -----")
    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])


def merge(list_a, list_b, order="agony"):
    """ Merges two lists into one, preserving defined order.
        IMPORTANT: both lists must be sorted by [order]!
    """
    # assert list_a is not None, "list_a is None."
    # assert list_b is not None, "list_b is None."
    if IS_DEBUG:
        print('-- Merge 2 lists ({0} + {1}).'
              .format(len(list_a) if list_a is not None else 0,
                      len(list_b) if list_b is not None else 0))

    if list_a is None or len(list_a) == 0:
        return list_b
    if list_b is None or len(list_b) == 0:
        return list_a

    t0 = time()
    res = []
    # find shorter list
    if len(list_a) <= len(list_b):
        short = list_a
        long = list_b
    else:
        short = list_b
        long = list_a

    # external cycle by shorter list
    j = 0
    j_max = len(long)
    for i in range(len(short)):
        while j < j_max and long[j][order] < short[i][order]:
            res.append(long[j])
            j += 1
        res.append(short[i])
    # finish long list
    if j < j_max:
        res.extend(long[j:])

    if IS_DEBUG:
        print('-+ Merge complete in {0} sec. Total len is {1}.'.format(round(time() - t0, 4), len(res)))

    return res

@staticmethod
def merge_many(lists, order="agony"):
    """ Merges all lists in the one, preserving defined order.
        IMPORTANT: both lists must be sorted by [order]!
    """
    assert lists is not None, "lists is None"
    if len(lists) == 0:
        return []
    if len(lists) == 1:
        return lists[0]

    res = FlightsSearch.merge(lists[0], lists[1], order)
    for i in range(2, len(lists)):
        res = FlightsSearch.merge(res, lists[i], order)

    return res

if __name__ == "__main__":
    ttest_basic()
