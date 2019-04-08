# Author :zhouyun
item_list = ({"RED_APPLE": 1000}, {"GREEN_ORANGE": 500},
             {"WHITE_PEAR": 100}, {"BLACK_GRAPE": 10})
cart_list = []
at_first = input('please input your salary: ')
flag = True
while(flag):
    print('Welcome to my store:')
    '''打印商品列表'''
    for i in range(0, 4):
        for j in item_list[i]:
            print(i+1, j, item_list[i][j])
    '''逻辑判断商品价格与工资大小'''
    cart_item = input('please input which you want to buy: ')
    for i in item_list[int(cart_item)-1]:
        item_price = item_list[int(cart_item)-1][i]
        if item_price > int(at_first):
            print('your salary is not enough,\nwant to try again?')
        else:
            cart_list.append(item_list[int(cart_item) - 1])
            at_first = int(at_first) - item_price
    '''确认，退出打印商品列表'''
    choose_next = input('please choose y/q/s(确认;退出程序;查看账户余额):')
    if choose_next == 'y':
        continue
    elif choose_next == 'q':
        print('-----购物车里面：---\n %s \n your salary now is %s' % (cart_list, at_first))
        break
    elif choose_next == 's':
        print('your salary now is', at_first)
        continue
    else:
        print('input error')
        continue
