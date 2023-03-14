print(
    "Hello! Welcome to the CS 11 Programming Assignment by Samarth Hiremath\n")

#Collect the number of students
numStudents = int(
    input(
        "Enter the number of students (Please enter a value between 1 - 10, inclusive): "
    ))
while ((numStudents < 1 or numStudents > 10)):
    numStudents = int(
        input(
            "Invalid Input: Please enter the number of students between 1 - 10: "
        ))

#Collect the number of tests
numTests = int(
    input(
        "Enter the number of tests (Please enter a value between 1 - 5, inclusive): "
    ))
while ((numTests < 1 or numTests > 5)):
    numTests = int(
        input(
            "Invalid Input: Please enter the number of tests between 1 - 5: "))

print("\nScore Report:")

#Outer loop that iterates through students
for stud in range(1, numStudents + 1):
    total = int(0)
    avg = float(0)

    #Inner loop that iterates through tests
    for test in range(1, numTests + 1):
        score = int(
            input("\nPlease enter the score for Student " + str(stud) +
                  " Test #" + str(test) + ": "))
        total += score

    #Calculate average
    avg = float(total) / numTests

    #Output the ginal values
    print("\nStudent " + str(stud) + ":")
    print("\tTotal Score: " + str(total))
    print("\tAverage Score: " + str(avg))

print("\nDone!")
