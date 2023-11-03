import unittest
from GetToken import TestToken
from Operchain import TestOperchain
from Querychian import Testquery
from Value import Testvalue


def test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TestToken))
    suite.addTest(loader.loadTestsFromTestCase(TestOperchain))
    suite.addTest(loader.loadTestsFromTestCase(Testquery))
    suite.addTest(loader.loadTestsFromTestCase(Testvalue))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
