"""
    Basic functions for data preparation and results analysis in ML.

    A general purpose functions for converting data from the dictionary format to an (n x k) python list that's
    ready for training an sklearn algorithm - sklearn loves to work with numpy arrays.

    n--no. of key-value pairs in dictonary
    k--no. of features being extracted

    Input data file structure:
      - first column is a label
      - last column is a note (will be ignored)
      - everything in a middle are features
    Example: Label,Data,Note

    @author: Alex Bugrimenko
"""
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.preprocessing import StandardScaler
from tools.tools_data import audit_get_counts


def data_split(data, prob):
    """ Splits data into fractions [prob, 1 - prob] """
    import random
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results


def data_train_test_split_simple(features, labels, test_size, is_print=False):
    """ Splits data into training and test sets
        test_pct - percent of data returned in a test array
    """
    data = zip(features, labels)
    train, test = data_split(data, 1 - test_size)
    f_train, l_train = zip(*train)
    f_test, l_test = zip(*test)
    if is_print:
        print("--- Train/test split results ---")
        print("-- # features:", len(features[0]))
        print("-- # items in train:", len(l_train))
        audit_get_counts(l_train, is_print=True)
        print("-- # items in test:", len(l_test))
        audit_get_counts(l_test, is_print=True)
    return f_train, f_test, l_train, l_test


def get_train_test_split(features, labels, test_size=0.3, random_state=0, is_print=False):
    """ Gets rescaled and ready for classifiers data:
        - performs train/test split using specified test_size
        - prints train/test stats if is_print = True
    """
    from sklearn.model_selection import train_test_split

    # get train/test split
    f_train, f_test, l_train, l_test = train_test_split(features, labels,
                                                        test_size=test_size, random_state=random_state)
    if is_print:
        print("--- Train/test split results ---")
        print("-- # features:", len(features[0]))
        print("-- # items in train:", len(l_train))
        audit_get_counts(l_train, is_print=True)
        print("-- # items in test:", len(l_test))
        audit_get_counts(l_test, is_print=True)
    return f_train, f_test, l_train, l_test


def scale_feature(arr):
    """
        Rescales all values within array to be in range [0..1]
        When all values are identical: assign each new feature to 0.5 (halfway between 0.0 and 1.0)
    """
    xmin = min(arr)
    xmax = max(arr)
    res = []
    if xmin == xmax:
        res = [.5 for _ in arr]
    else:
        res = [float((x - xmin)) / (xmax - xmin) for x in arr]
    return res


def data_feature_label_split(data, is_rescale_required=True, is_print=False, is_skip_first=False):
    """
        Separates out the labels, features and notes and put it into separate lists.
        Standardize features by removing the mean and scaling to unit variance when is_rescale_required=True
    """
    labels = []
    features = []
    notes = []
    i = 0
    for item in data:
        # skip the header
        if len(item) == 0 or (i == 0 and is_skip_first):
            i = 1
            continue
        labels.append(item[0])
        features.append(item[1:-1])
        notes.append(item[-1])
    if is_print:
        print("----- Data Feature-Label split -----")
        print("--- # features:", len(features[0]))
        print("--- # samples:", len(features))
        print("--- # samples by label:")
        audit_get_counts(labels, is_print=True)

    if is_rescale_required:
        # rescale to [0..1]
        # scaler = StandardScaler()  # MinMaxScaler()
        # features = scaler.fit_transform(X=features)
        features = scale_feature()
        if is_print:
            print("--+ features have been re-scaled to [0..1]")

    return features, labels, notes


def print_feature_importances(feature_importances):
    cnt = 0
    for i, f in enumerate(feature_importances):
        if f > 0:
            cnt += 1
            print("feature %d (%f)" % (i, f))
    print("Total # features used:", cnt)


def print_feature_importances_top(feature_importances, feature_names=None, top=10):
    if top < 1:
        top = 10
    cnt = 0
    if feature_names is None or len(feature_names) != len(feature_importances):
        feature_names = []
        for i, _ in enumerate(feature_importances):
            feature_names.append("Feature {0}".format(i))
    importances = zip(feature_names, feature_importances)
    importances = sorted(importances, key=lambda x: x[1], reverse=True)
    for i, f in enumerate(importances):
        if f[1] > 0:
            cnt += 1
            if i <= top:
                print("feature %d: [%s] (%f)" % (i, f[0], f[1]))
    print("Total # features used:", cnt)


# ---------- main calls -------------
if __name__ == "__main__":
    print("~~~ There is no Main method defined. ~~~")
