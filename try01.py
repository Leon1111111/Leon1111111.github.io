import random

command = int(input("是否開始猜拳? 0.準備猜拳 1.不用了謝謝" ))

c_choice =random.randint(0,2)

if command == 0:
    choice = int(input("請問要猜什麼拳?0.剪刀 1.石頭 2.布"))

    if choice == 0:
        print("你選擇出剪刀")
        if c_choice == 0:
            print("對方選擇出剪刀，雙方平手")
        elif c_choice == 1:
            print("對方選擇出石頭，你不幸輸了")
        elif c_choice == 2:
            print("對方選擇出布，恭喜你贏了")

    elif choice ==1:
        print("你選擇出石頭")
        if c_choice == 0:
            print("對方選擇出剪刀，恭喜你贏了")
        elif c_choice == 1:
            print("對方選擇出石頭，雙方平手")
        elif c_choice == 2:

            print("對方選擇出布，你不幸輸了")

    elif choice ==2:
        print("你選擇出布")
        if c_choice == 0:
            print("對方選擇出剪刀，你不幸輸了")
        elif c_choice == 1:
            print("對方選擇出石頭，恭喜你贏了")
        elif c_choice == 2:
            print("對方選擇出布，雙方平手")

elif command  ==1:
    print("遊戲結束")