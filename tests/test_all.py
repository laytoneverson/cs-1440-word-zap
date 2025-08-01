"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

from test_player_init import TestPlayerInit
from test_player_getName import TestPlayerGetName
from test_player_getLetters import TestPlayerGetLetters
from test_player_drawLetter import TestPlayerDrawLetter
from test_player_printLetters import TestPlayerPrintLetters
from test_player_checkWord import TestPlayerCheckWord
from test_main import TestMain

if __name__ == '__main__':
    testCases = [
        TestPlayerInit,
        TestPlayerGetName,
        TestPlayerGetLetters,
        TestPlayerDrawLetter,
        TestPlayerPrintLetters,
        TestPlayerCheckWord,
        TestMain
    ]

    allTests = []
    for testCase in testCases:
        allTests.append(unittest.TestLoader().loadTestsFromTestCase(testCase))

    unittest.TextTestRunner().run(unittest.TestSuite(allTests))
