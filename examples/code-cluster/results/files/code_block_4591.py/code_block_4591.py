for i in file.groupby("Month").count().index:
    s = 'Month' + str(i)
    a = []
    for j in file.Month:
        if j==i:
            a.append(1)
        else:
            a.append(0)
    file[s] = a
file.sample(5)'