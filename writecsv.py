from csv import writer

with open("data.csv", "a") as f:
    data = writer(f)
    data.writerow(["name", "country"])
    data.writerow(["izhar", "pak"])
    data.writerow(["tom", "usa"])
    data.writerow(["meto", "aus"])
