# -*- coding: utf-8 -*-
# 
# (c) @paskwal, 2019

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
            with self.subTest(testcase_in=testcase_in):
                self.assertEqual(test_proc.stdout.rstrip(), expected_out.rstrip())
#            self.test_command(stdout = test_proc.stdout, expected =expected_out)
        self.assertTrue(True)   

#    def test_command(self, stdout, expected):
#        self.assertEqual(stdout.rstrip(), expected.rstrip())



class Test01(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "01_defaultdict.py"
    _TEST_CASES = {
        "01_testcase_00_in.txt": "01_testcase_00_out.txt",
        "01_testcase_01_in.txt": "01_testcase_01_out.txt",
        "01_testcase_02_in.txt": "01_testcase_02_out.txt",
        "01_testcase_03_in.txt": "01_testcase_03_out.txt"
    }

class Test02(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "02_named_tuples.py"
    _TEST_CASES = {
        "02_testcase_00_in.txt": "02_testcase_00_out.txt",
        "02_testcase_01_in.txt": "02_testcase_01_out.txt"
    }

class Test03(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "03_ordereddict.py"
    _TEST_CASES = {
        "03_testcase_00_in.txt": "03_testcase_00_out.txt"
    }

class Test06(AbstractInputOutputTestCase):
    _SCRIPT_NAME = "06_piling_up.py"
    _TEST_CASES = {
        "06_testcase_00_in.txt": "06_testcase_00_out.txt",
        "06_testcase_01_in.txt": "06_testcase_01_out.txt",
        "06_testcase_02_in.txt": "06_testcase_02_out.txt",
        "06_testcase_03_in.txt": "06_testcase_03_out.txt"
    }

if __name__ == '__main__':
    unittest.main()
