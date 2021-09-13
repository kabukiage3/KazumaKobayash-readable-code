#!/bin/python3

with open('data/sample1.txt', 'r') as f:
    for idx, line in enumerate(f):
        line = line.strip("\n") # 改行記号削除
        print(f"{idx}:{line}")