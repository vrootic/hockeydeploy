import sys
import os
import settings

target_project_path = settings.PROJECT_PATH
project_name = settings.PROJECT_NAME

default_project_path = './DefaultProjectFile'
target_htaccess_path = target_project_path + project_name + '/server/.htaccess'
target_htpasswd_path = target_project_path + project_name + '/server/.htpasswd'

auth_string = [
  'AuthType Basic',
  'AuthName "Project Auth"',
  'AuthUserFile ' + target_project_path + project_name + '/server/.htpasswd',
  'Require valid-user'
]

def build_project_directory():
    if os.path.exists(target_project_path) and os.path.exists(default_project_path):
    
        os.system('cp -r ' + default_project_path + ' ' + target_project_path)
        os.system('mv ' + target_project_path + 'DefaultProjectFile ' + target_project_path + project_name)
        
        with open(target_htaccess_path, 'a+') as hta:
            hta.write( "\n# Below is auto-generated.\n" + auth_string[0] + "\n")
            hta.write(auth_string[1] + "\n")
            hta.write(auth_string[2] + "\n")
            hta.write(auth_string[3] + "\n")
        
        return 'successful'
    else:
        return 'Fail to generate project'

if __name__ == '__main__':
    build_project_directory()
