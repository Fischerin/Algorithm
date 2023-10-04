n, m = map(int, input().split())
box=[0]*(n+1) # n개의 바구니를 초기화한 배열을 만든다. 
# 배열이 0부터 시작이므로 1을 더한다. 

for _ in range(m):
    i, j, k = map(int, input().split()) #m번 동안 i,j,k를 입력받는다.
    for x in range(i, j+1):
        box[x-1]=k #리스트값 갱신을 위해 추가 실행 i~j번의 바구니에 k의 공을 넣는다.
        # 바구니는 1번부터지만 인덱스는 0부터 시작하므로 1을 빼준다.

for i in range(n):
    print(box[i], end=' ')
    
    