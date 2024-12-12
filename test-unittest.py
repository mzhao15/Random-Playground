import unittest
from parameterized import parameterized


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("start test class")

    @classmethod
    def tearDownClass(cls):
        print("tear down test class")

    def setUp(self):
        print("start test method")

    def tearDown(self):
        print("tear down test method")


    def test_method_1(self):
        self.assertTrue(1 == 1)

    def test_method_2(self):
        self.assertTrue(1 == 1)


if __name__ == "__main__":
    unittest.main()