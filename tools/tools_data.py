"""
    Helper functions to parse, analyze and print discovered data.

    @author: Alex Bugrimenko
"""
import datetime
from time import time
from dateutil.parser import parse


# ------------ Data Audit -----------
def is_int(v):
    try:
        int(v)
        return True
    except ValueError:
        return False


def is_float(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


def is_date(v):
    try:
        if v is None:
            return None
        v = v.strip()
        return parse(v) is not None
    except ValueError:
        return False


def is_any_numbers(l):
    """ checks if there are at least one number available in the l """
    if l is None or len(l) < 1:
        return False
    res = [x for x in l if x is not None and is_float(x)]    # (is_int(x) or is_float(x))
    return len(res) > 0


def get_type(v):
    v = v.strip()
    if v == 'NULL':
        return type(None)
    elif v == '':
        return type(None)
    elif v.startswith('{'):
        return type([])
    elif is_int(v):
        return type(1)
    elif is_float(v):
        return type(1.1)
    elif is_date(v):
        return type(datetime.datetime)
    else:
        return type("")


def get_date(v):
    try:
        if v is None:
            return None
        v = v.strip()
        return parse(v)
    except ValueError:
        return None


def get_float(v):
    try:
        if v is None:
            return None
        v = v.strip()
        # if v.lower() == 'inf':
        #    return None
        return float(v)
    except ValueError:
        return None


def get_float_advanced(v, multiplier=1):
    """ Gets float value converting K,M,B into numerical values
        multiplier allows additional transformation
    """
    try:
        if v is None:
            return None

        sign = 1
        if v.startswith('(') and v.endswith(')'):
            sign = -1

        v = v.strip(' $%()').lower()
        v = v.replace(',', '')
        if v == 'inf':
            return None

        mult = 1
        if v.endswith('k'):
            mult = 1000
        elif v.endswith('m'):
            mult = 1000000
        elif v.endswith('b'):
            mult = 1000000000
        v = v.strip('kmb')
        f = float(v)
        return f * mult * sign * multiplier
    except ValueError:
        return None


def audit_get_datatype(v, counts):
    """ Gets total counts by discovered data type.
        counts must be a dictionary with the following stucture:
            cnt - total # data elements analyzed
            null - # of discovered null values
            empty - # of discovered empty values
            na - # of discovered n/a values
            array - # of discovered values of type list/array
            zero - # of discovered zero values
    """
    v = v.strip()
    counts['cnt'] += 1
    if v.lower() == 'null':
        counts['null'] += 1
        return type(None)
    elif v == '':
        counts['empty'] += 1
        return type(None)
    elif v.lower() == 'na' or v.lower() == 'n/a' or v.lower() == 'nan':
        counts['na'] += 1
        return type(None)
    elif v.startswith('{'):
        counts['array'] += 1
        return type([])
    elif is_int(v):
        if int(v) == 0:
            counts['zero'] += 1
        return type(1)
    elif is_float(v) or get_float_advanced(v) is not None:
        if get_float_advanced(v) == 0:
            counts['zero'] += 1
        return type(1.1)
    elif len(v) > 4 and is_date(v):
        return type(datetime.datetime)
    else:
        return type("")


def audit_get_counts(data, is_print=True):
    """ Gets counts for each unique value in a data list """
    from collections import defaultdict
    cnts = defaultdict(int)
    for s in data:
        cnts[s] += 1
    if is_print:
        keys = cnts.keys()
        keys = sorted(keys, key=lambda s: s.lower())
        for k in keys:
            print("{0}\t: {1}".format(k, cnts[k]))
    return cnts


def audit_data_describe(data, header, is_print=True):
    """ Describes each data element defined in the header. """
    t0 = time()
    res = {'# rows': len(data)}
    if len(data) == 0:
        return res

    for h in header:
        res[h] = {'type': '', 'cnt': 0, 'null': 0, 'empty': 0, 'na': 0, 'zero': 0,
                  'array': 0, 'min': None, 'max': None}
    for i in range(len(data)):
        for k in header:
            if k in data[i].keys():
                t = audit_get_datatype(str(data[i][k]), res[k])
                if res[k]['type'] == '':
                    res[k]['type'] = t
                try:
                    l = 0
                    if t == type(1) or t == type(1.1):
                        l = get_float_advanced(str(data[i][k]))
                    elif t == type('') or t == type([]):
                        l = len(data[i][k])
                    elif t == type(datetime.date) or t == type(datetime.datetime):
                        l = get_date(str(data[i][k]))
                    if l is None:
                        l = len(data[i][k])
                    if res[k]['min'] is None or res[k]['min'] > l:
                        res[k]['min'] = l
                    if res[k]['max'] is None or res[k]['max'] < l:
                        res[k]['max'] = l
                except:
                    print("ERROR: value is {0}.".format(l))
                    print(res[k])
                    print("Data is {1}.".format(data[i]))
            else:
                audit_get_datatype('', res[k])

    if is_print:
        print('=== Data Audit ===')
        print('--# row(s):', res['# rows'])
        for h in header:
            print('--- [{0}] ({1}) ---'.format(h, res[h]['type']))
            print('cnt:\t', res[h]['cnt'])
            print('null:\t', res[h]['null'])
            print('empty:\t', res[h]['empty'])
            print('n/a:\t', res[h]['na'])
            print('zero:\t', res[h]['zero'])
            print('array:\t', res[h]['array'])
            print('min:\t', res[h]['min'])
            print('max:\t', res[h]['max'])
        print("--+ Data Audit complete in {0} s.".format(round(time() - t0, 3)))
    return res


def audit_list_describe(data, header=None, is_print=True):
    """ Describes each data element in the list. """
    t0 = time()
    res = {'# rows': len(data)}
    if len(data) == 0:
        return res
    if header is None or len(header) == 0:
        # auto populate header with column indices
        if len(data[0]) > 0:
            header = ["Column " + str(x) for x in range(len(data[0]))]
        elif len(data) > 1 and len(data[1]) > 0:
            header = ["Column " + str(x) for x in range(len(data[1]))]
        else:
            raise Exception("Cannot define data header for audit.")

    for h in header:
        res[h] = {'type': '', 'cnt': 0, 'null': 0, 'empty': 0, 'na': 0, 'zero': 0,
                  'array': 0, 'min': None, 'max': None}
    for i in range(len(data)):
        for k, h in enumerate(header):
            if k >= len(data[i]):
                break
            t = audit_get_datatype(str(data[i][k]), res[h])
            if res[h]['type'] == '':
                res[h]['type'] = t
            try:
                l = 0
                if t == type(1) or t == type(1.1):
                    l = get_float_advanced(str(data[i][k]))
                elif t == type('') or t == type([]):
                    l = len(data[i][k])
                elif t == type(datetime.date) or t == type(datetime.datetime):
                    l = get_date(str(data[i][k]))
                if l is None:
                    l = len(data[i][k])
                if res[h]['min'] is None or res[h]['min'] > l:
                    res[h]['min'] = l
                if res[h]['max'] is None or res[h]['max'] < l:
                    res[h]['max'] = l
            except:
                print("ERROR: value is {0}.".format(l))
                print(res[h])
                print("Data is {1}.".format(data[i]))

    if is_print:
        print('=== Data Audit ===')
        print('--# row(s):', res['# rows'])
        for h in header:
            print('--- [{0}] ({1}) ---'.format(h, res[h]['type']))
            print('cnt:\t', res[h]['cnt'])
            print('null:\t', res[h]['null'])
            print('empty:\t', res[h]['empty'])
            print('n/a:\t', res[h]['na'])
            print('zero:\t', res[h]['zero'])
            print('array:\t', res[h]['array'])
            print('min:\t', res[h]['min'])
            print('max:\t', res[h]['max'])
        print("--+ Data Audit complete in {0} s.".format(round(time() - t0, 3)))
    return res


# ------------ Print Helpers -----------
def print_header(data, top_rows=10):
    """ Prints top top_rows rows of the list. """
    if type(data) is list:
        for i in range(top_rows):
            print(data[i])
    else:
        print('print_header:: data must be a list.')
    return


def print_sorted_dict(data, outstream=None):
    """ Sorts dictionary and prints its content.
        outstream allows to print into stream (usually into a text file) instead of screen
    """
    if type(data) is not dict:
        print('print_sorted_dict:: data must be a dictionary.')
        return
    keys = data.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = data[k]
        if outstream is None:
            if is_int(v) or is_float(v):
                print("%s: %d" % (k, v))
            else:
                print("%s:" % k)
                print(v)
        else:
            if is_int(v) or is_float(v):
                outstream.write("%s: %d" % (k, v))
            else:
                outstream.write("%s:" % k)
                outstream.write(v)


def print_sorted_set(data, outstream=None):
    """ Sorts set and prints its content
        outstream allows to print into stream (usually into a text file) instead of screen
    """
    if type(data) is not set:
        print('print_sorted_set:: data must be a set.')
        return
    keys = sorted(data, key=lambda s: s.lower())
    if outstream is None:
        print(", ".join(keys))
    else:
        outstream.write(", ".join(keys))
        outstream.write("\n")


def print_simple(data, outstream=None):
    """ Prints data
        outstream allows to print into stream (usually into a text file) instead of screen
    """
    if outstream is None:
        print(data)
    else:
        outstream.write(data + "\n")


def print_stat(data, stopchar='['):
    """ Groups all strings by substring ended with stopchar
        and shows counts for each distinct substring
    """
    from collections import defaultdict
    if type(data) is not list:
        print('print_stat:: data must be a set.')
        return
    uniq = defaultdict(int)
    for i in range(len(data)):
        ar = data[i].split(stopchar)
        uniq[ar[0]] += 1
    print_sorted_dict(uniq)
    return uniq


# ---------- main calls -------------
if __name__ == "__main__":
    print("~~~ There is no Main method defined. ~~~")
