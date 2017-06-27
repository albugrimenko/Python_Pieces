# -*- coding: utf-8 -*-
"""
    @author: Alex Bugrimenko
"""
import unittest
from tools.log import Log


class TestLog(unittest.TestCase):

    def setUp(self):
        self.log = Log()
        return

    def tearDown(self):
        del self.log
        return

    def test_constructor(self):
        l = Log()
        self.assertIsNotNone(l, "Log")
        self.assertIsNotNone(l.errList, "errList")

    def test_add(self):
        self.log.errList.clear()
        self.assertEqual(0, len(self.log.errList), "len(self.log.errList) before")
        self.log.add("err", "test error")
        self.assertEqual(1, len(self.log.errList), "len(self.log.errList) 1")
        self.log.add("info", "test info")
        self.assertEqual(2, len(self.log.errList), "len(self.log.errList) 2")
        self.log.add("warning", "test warning")
        self.assertEqual(3, len(self.log.errList), "len(self.log.errList) 3")

    def test_add_errlist(self):
        self.log.errList.clear()
        self.assertEqual(0, len(self.log.errList), "len(self.log.errList) before")
        l = ["one", "two", "three"]
        self.log.add_errlist(l)
        self.assertEqual(3, len(self.log.errList), "len(self.log.errList)")


if __name__ == '__main__':
    unittest.main(verbosity=2)
