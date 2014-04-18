import os
import sys

project_name = sys.argv[1]
user_name = sys.argv[2]
target_project_path = './target/'

target_htpasswd_path = target_project_path + project_name + '/server/.htpasswd'

if project_name != None and user_name != None:
    os.system("htpasswd " + target_htpasswd_path + " " + user_name)
