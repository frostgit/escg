#!/usr/bin/env python
import os
import subprocess

def method1(target_folder):
    ret = ""
    
    target_ID="android-15"
    your_project_name="universal_controller"
    path_to_your_project=target_folder
    your_activity_name="MainActivity"
    your_package_namespace="opa.interactive.uc1"

    ret = ret + " --target " + target_ID
    ret = ret + " --name " + your_project_name
    ret = ret + " --path " + path_to_your_project
    ret = ret + " --activity " + your_activity_name
    ret = ret + " --package " + your_package_namespace

    return ret

def create_android_project(target_folder):
    android_home = os.environ.get('ANDROID_HOME')
    android_home = os.path.abspath(android_home)
    target_path = os.path.abspath(target_folder)
    print('ANDROID_HOME is ' + android_home)
    print('target_path is ' + target_path);
    cmd = os.path.join(android_home,'tools/android')
    cmd = cmd + " create project "
    cmd = cmd + method1(target_folder)
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell = True,
                         cwd=target_path)
    output, errors = p.communicate()
    print output

def main(args):
    create_android_project(target_folder='../../projects/client_android')
    
if __name__=='__main__':
    import sys
    main(sys.argv[1:])
    
