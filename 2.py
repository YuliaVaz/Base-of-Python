time = int(input ("Enter the time: "))
hours = time // 3600
time = time % 3600
min = time // 60
sec = time % 60
if (hours<10) :
    print('0', end="")
print(hours, end = ':')
if (min < 10) :
    print('0', end="")
print(min, end = ':')
if (sec < 10) :
    print('0', end="")
print(sec)