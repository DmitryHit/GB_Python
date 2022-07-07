def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 >= arg1 and arg3 >= arg1:
        return arg2 + arg3
    else:
        return arg1 + arg3


print(my_func(int(input("Первое число: ")), int(input("Второе число: ")),
              int(input("Третье число: "))))
