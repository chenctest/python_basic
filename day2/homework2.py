# Author :zhouyun
passport = {'zy': '123456', 'cc': '1234567'}
'''1、用户名和密码保存在字典
   2、用户名和密码正确提示PASS
   3、用户名或者密码错误提示FAIL
   4、只有三次输错密码的机会，第三次输错密码提示'今日已输错3次，该账号已锁定！！！'
   5、输错三次的下次再登录提示该账号已锁定
'''
for i in range(5):
    name = input('please input your name:')

    with open('./locked.txt', 'r+') as f:
        locked = f.read()
    if name == locked:
        print('该账号已被锁定')
    else:
        psw = input('please input your password:')
        if name in passport and psw == passport[name]:
            print('****PASS****')
            break
        else:
            print('----FAIL----')
            if i >= 2:
                print('今日错误已达上限！！！')
                # ./locked.txt代表当前目录下的locked.txt
                with open('./locked.txt', 'w') as f:
                    f.write(name)
                break
            continue
