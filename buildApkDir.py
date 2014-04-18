import os
import sys
import settings

project_name = settings.PROJECT_NAME
target_path = settings.PROJECT_PATH
try:
  bundle_id = sys.argv[1]
except IndexError:
  print "Error: No [Bundle_id]. Use `python buildApk.py [bundle_id]` instead"
  sys.exit()
target_path += project_name + "/server/"

if os.path.exists(target_path):
    os.mkdir(target_path + bundle_id + ".android")
