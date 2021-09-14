#!/bin/python3
import sys
file_path = sys.argv[1]

with open(file_path, 'r', encoding="utf-8") as f:
    lines = f.readlines()
    
    if len(sys.argv) > 2: # 表示したい行目を指定している場合。
        for argidx in range(2,len(sys.argv)):
            idx = int(sys.argv[argidx]) # 表示したい行目。 e.g. 2
            line = lines[idx-1].strip("\n")
            word, word_info = line.split()
            print(f"{idx}: {word} {word_info}")

    elif len(sys.argv) == 2: # 表示したい行目を指定していない場合。
        for idx, line in enumerate(lines):
            line = line.strip("\n")
            word, word_info = line.split()
            print(f"{idx+1}: {word} {word_info}")