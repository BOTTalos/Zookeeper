# put your python code here
hour_1 = int(input())
minute_1 = int(input())
second_1 = int(input())
hour_2 = int(input())
minute_2 = int(input())
second_2 = int(input())
hour_1 *= 3600
minute_1 *= 60
hour_2 *= 3600
minute_2 *= 60
res_1 = hour_1 + minute_1 + second_1
res_2 = hour_2 + minute_2 + second_2
final = res_2 - res_1
print(final)
