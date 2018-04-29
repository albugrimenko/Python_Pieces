import time


def progressbar_textmode():
    """ Anymated progress bar """
    from tqdm import tqdm
    for i in tqdm(range(1000)):
        time.sleep(.01)


if __name__ == "__main__":
    progressbar_textmode()