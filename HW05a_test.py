"""
SSW567 HW 05a
Xueshi Wang
Mock all the data from Github.
2019.2.24
"""
from HW05a import getinfo
from unittest import mock
import unittest
from unittest.mock import patch, Mock
import json

class Testgetinfo(unittest.TestCase):
    """mock the data from Github"""
    @patch('HW05a.requests.get')
    def testgetinfo(self, mockedReq):
        """
        result = [{"name": "hellogitworld"}, {"name": "helloworld"}, {"name": "Mocks"}, {"name": "Project1"}, {"name": "threads-of-life"}]
        mockedReq.return_value.json.return_value = result
        result = getinfo('richkempinski')
        """
        results = list([Mock(),Mock(),Mock(),Mock(),Mock(),Mock()])
        #the {} are used to mock the length in result[1] to result[5]. Get to know this from the above code since it always return length of 5
        results[0].json.return_value = [{"name": "hellogitworld"}, {"name": "helloworld"}, {"name": "Mocks"}, {"name": "Project1"}, {"name": "threads-of-life"}]
        results[1].json.return_value = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        results[2].json.return_value = [{}, {}, {}, {}, {}, {}]
        results[3].json.return_value = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        results[4].json.return_value = [{}, {}]
        results[5].json.return_value = [{}]
        mockedReq.side_effect = results
        result = getinfo('richkempinski')
        self.assertEqual(result, {
            'hellogitworld': 30, 'helloworld': 6, 'Mocks': 9, 'Project1': 2, 'threads-of-life': 1
        })
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
