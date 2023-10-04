n, m = map(int, input().split())
box = [0]*n
temp = 0
# 바구니와 temp함수를 0으로 초기화한다.

for x in range(n):
    box[x]=x+1 #박스: 1번째 박스기 때문에 배열에 1을 더한다.
    
for x in range(m):
    i, j = map(int, input().split())
    temp= box[i-1]
    box[i-1]=box[j-1]
    box[j-1]=temp
    #공을 바꿀 횟수(m)에 바구니를 입력받는다. 
    #하나의 공을 temp라는 변수에 두고 치환한다.ㅇ
    #인덱스는 0부터 시작하기 때문에 첫번째에 접근하려면 -1을 해야한다.
    
for x in range(n):
    print(box[x], end=" ")
    #문제: 1번 바구니부터 n번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.
    #공백으로 구분해 출력한다 => end=" "
    