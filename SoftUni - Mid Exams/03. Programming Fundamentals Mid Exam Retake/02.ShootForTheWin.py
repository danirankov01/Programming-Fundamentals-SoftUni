sequence = list(map(int, input().split()))
shotTargets = 0

while(True):
    indices = input()
    if(indices == "End"):
        print(f"Shot targets: {shotTargets} ->", end=" ")
        print(*sequence)
        break

    indices = int(indices)

    if(0 <= indices < len(sequence)):
        if(sequence[indices] != -1):
            shotTargets += 1
            value = sequence[indices]
            sequence[indices] = -1

            for i in range(len(sequence)):
                if(sequence[i] != -1):
                    if(sequence[i] > value):
                        sequence[i] -= value
                    else:
                        sequence[i] += value