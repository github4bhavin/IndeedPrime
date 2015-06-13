__author__ = 'bhavinpatel'


import unittest


from Course import Course


class CourseTest (unittest.TestCase):

    def test_case_1(self):
        inputData = []
        case_1 = open( "Course_case_1.txt", "r")
        output = Course( case_1.readlines() )
        output.showSchedule()

if __name__ == "__main__":
    unittest.main()