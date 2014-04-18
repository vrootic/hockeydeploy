import os
import sys
import settings

project_name = settings.PROJECT_NAME
target_project_path = settings.PROJECT_PATH
try:
  user_name = sys.argv[1]
except IndexError:
  print 'Error: No [User_name]. Use `python addUser.py [user_name]` instead'
  sys.exit()

target_htpasswd_path = target_project_path + project_name + '/server/.htpasswd'

if project_name != None and user_name != None:
    os.system("htpasswd " + target_htpasswd_path + " " + user_name)
