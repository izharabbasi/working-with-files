from csv import reader

with open("data1.csv", "r") as f:
    data = reader(f)
    next(data)
    for row in data:
        print(row)
