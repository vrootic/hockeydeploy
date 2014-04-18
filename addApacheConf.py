#!/usr/bin/python
import sys
import settings

project_name = settings.PROJECT_NAME
target_project_path = settings.PROJECT_PATH

target_path = "/etc/apache2/http.conf"
target_path = "./test.txt"

with open(target_path, "a+") as target_file:
    target_file.write("\n")
    target_file.write("<Directory " + project_path + project_name + "/server>\n")
    target_file.write("  Order Deny, Allow\n")
    target_file.write("  AllowOverride all\n")
    target_file.write("  Allow from all\n")
    target_file.write("</Directory>\n")
