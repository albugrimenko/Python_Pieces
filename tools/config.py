"""
    A simple config file accessor.

    @author: Alex Bugrimenko
"""
import os


class Config:
    """ Config """

    def __init__(self, filename):
        assert filename, "Filename is required."
        if not os.path.isfile(filename):
            raise Exception("Config file is not found: {0}.".format(filename))
        self.settings = {}
        self.filename = filename
        self.load()

    def load(self):
        """ Loads config file - reads all config parameters """
        self.settings.clear()
        return

    def get(self, paramname, default=None):
        """ Gets values of a specified paramaeter name.
            Returns default if parameter is npt found.
        """
        if paramname is None or len(paramname) == 0 \
                or self.settings is None or paramname not in self.settings.keys():
            return default
        else:
            return self.settings[paramname]
