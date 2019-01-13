N = int(input())
H = [0]*N
S = [0]*N

for i in range(N):
    H[i], S[i] = map(int, input().split())

#N秒後のペナルティを計算し、ペナルティが大きい順に打つ。
#打ったときのペナルティを再計算し、最大値を覚えておく。
def calc_p(h,s,n):
    return (h + s*n)

P = [0]*N
for i in range(N):
    P[i] = -calc_p(H[i],S[i],(N-1))
sorted_index_P = sorted(range(len(P)), key=lambda k: P[k])

max_p = 0
for (k,i) in enumerate(sorted_index_P):
    p = calc_p(H[i], S[i], k)
    if (max_p < p):
        max_p = p
    #print(i, P[i], p)

print(max_p)
