import unittest
import feladat

from zh_tools import *


class TestOsszead(BaseTest):

    @unittest.skipUnless(checkMethodExists('osszead', 3), 'hianyzo metodus')
    @pont(2)
    def test_egyszeru_osszeadas(self):
        self.assertEqual(feladat.osszead(1, 2, 3), 6, "nem jo")
        self.assertFalse(feladat.osszead(1,1,1) == 4, 'nemtom')

    @unittest.skipUnless(checkMethodExists('osszead', 3), 'hianyzo metodus')
    @pont(1)
    def test_egyszeru_osszeadas2(self):
        self.assertEqual(feladat.osszead(1, 1, -1), 1, "most se jo")
        
    @unittest.skipUnless(checkMethodExists('osszead', 3), 'hianyzo metodus')
    @pont(1)
    def test_egyszeru_osszeadas3(self):
        #raise(ValueError('nagy hiba'))
        pass

class TestErtelmesCucc(BaseTest):

    @classmethod
    def setUpClass(self):
        try:
            self.target = feladat.ertelmesCucc()
        except AttributeError:
            failTest("Hianyzik az osztaly")
        except TypeError:
            failTest("Hibas konstruktor")
        super().setUpClass()

    @unittest.skipUnless(checkMethodExists('csinal', 1), 'hianyzo metodus')
    @pont(3)
    def test_csinal(self):
        self.assertEqual(self.target.csinal(), 4, 'nem jo')

    @unittest.skipUnless(checkMethodExists('__eq__', 2), 'hianyzo metodus')
    @pont(2)
    def test_egyenlo(self):
        masik = feladat.ertelmesCucc()
        self.assertTrue(self.target == masik) 
    