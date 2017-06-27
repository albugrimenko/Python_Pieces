"""
    JSON Config accessor

    @author: Alex Bugrimenko
"""
import tools.config as conf
import json


class ConfigJSON(conf.Config):
    """ Config for json config files """

    def __init__(self, filename):
        assert filename, "filename is required."
        conf.Config.__init__(self, filename)

    def load(self):
        """ Loads config file - reads all config parameters """
        self.settings.clear()
        with open(self.filename) as cfg:
            self.settings = json.load(cfg)


# ---------- main calls -------------
if __name__ == "__main__":
    print("~~~ There is no Main method defined. ~~~")
