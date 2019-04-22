# Author :zhouyun
menu = {
    '北京':{
        '海淀':{},
    },
    '上海':{
        '闵行':{}
    },
    '山东':{},
}


exit_flag = False
current_layer = menu

layers = [menu]

while not exit_flag:
    for i in current_layer:
        print(i)
    c = input('>>:').strip()
    if c =='b':
        current_layer = layers[-1]
        layers.pop()
        print(layers)
    elif c not in current_layer:
        continue
    else:
        layers.append(current_layer)
        print(layers)
        current_layer = current_layer[c]
