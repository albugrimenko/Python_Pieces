"""
    @author: Alex Bugrimenko
"""
import unittest
from tools.config_json import ConfigJSON

CfgFileName = "config_test.json"
CfgFileName_empty = "config_test_empty.json"


class TestConfigJSON(unittest.TestCase):

    def setUp(self):
        self.cnf = ConfigJSON(CfgFileName)
        return

    def tearDown(self):
        del self.cnf
        return

    def test_constructor(self):
        self.assertIsNotNone(self.cnf, "config")
        self.assertIsNotNone(self.cnf.settings, "config.settings")

    def test_constructor_empty_file(self):
        c = ConfigJSON(CfgFileName_empty)
        self.assertIsNotNone(c, "config_empty")
        self.assertIsNotNone(c.settings, "config_empty.settings")
        self.assertEqual(0, len(c.settings), "config_empty.settings")

    def test_settings(self):
        self.assertIsNotNone(self.cnf.settings, "config.settings")
        self.assertTrue(len(self.cnf.settings), "config.settings.len")

    def test_settings_get_none(self):
        a = self.cnf.get("abc", None)
        self.assertIsNone(a, "config.get_none")
        a = self.cnf.get("abc", "test")
        self.assertEqual("test", a, "config.get_none_def")

    def test_settings_get(self):
        a = self.cnf.get("test", None)
        self.assertEqual("TEST", a, "config.get")


if __name__ == '__main__':
    unittest.main(verbosity=2)
