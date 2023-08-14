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
# There is pseudocode for you to guide you.


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
        # self.add_score(score) = add_score(score)
        # self.get_average() = get_average()
    def add_score(self, score):
        self.scores.append(score)

    def get_average(self, scores):
        if len(self.scores) == 0:
            return None
        else:
            return sum(self.scores) // len(self.scores)
