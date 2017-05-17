# coding: utf-8
import sys
x = input("式を入力:")
while x != exit:
    if type(x) == int:
        print("答えは" + str(int(x)))
    elif type(x) == float:
        print("答えは" + str(float(x)))
    else:
        pass
    x = input(":")
print("終了します")
sys.exit()
