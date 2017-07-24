# hockeydeploy
Use HockeyKit to deploy on Ubuntu/Linux server in order to build a testflight-like service


Target User: Engineer

* Prerequisite:

1. Script files in this project must be applied on Linus-based server.

2. Python2.7



* Step of building project:

1. Build Hockey Project
  * Set up [project-name] folder
  * Set up file directory in Apache http.conf to set up server file location on server
  * Target platforms are iOS/Android
2. Set up parameter for PROJECT_NAME and PROJECT_PATH in settings.py

3. Use `pytho hockeyDeploy.py` to build folder that required in (1)
