# coding: utf-8
import sys
x = input("式を入力:")
while x != "exit":
    x = eval(x)
    print("答えは、" + str(x))
    x = input("式を入力:")
print("終了します")
sys.exit()
