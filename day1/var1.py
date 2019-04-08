name = input("please input your name:")
psw = input('password:')
info1 = '''
-----%sinfo---
name : %s
psw  : %s
-----------------
''' % (name, name, psw)
info2 = '''
-----{0}info---
name : {0}
psw  : {1}
-----------------
'''.format(name, psw)
info3 = '''
-----{_name}info---
name : {_name}
psw  : {_psw}
-----------------
'''.format(_name=name, _psw=psw)
print(info1)
print(info2)
print(info3)
