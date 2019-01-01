def main():
	H, W = map(int, input().split())
	S = [list(input()) for _ in range(H)]
 
	D = [[0]*W for j in range(H)]
 
	D[0][0] = 1
	L = [(0,0)]
 
	#黒の数をカウント
	sum_black = 0
	for h in range(H):
		for w in range(W):
			if ('#'==S[h][w]):
				sum_black += 1
 
	for k in range(2,H*W):
		L_next = []
		for l in L:
			w = l[0]
			h = l[1]
			#上
			if (0 < h):
				if ((0 == D[h-1][w]) and ('.'==S[h-1][w])):
					D[h-1][w] = k
					L_next.append((w,h-1))
			#左
			if (0 < w):
				if ((0 == D[h][w-1]) and ('.'==S[h][w-1])):
					D[h][w-1] = k
					L_next.append((w-1,h))
			#下
			if (h < (H - 1)):
				if ((0 == D[h+1][w]) and ('.'==S[h+1][w])):
					D[h+1][w] = k
					L_next.append((w,h+1))
			#右
			if (w < (W - 1)):
				if ((0 == D[h][w+1]) and ('.'==S[h][w+1])):
					D[h][w+1] = k
					L_next.append((w+1,h))
		L = L_next
		if (0 != D[H-1][W-1]):
			break
		if (not L):	#リストが空
			return -1
 
	return W*H - D[H-1][W-1] - sum_black
 
print(main())