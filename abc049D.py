N,K,L = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(K)]
T = [list(map(int, input().split())) for _ in range(L)]

#print(N,K,L,D,T)

list_D = [set([i]) for i in range(N)]
list_T = [set([i]) for i in range(N)]
root_D = [i for i in range(N)]
root_T = [i for i in range(N)]

#print(list_D)

for d in D:
    d0 = d[0] - 1
    d1 = d[1] - 1
    r0 = root_D[d0]
    r1 = root_D[d1]
    list_D[r0] = list_D[r0] | list_D[r1]
    root_D[r1] = r0
    root_D[d1] = r0
    #print(list_D, root_D)

for t in T:
    t0 = t[0] - 1
    t1 = t[1] - 1
    r0 = root_T[t0]
    r1 = root_T[t1]
    list_T[r0] = list_T[r0] | list_T[r1]
    root_T[r1] = r0
    root_T[t1] = r0
    #print(list_T, root_T)

#和集合
res = [0] * N
for i in range(N):
    rd = root_D[i]
    rt = root_T[i]
    d = list_D[rd]
    t = list_T[rt]
    res[i] = len(d & t)
#print(*(res[i] for i in range(N)))
print(" ".join([str(i) for i in res]))