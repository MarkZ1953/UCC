def formal():
    with open("TestCases/test_cases1.txt") as fp:
        lines = [line.rstrip() for line in fp]
        print(lines)
        for data in lines:
            print(f"{data}")

formal()