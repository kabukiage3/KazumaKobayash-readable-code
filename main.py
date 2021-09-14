#!/bin/python3
import sys
file_path = sys.argv[1]

with open(file_path, 'r') as f:
    lines = f.readlines()
    
    if len(sys.argv) > 2: # 表示したい行目を指定している場合。
        for i in range(2,len(sys.argv)):
            idx = int(sys.argv[i]) # 表示したい行目。 e.g. 2
            line = lines[idx-1].strip("\n")
            print(f"{idx}:{line}")

    elif len(sys.argv) == 2: # 表示したい行目を指定していない場合。
        for idx, line in enumerate(lines):
            line = line.strip("\n")
            print(f"{idx+1}:{line}")