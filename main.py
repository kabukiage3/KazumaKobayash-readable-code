#!/bin/python3
import sys
file_path = sys.argv[1]

with open(file_path, 'r', encoding="utf-8") as f:
    lines = f.readlines()
    
    if len(sys.argv) > 2: # 行数指定あり
        for argidx in range(2,len(sys.argv)):
            idx = int(sys.argv[argidx]) # 指定行数
            line = lines[idx-1].strip("\n")
            word, word_info = line.split() # 単語情報, 読みがな
            print(f"{idx}: {word} {word_info}") 

    elif len(sys.argv) == 2: # 行数指定なし
        for idx, line in enumerate(lines):
            line = line.strip("\n")
            word, word_info = line.split() # 単語情報, 読みがな
            print(f"{idx+1}: {word} {word_info}")
