import unittest
import zh_tools
import builtins
import ast

def collector(misses):
    info = dict()
    for missed_test in misses:
        missed_name = str(missed_test[0]).split(' ')[0].split('.')[-1]
        error_msg = missed_test[1].split('\n')[-2]
        
        info[missed_name] = error_msg
    return info

def speak(name, value, success, reason=''):
    processed_name = ' '.join(name.split('_')[1:])
    if success:
        print(f'{processed_name} {value}/{value}: pont ✓')
    else:
        print(f'{processed_name} {0}/{value}: pont ✗')
        print(f'ok: {reason}')

def main():
    builtins.input = lambda *arg, **kwargs: zh_tools.failTest('A feladat megoldasahoz az input hasznalata nem szukseges!')
    builtins.eval = lambda *arg, **kwargs: zh_tools.failTest('A feladat megoldasahoz az eval hasznalata nem szukseges!')
    ALLOWED_MODULES = ['__main__']
    try:
        import robot
    except ModuleNotFoundError as e:
        print('A beadott megoldás helytelen formátumú a beadott fájl neve feladat.py kell legyen!')
        return
    except BaseException as e:
        print(f'A megoldás értelmezés során az alábbi hibába ütközik: {e}')
        return
        
    with open("feladat.py", "r", encoding="utf-8") as fp:
        for node in ast.walk(ast.parse(fp.read())):
            if isinstance(node, ast.Import):
                for name in node.names:
                    if name.name not in ALLOWED_MODULES:
                        print(f'Tiltott modult használsz! ({name.name})')
                        return
            
            if isinstance(node, ast.ImportFrom):
                if node.module not in ALLOWED_MODULES:
                    print(f'Tiltott modult használsz! ({node.module})')
                    return
            
            if isinstance(node, ast.Expr):
                if node.value.func.id == 'exec':
                    print('A feladat megoldasahoz az exec hasznalata nem szukseges!')
                    return
            


    
    loader = unittest.TestLoader()
    result = unittest.TestResult()


    FULL = '█'
    EMPTY = '░'

    point_sum = 0
    point_lost = 0
    point_matrix = zh_tools.pont(shouldDump=True)(lambda : 1+1)
    failure_info = dict()
    every_test = dict()

    robotTestSuits = loader.loadTestsFromModule(robot)
    
    for testSuit in robotTestSuits:
        for test in testSuit:
            test_name, suite_name = str(test).split(' ')
            if suite_name not in every_test:
                every_test[suite_name] = list()
            every_test[suite_name].append(test_name)
    robotTestSuits.run(result)

    if result.errors:
        failure_info.update(collector(result.errors))
        
    if result.failures:
        failure_info.update(collector(result.failures))
    
    for skip in result.skipped:
        errorHolder, msg = skip
        test_name = errorHolder.id().split(' ')[0].split('.')[-1]
        if test_name == 'setUpClass':
            for test_name in every_test[errorHolder.id().split(' ')[-1]]:
                failure_info[test_name] = msg
        else:
            failure_info[test_name] = msg
    
    for suite_name, tests in every_test.items():
        printed_name = suite_name.split('Test')[-1][:-1]
        print(f'A(z) {printed_name} tesztjeinek eredménye az alábbi:\n')
        for func_name in tests:
            value = point_matrix[func_name]
            point_sum += value
            if func_name in failure_info:
                point_lost += value
                speak(func_name, value, False, failure_info[func_name])
            else:
                speak(func_name, value, True)
    
    print()        
    print(f'{point_sum-point_lost}/{point_sum} pont')
    print(FULL*(point_sum-point_lost) + EMPTY*(point_lost))
    


if __name__ == '__main__':
    main()
    