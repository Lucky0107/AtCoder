from scipy.sparse import csgraph
 
N,M = map(int, input().split())
 
inf = float('inf')
 
D = [[inf] * N for _ in range(N)]
neighbor1 = []
 
for _ in range(M):
    u,v,l = map(int, input().split())
    if (1 == u):
        neighbor1.append((v,l))
    else:
        D[u-1][v-1] = l
        D[v-1][u-1] = l
 
if (2 <= len(neighbor1)):
#    for k in range(1,N):
#        for i in range(1,N):
#            for j in range(1,N):
#                d = (D[i][k] + D[k][j])
#                if (d < D[i][j]):
#                    D[i][j] = d
    D = csgraph.floyd_warshall(D)
 
    d = inf
    for i,li in neighbor1:
        for j,lj in neighbor1:
            if (i < j):
                tmp = li + lj + D[i-1][j-1]
                if (tmp < d):
                    d = tmp
    if (inf == d):
        print(-1)
    else:
        print(int(d))
else:
    print(-1)