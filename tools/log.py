"""
    Basic Logger (simple and not thread safe)

    @author: Alex Bugrimenko
"""
import datetime as dt


class Log:
    """ Log """

    def __init__(self, filename='', is_auto_save=False):
        self.errList = []
        self.fileName = filename
        self.isAutoSave = is_auto_save

    def add(self, severity, msg):
        if msg is None:
            raise Exception("Error message is required.")
        item = {}
        t = dt.datetime.now()
        item["date"] = t.strftime("%Y-%m-%d")
        item["time"] = t.strftime("%H:%M:%S")
        item["severity"] = severity[:3].upper()
        item["msg"] = msg
        self.errList.append(item)
        if self.isAutoSave:
            self.save(filename=self.fileName, is_append=True, is_clear=True)

    def add_errlist(self, errlist):
        if errlist is None or len(errlist) < 1:
            return
        t = dt.datetime.now()
        for i in range(len(errlist)):
            item = {}
            item["date"] = t.strftime("%Y-%m-%d")
            item["time"] = t.strftime("%H:%M:%S")
            item["severity"] = 'ERR'
            item["msg"] = errlist[i]
            self.errList.append(item)
        if self.isAutoSave:
            self.save(filename=self.fileName, is_append=True, is_clear=True)
        return

    def print_all(self):
        for item in self.errList:
            print(item["time"],
                  item["severity"],
                  item["msg"])
        return

    def print_and_log(self, msg, sev='INF', is_print=True):
        if is_print:
            print(msg)
        self.add(severity=sev, msg=msg)
        return

    def save(self, filename, is_append=True, is_clear=True):
        if len(filename) < 1:
            raise Exception("Log file name is required.")
        with open(filename, ('a' if is_append else 'w')) as f:
            for item in self.errList:
                f.write("{0}|{1}|{2}|{3}\n".format(
                    item["date"],
                    item["time"],
                    item["severity"],
                    item["msg"]
                ))
        if is_clear:
            self.errList.clear()
        return
