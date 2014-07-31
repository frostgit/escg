#!/usr/bin/env python
#practice with python
import os
import sys
import logging
logging.basicConfig()
logger = logging.getLogger()

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

def create_android_project(android_home,target_folder):
    if(android_home==None): android_home=os.environ.get('ANDROID_HOME')
    if(android_home==None):
        print('please set ANDROID_HOME as an environment variable that points to the android sdk')
        raise Exception('environment variable ANDROID_HOME not set')
        
    android_home = os.path.abspath(android_home)
    target_path = os.path.abspath(target_folder)
    print('ANDROID_HOME is ' + android_home)
    print('target_path is ' + target_path);
    cmd = os.path.join(android_home,'tools/android')
    cmd = cmd + " create project "
    cmd = cmd + method1(target_folder)

    import subprocess
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell = True,
                         cwd=target_path)
    output, errors = p.communicate()
    
    print output
    

def main():
##    args = sys.argv[1:]
    
    exit_value = 1
    try:
        create_android_project(target_folder = '../../projects/client_android',
                               android_home = os.environ.get('ANDROID_HOME'))
    except Exception as exc:
        logger.error(' Exception caught!!! %s - %s', exc.__class__.__name__, exc)
        exit_value = 1
    except BaseException, detail:
        message = ' BaseException caught (but is probably not important)',detail
        logger.info(message)
        print(message)
        exit_value = 1
    else:
        # i could have just put this at the end of the try block and ditch the else block
        # be careful with this... errors doesnt show in the logs... test it with the following
##        print some_foo_bar
##        raise NameError('test error')
        # you need another try block to handle errors within this else block
        exit_value = 0
    finally:
        
        print('finally... end of main')
        print exit_value
        return exit_value

if __name__=='__main__':
    sys.exit(main())
