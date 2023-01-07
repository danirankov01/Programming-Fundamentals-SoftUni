n = int(input())
opened = False
closed = False

open = ""
close = ""
for i in range(n):
    line = input()
    if(opened == False and line == ")"):
        print("UNBALANCED")
        break
    if(line == "("):
        opened = True
        open += "("
        if(open == "(("):
            print("UNBALANCED")
            break
    if(line == ")"):
        open = ""
        close = ""
        opened = False
        closed = True
if(opened == False and closed == True):
    print("BALANCED")