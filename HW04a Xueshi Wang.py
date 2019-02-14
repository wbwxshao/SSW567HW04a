"""
SSW567 HW 04a
Xueshi Wang
2019/02/14
"""

import requests
import json
import urllib.parse #to join url
import unittest

def getinfo(userid):
    """Given the Github userid and return name of repo and number of commits"""
    github_url = 'https://api.github.com/users/'
    repo = userid + '/repos'
    user_url = urllib.parse.urljoin(github_url, repo)
    r = requests.get(user_url)
    result = json.loads(r.text)
    repo_list = list()
    for i in range(len(result)):
        repo_list.append(result[i]['name'])

    #below is to get commits numbers of each repo
    url_repo = urllib.parse.urljoin('https://api.github.com/repos/', userid)
    number_commits = dict()
    for name in repo_list:
        commit = '/' + name + '/commits'
        commit_url = url_repo + commit
        a = requests.get(commit_url)
        result2 = json.loads(a.text)
        number_commits[name] = len(result2)
    print(number_commits)
    return number_commits

class Testgetinfo(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testgetinfo(self): 
        result = {
            'hellogitworld': 30, 'helloworld': 6, 'Mocks': 9, 'Project1': 2, 'threads-of-life': 1
        }
        self.assertEqual(getinfo('richkempinski'),result)

        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
