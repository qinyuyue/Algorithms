## person show up more than 3 times in one hour
def more3perhour(record):
    """
    Algorithms:
    1. initialize HashMap
        key: name
        value: times
    2. iterate HashMap,
        if len(value) > 3:
            sort and sliding window check
            find the first 1h slot, add to output list
    3. return output

    """
    print("f")
    output = []
    dic = {}
    # set up HashMap
    for row in record:
        name = row[0]
        time = row[1]
        if name in dic:
            dic[name].append(time)
        else:
            dic[name] = [time]
    # iterate HashMap
    for i in dic:

        if len(dic[i]) > 3:
            times = sorted(dic[i])

            l = 0
            r = 3
            while r < len(times)-1:
                if times[r] - times[l] > 100:
                    l += 1

                elif times[r+1] - times[l] > 100:
                    break
                r += 1
            print(times[l:r])
            output.append((i, times[l:r]))
                
    return output

record1 = [('Paul', 1355), ('Jen', 1910), ('Mar', 830), ('Paul', 1315), ('Mar', 835),\
          ('Paul', 1405), ('Paul', 1630), ('Mar', 855), ('Mar', 930), ('Mar', 915), \
          ('Jen', 1335)]


##print("hello")
r = more3perhour(record1)
print(r)
