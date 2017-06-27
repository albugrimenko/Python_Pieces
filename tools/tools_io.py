"""
    Helper functions for file operations and command mode.

    @author: Alex Bugrimenko
"""
import os


# --- interactive (UI)
def ui_is_continue():
    """ Asks if user wants to continue and return a boolean. """
    conf = input('\n=> Do you want to continue? [y/n]:')
    return conf in ["y", "Y"]


# ----------- File operations -----------------
def save_to_file(filename, data, is_print=False):
    """ saves data to text file """
    with open(filename, 'w', encoding='utf-8') as fout:
        if type(data) is list:
            fout.write("\n".join(data))
        else:
            fout.write(data)
    if is_print:
        print('--- Saved data to: ', filename)
    return


def file_rename(filename, is_add_suffix=True, suffix='_bak', is_auto_replace=True):
    """ Renames specified file by adding or removing a suffix """
    if len(suffix) < 1:
        suffix = '_bak'
    if os.path.isfile(filename):
        fn, file_ext = os.path.splitext(filename)
        if is_add_suffix:
            fn = fn + suffix + file_ext
        else:
            fn = fn.replace(suffix, '') + file_ext
        if is_auto_replace and os.path.isfile(fn):
            os.remove(fn)
        os.rename(filename, fn)
    else:
        print('WARNING: cannot find file to rename:', filename)


def file_get_uniq_name(filename, max_iter=1000):
    """ Gets unique file name by adding number to the end of the file
        If unique file name cannot be found, it returns an empty string
    """
    i = 1
    nfn = filename
    fn, file_ext = os.path.splitext(filename)
    while i < max_iter and os.path.isfile(nfn):
        nfn = "{0}_{1}{2}".format(fn, i, file_ext)
        i += 1
    return "" if i >= max_iter else nfn


# ------------ CSV files ------------
def parse_csv_dict(filename):
    """ Parses csv file and returns header columns and data. """
    import csv
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    return reader.fieldnames, data


# ---------- main calls -------------
if __name__ == "__main__":
    print("~~~ There is no Main method defined. ~~~")
