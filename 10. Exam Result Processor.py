

marks = list(map(int, input("Enter marks of 5 subjects: ").split()))

if any(mark < 35 for mark in marks):
    print("FAIL")
else:
    average_marks = sum(marks) / 5

    if average_marks >= 75:
        print("DISTINCTION")
    else:
        print("PASS")
