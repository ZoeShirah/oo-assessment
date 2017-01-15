"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   a. Abstraction:
        We don't have to know how everything works to put it together, easier to
        think about each level of complexity one at a time.
   b. Encapsulation:
        All the information about something is kept together in one place, like 
        an even more complete dictionary.
   c. Polymorphism:
        An object may come in many different types, but they can all be accessed
        the same way.


2. What is a class?
        A class is a collection of attributes and methods that define an object,
        it is a data structure similar to a dictionary but with greater capabilities.

3. What is an instance attribute?
        An instance attribute is an attribute that only exists on one instance of
        a class, not on every instance.

4. What is a method?
        A method is a function that is defined inside a class.

5. What is an instance in object orientation?
        An instance is an object -- it is a specific implementation of a class.
        Everytime a class is created and used it creates an "instance" of that class.
        Anything that is changed in that instance is specific to that instance and
        does not change the class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
        A class attribute is available to all instances of that class, but an
        instance attribute is only in that instance.  One might define a class
        attribute if it is relevant to all instances of that class, like that
        all Dogs can speak, but define an instance attribute if it is relevant
        only to that instance, like only this one Dog can also howl.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):

    def __init__(self, first, last, address):
        self.first_name = first
        self.last_name = last
        self.address = address


class Question(object):

    def __init__(self, question, answer):
        self.question = question
        self.correct_answer = answer

    def ask_and_evaluate(self):
        """asks a question, takes user input answer, and returns True if
        the answer matches the correct_answer, False if it doesn't"""

        answer = raw_input(self.question + " > ")
        if answer == self.correct_answer:
            return True

        return False


class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        """gets a question and correct answer, creates a Question object, and
        adds it to the list of questions"""

        new_question = Question(question, answer)
        self.questions.append(new_question)

    def administer(self):
        """asks all the questions in the list, gets answers, and returns the
        percentage score"""

        score = 0
        for q in self.questions:
            if q.ask_and_evaluate():
                score += 1

        return float(score)/float(len(self.questions))


def take_test(exam, student):
    """administers an exam, then adds the score to the student instance"""

    score = exam.administer()

    if type(score) == bool:
        if score:
            print "PASS"
        else:
            print "FAIL"
    else:
        print "Score: {:.2f}".format(score)

    student.score = score


def example():
    """an example run of taking a test"""

    #create an exam and add questions
    exam = Exam("Midterm")
    exam.add_question("What is 2 + 2?", "4")
    exam.add_question("What is '2'+'2'?", "22")
    exam.add_question("What is an instance?", "an object")

    #creates an instance of student
    student = Student("Jane", "Smith", "100 Irving St")

    #take test
    take_test(exam, student)


class Quiz(Exam):

    def administer(self):
        score = super(Quiz, self).administer()

        #if fewer that half the questions were answered correct, return false
        if score < 0.5:
            return False
        else:
            return True


def quiz_example():
    """an example run of taking a quiz"""

    #create an exam and add questions
    quiz = Quiz("Quiz 1")
    quiz.add_question("What is 2 + 2?", "4")
    quiz.add_question("What is '2'+'2'?", "22")
    quiz.add_question("What is an instance?", "an object")

    #creates an instance of student
    student = Student("Jane", "Smith", "100 Irving St")

    #take test
    take_test(quiz, student)
