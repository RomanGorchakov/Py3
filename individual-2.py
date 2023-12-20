#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input("Введите последовательность символов: ")
    count = 1

    for i in range(len(s)):
        if s[i:(i+1)] == s[(i+1):(i+2)]:
            count += 1

    if count == (len(s)):
        print("Все символы последовательности одинаковые.")
    else:
        print("Не все символы последовательности одинаковые.")
        
    print(count)