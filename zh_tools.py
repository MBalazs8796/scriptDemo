import ast
import multiprocessing
import unittest

def checkMethodExists(name, param_num):
    if not hasattr(checkMethodExists, 'ast'):
        with open("feladat.py", "r", encoding="utf-8") as fp:
                setattr(checkMethodExists, 'ast', ast.parse(fp.read()))

    for node in ast.walk(checkMethodExists.ast):
        if isinstance(node, ast.FunctionDef):
            if node.name == name and len(node.args.args) == param_num:
                return True
    
    return False

def pont(p = 1, shouldDump = False):
    def passer(func):
        if not shouldDump:
            if not hasattr(pont, 'func_values'):
                setattr(pont, 'func_values', dict())
            pont.func_values[func.__name__] = p
            return func
        else:
            return pont.func_values

    return passer

class BaseTest(unittest.TestCase):
    def run(self, result=None):
        self.prevRes = result
        if self.prevRes is None:
            self.prevRes = self.defaultTestResult()
        current_name = self.tests.pop(0)
        p = multiprocessing.Process(target=super().run, args=(self.prevRes, ))
        p.start()
        p.join(self.TIMER)
        if p.is_alive():
            p.terminate()
            p.join()
            self.prevRes.failures.append((current_name, 'Végtelen ciklus\n'))
            self.prevRes.testsRun += 1
            return self.prevRes
        self.prevRes = super().run(self.prevRes)
        return self.prevRes
    
    @classmethod
    def setUpClass(self):
        self.TIMER = 2
        self.prevRes = None
        self.tests = [x for x in dir(self) if x.startswith('test_')]
        