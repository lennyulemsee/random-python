#!/usr/bin/python3

with open("text1.txt", 'r') as rf:
    with open("textEven.txt", 'a') as wf:
        with open("textOdd.txt", "a") as w2f:
            for line in rf:
                if "yes" in line:
                    wf.write(line)
                else:
                    w2f.write(line)
