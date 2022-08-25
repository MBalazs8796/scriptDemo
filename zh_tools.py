import ast

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
                setattr(pont, 'func_values', list())
            pont.func_values.append(
                (func.__name__, p)
            )
            return func
        else:
            return pont.func_values

    return passer