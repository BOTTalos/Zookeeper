number_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())
max_ = number_of_halls * capacity
res = max_ >= number_of_viewers
print(res)
