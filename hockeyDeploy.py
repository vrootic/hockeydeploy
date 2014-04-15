import sys
import os

target_project_path = './target'
newproject_name = sys.argv[1]

default_project_path = './DefaultProjectFile'
target_htaccess_path = target_project_path + '/' + newproject_name + '/server/.htaccess'
target_htpasswd_path = target_project_path + '/' + newproject_name + '/server/.htpasswd'

auth_string = [
  'AuthType Basic',
  'AuthName "Project Auth"',
  'AuthUserFile ' + target_project_path + '/' + newproject_name + '/server/.htpasswd',
  'Require valid-user'
]

if os.path.exists(target_project_path) and os.path.exists(default_project_path):

    os.system('cp -r ' + default_project_path + ' ' + target_project_path)
    os.system('mv ' + target_project_path + '/' + 'DefaultProjectFile ' + target_project_path + '/' + newproject_name)
    
    with open(target_htaccess_path, 'a+') as hta:
        hta.write( "\n# Below is auto-generated.\n" + auth_string[0] + "\n")
        hta.write(auth_string[1] + "\n")
        hta.write(auth_string[2] + "\n")
        hta.write(auth_string[3] + "\n")
        
else:
    print 'Fail to generate project'
