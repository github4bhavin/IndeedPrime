__author__ = 'bhavinpatel'

import unittest

from WaversFlight import ClockTower

class WaversFlightTest(unittest.TestCase):

    def test_case_1(self):
        inputData = []

        case_1 = open( "case_1.txt", "r")
        output = ClockTower( case_1.readlines() )
        print output
        pass


if __name__ == "__main__":
    unittest.main()