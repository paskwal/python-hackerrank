# -*- coding: utf-8 -*-
# 
# 

import unittest
import subprocess
import os

# https://docs.python.org/3.7/library/subprocess.html#subprocess.run
# https://docs.python.org/3/library/unittest.html

class AbstractInputOutputTestCase(unittest.TestCase):
    _SCRIPT_NAME = ""
    _TEST_CASES = {}

    def test_cases(self):
        for testcase_in in self._TEST_CASES.keys():
            testcase_out = self._TEST_CASES[testcase_in]
            with open(testcase_in, 'r') as content_file:
                content_in = content_file.read()
            with open(testcase_out, 'r') as content_file:
                expected_out = content_file.read()                
            command_to_exec = "python3 " + self._SCRIPT_NAME
            test_proc = subprocess.run(command_to_exec, input = content_in, shell = True, capture_output = True, text = True)
            self.assertEqual(test_proc.stdout.rstrip(), expected_out.rstrip())
        self.assertTrue(True)   


class Test01ListComprehensions(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "01_list_comprehensions.py"
    _TEST_CASES = {
        "01_testcase_00_in.txt": "01_testcase_00_out.txt",
        "01_testcase_01_in.txt": "01_testcase_01_out.txt",
    }

class Test02FindTheRunnerUp(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "02_find_the_runner-up.py"
    _TEST_CASES = {
        "02_testcase_00_in.txt": "02_testcase_00_out.txt",
    }

class Test03NestedLists(unittest.TestCase):
    _SCRIPT_NAME = "03_nested_lists.py"
    _TEST_CASES = {
        "03_testcase_00_in.txt": "03_testcase_00_out.txt"
        }



class Test04FindingThePercentage(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "04_finding_the_percentage.py"
    _TEST_CASES = {
        "04_testcase_00_in.txt": "04_testcase_00_out.txt",
        "04_testcase_01_in.txt": "04_testcase_01_out.txt"
        }

class Test05Lists(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "05_lists.py"
    _TEST_CASES = {
        "05_testcase_00_in.txt": "05_testcase_00_out.txt"
        }

class Test06Tuples(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "06_tuples.py"
    _TEST_CASES = {
        "06_testcase_00_in.txt": "06_testcase_00_out.txt"
        }


if __name__ == '__main__':
    unittest.main()
