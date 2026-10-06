line = input().split()
n = int(line[0])
K = int(line[1])

adjlst = [[1]]
for i in range(n):
    adjlst.append([])
adjlst[1].append(0)

for i in range(n - 1):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    adjlst[x].append(y)
    adjlst[y].append(x)

def dfs(node, par, adjlst, K):
    conlst = [0] * (K + 1)
    dislst = [0] * (K + 1)
    conlst[0] = 1
    for chld in adjlst[node]:
        if chld != par:
            tcl, tdl = dfs(chld, node, adjlst, K)
            # print(str(tcl))
            # print(str(tdl))
            dislst[0] += tdl[0]
            tcl2 = [0] * (K + 1)
            for i in range(K):
                dislst[i + 1] += tcl[i] + tdl[i + 1]
                tcl2[i + 1] += conlst[i]
            for i in range(K + 1):
                for j in range(K + 1):
                    if i + j <= K:
                        tcl2[i + j] += tcl[i] * conlst[j]
            conlst = list(tcl2)
    return conlst, dislst

conlst, dislst = dfs(1, 0, adjlst, K)
# print(str(conlst))
# print(str(dislst))
ans = sum(conlst) + sum(dislst) + 1
print(str(ans))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna