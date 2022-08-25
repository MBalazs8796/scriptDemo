import unittest
import robot
import zh_tools

def collector(misses):
    return [(res[0].id().split('.')[-1], res[1]) for res in misses]

def main():
    loader = unittest.TestLoader()
    result = unittest.TestResult()

    issues = list()
    point_sum = 0
    point_achieved = 0
    point_matrix = zh_tools.pont(shouldDump=True)(lambda : 1+1)
    failure_info = list()

   
    if result.skipped:
        failure_info.extend(collector(result.skipped))
    if result.failures:
        failure_info.extend(collector(result.failures))
    
    print(failure_info)

    for name, error_msg in failure_info:
        pass


if __name__ == '__main__':
    main()