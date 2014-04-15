import os
import sys

project_name = sys.argv[1]
bundle_id = sys.argv[2]
target_path = "./target/"
target_path += project_name + "/server/"

if os.path.exists(target_path):
    os.mkdir(target_path + bundle_id + ".ios")
    os.mkdir(target_path + bundle_id + ".android")
