# Author : zhouyun
# 三级菜单，可依次选择进入各子菜单
_dic_a = {'湖北': '黄冈', '湖南': '长沙'}
_dic_b = {'黄冈': '龙感湖', '长沙': '望城坡'}
print('-'*20)
print(' 1、输入1查看所有省份\n 2、输入2查看所有城市\n '
      '3、输入3查看所有县\n 4、输入menu查看菜单\n 5、输入q退出')
print('-' * 20)
while True:
    choose = input('请输入选择内容：')
    if choose == '1':
        print('所有省份:')
        for i in _dic_a:
            print('--', i)
    elif choose == '2':
        print('所有城市:')
        for i in _dic_b:
            print('--', i)
    elif choose == '3':
        print('所有县:')
        for i in _dic_b:
            print('--', _dic_b[i])
    elif choose == 'q':
        break
    elif choose == 'menu':
        print('-' * 20)
        print(' 1、输入1查看所有省份\n 2、输入2查看所有城市\n '
              '3、输入3查看所有县\n 4、输入menu查看菜单\n 5、输入q退出')
        print('-' * 20)
    else:
        print('输入错误，请重新输入,如果想退出,请输入q')
        continue
