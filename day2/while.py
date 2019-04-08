# Author :zhouyun
count = 0
while count < 3:
    count += 1
    age = 50
    guess_age = input('age:')
    if guess_age == "":
        print("你输入的为空，请从新输入")
    else:
        guess_age = int(guess_age)
        if guess_age == age:
            print("等于", age)
            break
        elif guess_age > age:
            print("大于", age)
            continue
        else:
            print("小于", age)
            continue
