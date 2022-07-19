from application import app , manager
from flask_script import Server
import www

#web server
manager.add_command('runserver',Server(host='127.0.0.1',port=app.config["SERVER_PORT"] , use_debugger= True , use_reloader= True))




def main():
    manager.run()

if __name__ == '__main__':
    try:
        import sys
        #执行该语句会直接退出程序，这也是经常使用的方法，也不需要考虑平台等因素的影响，一般是退出Python程序的首选方法
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
