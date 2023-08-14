# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

class Student:
    def __init__(self, name):
        self.scores = []
        self.name = name
    def add_score(self, score):
        # for score in self.scores: didnt need a for loop
        return self.scores.append(score)
        #unsure about why I need the return statement

    def get_average(self):
        if len(self.scores) == 0:
            return None
        else:
            return sum(self.scores) // len(self.scores)
        # one / returns a float (decimal)
        #two // returns as whole number


student = Student("Malik")


student.add_score(22)
student.add_score(23)
student.add_score(24)
print(student.get_average())
