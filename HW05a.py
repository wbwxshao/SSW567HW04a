"""
SSW567 HW 05a
Xueshi Wang
"""

import requests
import json

def getinfo(userid):
    """Given the Github userid and return name of repo and number of commits"""
    github_url = 'https://api.github.com/users/'
    repo = userid + '/repos'
    #user_url = urllib.parse.urljoin(github_url, repo)
    user_url = github_url + repo
    r = requests.get(user_url)
    result = r.json()
    repo_list = list()
    for i in range(len(result)):
        repo_list.append(result[i]['name'])

    #below is to get commits numbers of each repo
    #url_repo = urllib.parse.urljoin('https://api.github.com/repos/', userid)
    url_repo = 'https://api.github.com/repos/' + userid
    number_commits = dict()
    for name in repo_list:
        commit = '/' + name + '/commits'
        commit_url = url_repo + commit
        a = requests.get(commit_url)
        result2 = a.json()
        number_commits[name] = len(result2)
    return number_commits

