"""
    @author: Alex Bugrimenko
"""
import unittest
import tools.tools_data as t


class TestToolsData(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_is_int(self):
        self.assertTrue(t.is_int("0"), "0")
        self.assertTrue(t.is_int("1"), "1")
        self.assertTrue(t.is_int("-2"), "-2")
        self.assertTrue(t.is_int("+7"), "+7")
        self.assertFalse(t.is_int("0.1"), "0.1")
        self.assertFalse(t.is_int("1s"), "1s")
        self.assertFalse(t.is_int("1,23."), "1,23.")

    def test_is_float(self):
        self.assertTrue(t.is_float("0.0"), "0.0")
        self.assertTrue(t.is_float("1."), "1.")
        self.assertTrue(t.is_float("-2.1"), "-2.1")
        self.assertTrue(t.is_float("+7.7"), "+7.7")
        self.assertTrue(t.is_float("1"), "1")
        self.assertFalse(t.is_float("1s"), "1s")
        self.assertFalse(t.is_float("1 23"), "1 23")
        self.assertFalse(t.is_float("1,23."), "1,23.")

    def test_is_date(self):
        self.assertTrue(t.is_date("12/8/2016"), "12/8/2016")
        self.assertTrue(t.is_date(" 1-8-2016"), " 1-8-2016")
        self.assertTrue(t.is_date("1.8.2016 "), "1.8.2016")
        self.assertTrue(t.is_date("12/8/2016 12:22"), "12/8/2016 12:22")
        self.assertTrue(t.is_date("12 Aug 2016"), "12 Aug 2016")
        self.assertTrue(t.is_date("12.2016"), "12.2016")
        self.assertFalse(t.is_date("12 asd 2016"), "12 Fri 2016")
        self.assertFalse(t.is_date("asdasd"), "asdasd")

    def test_get_date(self):
        from dateutil.parser import parse
        d = parse("12/8/2016")
        self.assertEquals(d, t.get_date("12/8/2016"), "12/8/2016")
        self.assertEquals(d, t.get_date(" 12-8-2016"), " 12-8-2016")
        self.assertEquals(d, t.get_date("12.8.2016 "), "12.8.2016 ")
        self.assertEquals(d, t.get_date("12/8/2016 00:00"), "12/8/2016 00:00")
        self.assertEquals(d, t.get_date("8 Dec 2016"), "8 Dec 2016")
        self.assertIsNone(t.get_date("12 asd 2016"), "12 asd 2016")
        self.assertIsNone(t.get_date("asdasd"), "asdasd")

    def test_get_float(self):
        self.assertEqual(0., t.get_float("0.0"), "0.0")
        self.assertEqual(1., t.get_float("1."), "1.")
        self.assertEqual(-2.1, t.get_float("-2.1"), "-2.1")
        self.assertEqual(7.7, t.get_float("+7.7"), "+7.7")
        self.assertEqual(1., t.get_float("1"), "1")
        self.assertIsNone(t.get_float("1s"), "1s")
        self.assertIsNone(t.get_float("1 23"), "1 23")
        self.assertIsNone(t.get_float("1,23."), "1,23.")

    def test_get_float_advanced(self):
        self.assertEqual(0., t.get_float_advanced("0.0"), "0.0")
        self.assertEqual(1., t.get_float_advanced("1."), "1.")
        self.assertEqual(-2.1, t.get_float_advanced("-2.1"), "-2.1")
        self.assertEqual(7.7, t.get_float_advanced("+7.7"), "+7.7")
        self.assertEqual(1., t.get_float_advanced("1"), "1")
        self.assertEqual(111215500000., t.get_float_advanced("$111,215.5M"), "$111,215.5M")
        self.assertEqual(4000., t.get_float_advanced("4k"), "4k")
        self.assertEqual(123., t.get_float_advanced("1,23."), "1,23.")
        self.assertIsNone(t.get_float_advanced("1s"), "1s")
        self.assertIsNone(t.get_float_advanced("1 23"), "1 23")

    def test_is_any_numbers(self):
        l = ["asdas", "sssa", "12 3", 'test 121']
        self.assertFalse(t.is_any_numbers(l))
        l.append("22.5")
        self.assertTrue(t.is_any_numbers(l), "22.5")
        l.append("71")
        self.assertTrue(t.is_any_numbers(l), "71")


if __name__ == '__main__':
    unittest.main(verbosity=2)
