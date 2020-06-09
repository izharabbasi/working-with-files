with open("salary.txt", "r") as rf:
    with open("salary1.txt", "a") as wf:
        for line in rf.readlines():
            name, salary = line.split(",")
            wf.write(f"{name} and salary is {salary}\n")
