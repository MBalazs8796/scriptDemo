import unittest
import feladat

from zh_tools import *


class TestOsszead(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

    @unittest.skipUnless(checkMethodExists('osszead', 3), 'hianyzo metodus')
    @pont(2)
    def test_egyszeru_osszeadas(self):
        self.assertEqual(feladat.osszead(1, 2, 3), 7, "nem jo")
        self.assertFalse(feladat.osszead(1,1,1) == 3, 'nemtom')

    @unittest.skipUnless(checkMethodExists('osszead', 3), 'hianyzo metodus')
    @pont(100)
    def test_egyszeru_osszeadas2(self):
        self.assertEqual(feladat.osszead(1, 1, -1), 1, "most se jo")

class TestErtelmesCucc(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    @classmethod
    def setUpClass(self):
        try:
            self.target = feladat.ertelmesCucc()
        except AttributeError:
            raise unittest.SkipTest("Hianyzik az osztaly")
        except TypeError:
            raise unittest.SkipTest("Hibas konstruktor")

    @unittest.skipUnless(checkMethodExists('csinal', 1), 'hianyzo metodus')
    @pont(3)
    def test_csinal(self):
        self.assertEqual(self.target.csinal(), 4, 'nem jo')

    @unittest.skipUnless(checkMethodExists('__eq__', 2), 'hianyzo metodus')
    @pont(2)
    def test_egyenlo(self):
        masik = feladat.ertelmesCucc()
        self.assertTrue(self.target == masik) 