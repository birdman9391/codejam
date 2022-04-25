
T = int(input())

for index, t in enumerate(range(T)):
    N, P = [int(num) for num in input().split(" ")]
    D = []
    X = []
    for i in range(N):
        _X = [int(num) for num in input().split(" ")]
        X.append([min(_X), max(_X)])
        
        lenX = X[-1][1] - X[-1][0]
        if i == 0:
            D.append([X[0][0] + 2 * lenX, X[0][0] + lenX])
        else:
            D.append([lenX + min(abs(X[-1][1] - X[-2][0]) + D[-1][0], abs(X[-1][1] - X[-2][1]) + D[-1][1]), lenX + min(abs(X[-1][0] - X[-2][0]) + D[-1][0], abs(X[-1][0] - X[-2][1]) + D[-1][1])])
    print(f"Case #{index+1}: {min(D[-1])}")

