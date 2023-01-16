electrons = int(input())
result = []
saveElectrons = electrons

for i in range(1, saveElectrons + 1):
    formulla = 2 * i ** 2
    if(electrons - formulla >= 0):
        result.append(formulla)
        electrons -= formulla
        if(electrons == 0):
            print(result)
            break
    else:
        result.append(saveElectrons - sum(result))
        print(result)
        break
        