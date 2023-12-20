#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Введите слово: ")
    letters = set()
    count = 0
    
    for i in word:
        if i in letters:
            count += 1
            i_repeat = i
        else:
            letters.add(i)
            
    if count == 1:
        print(f"В слове только две повторяющиеся буквы {i_repeat}.")
    elif count > 1:
        print("В слове больше двух повторяющихся букв.")
    else:
        print("В слове нет повторяющихся букв.")