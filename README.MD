# Logging and Automated Testing

### Name: <Insert Here>

### UCID: <Insert Here>

## Introduction

The purpose of this unit is to introduce you to some basic tools in Python such as automated testing and logging.  
In this unit, you will learn how to write to a log file and test that a file exist using unit
testing.

## Assignment Tasks

For this assignment you need to write 5 unit tests that test the following:

1. Check that each of the 3 default log files are created with the names: errors.log, information.log, and
   root_logger_default.log
2. Make a unit test to check that a message you print into the information log file is correct. Look into python string
   search functions [here](https://www.geeksforgeeks.org/python-string-find/) and how to open a
   file [here](https://www.pythontutorial.net/python-basics/python-read-text-file/)
3. Make a unit test to check that the "logs" folder is created
4. Make a fixture for a test that deletes the log files in the directory, you need to write a test to check this
5. Create a new logger and handler to make a new log for debug information. The file should be called debug.log, and you
   are required to write a test for this.

## Steps to Complete the Assignment

1. Clone the repo, do pip install -r requirements.txt, and then pytest --pylint to see that the tests fail
2. Put your name in the README.MD as indicated above. If you don't do this you will get a 0.
3. Put the 5 assignment task tests in their respective test file i.e. put task 1 in test_task1.py
4. Make sure all the tests pass, do a commit, and push it back to GitHub. Click on the Actions tab and then click on the
   workflows on the left to see the tests run.
5. When you are satisfied submit a link to your repository in the Canvas assignment.

You get 20 points for each task.

### Unit Video - [Watch Here](https://youtu.be/g0IAAD9We9k)
## Required Readings
1. Read this article about software testing [here](https://www.ibm.com/topics/software-testing)
2. Read this article about how automated tests are used at
   Google [here](https://itrevolution.com/case-study-automated-testing-google/)
3. Read this article from Fowler on Continuous Delivery [here](https://martinfowler.com/bliki/ContinuousDelivery.html)
4. Read this article about Devops [here](https://newrelic.com/devops/what-is-devops)
5. Read this article from one of the luminaries in software
   engineering [here](https://martinfowler.com/articles/continuousIntegration.html)  this article is the foundation of
   devops and started the revolution in coding.
6. Read this on AAA testing [here](https://freecontent.manning.com/making-better-unit-tests-part-1-the-aaa-pattern/)

### References and Articles used for Assignment

1. [The article on logging I use for the assignment](https://realpython.com/python-logging/)
2. [TopTotal - Developoer Testing Tutorial on Logging](https://www.toptal.com/python/in-depth-python-logging)
3. [Logging Tutorial in Python - Another one I Used](https://www.loggly.com/ultimate-guide/python-logging-basics/)
4. [Python Logging Handlers Explained](https://docs.python.org/3/library/logging.handlers.html)
5. [Read the documentation on logging from Python](https://docs.python.org/3/library/logging.html)
6. [Pytest - Python Unit Test Framework we Use](https://docs.pytest.org/en/7.1.x/how-to/index.html)
7. [Python File Operations](https://www.programiz.com/python-programming/file-operation)
8. [Python Directory Operations](https://www.journaldev.com/14417/python-directory-create-rename-delete)
9. [Read this article on logging](https://machinelearningmastery.com/logging-in-python/)
10. [Pylint Tutorial - Coding Standards](https://pylint.pycqa.org/en/latest/tutorial.html)
11. [PEP-8 Python Coding Standards](https://realpython.com/python-pep8/)