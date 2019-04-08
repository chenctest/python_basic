# Author :zhouyun
msg = '\nhello,{name},how are you\n!'
promp = input('name:')
if promp.isdigit() != True:
    print(msg.format_map({'na2me':promp}))
