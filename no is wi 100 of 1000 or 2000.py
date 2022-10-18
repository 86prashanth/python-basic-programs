def near_thousand(n):
    return ((abs(1000-n)<=100 or (abs(2000-n)<=200)))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(4000))