import os
import sys
import settings

project_name = settings.PROJECT_NAME
target_path = settings.PROJECT_PATH
bundle_id = settings.ANDROID_BUNDLE_ID
target_path += project_name + "/server/"

if os.path.exists(target_path):
    os.mkdir(target_path + bundle_id + ".android")
