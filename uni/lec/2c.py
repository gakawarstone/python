ages = {}
ages['anton'] = int(input('anton:'))
ages['boris'] = int(input('boris:'))
ages['victor'] = int(input('victor:'))
for boy in ages:
    if ages[boy] == max(ages.values()):
        print(boy)
