# 실습문제 5.2.2
data = []
data.append(int(input("1일차 턱걸이 횟수 >>>")))
data.append(int(input("2일차 턱걸이 횟수 >>>")))
data.append(int(input("3일차 턱걸이 횟수 >>>")))
data.append(int(input("4일차 턱걸이 횟수 >>>")))
data.append(int(input("5일차 턱걸이 횟수 >>>")))
data.append(int(input("6일차 턱걸이 횟수 >>>")))
data.append(int(input("7일차 턱걸이 횟수 >>>")))

avg = (data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]) / 7
print(int(avg))