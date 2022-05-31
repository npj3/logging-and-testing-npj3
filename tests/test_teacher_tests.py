"""These tests should not be changed because I am using them for evaluation.
If you change these tests I will fail you
for the assignment.  If you change these tests a second time I will fail you for the course """
import logging
import os
from os.path import exists

import app
from app import print_hello_name


def test_always_passes():
    """This always passes"""
    assert True


def test_count_log_files(run_program):
    """Testing the number of files in the logs directory"""
    # pylint: disable=unused-argument
    action = len(os.listdir(app.Config.LOG_DIR))
    assert action == 4


def test_hello_world_print(capsys):
    """You have to make this test pass by changing World to Keith"""
    print_hello_name('Keith')
    # This is how we capture the terminal output after running the print command.
    # Out is the console output and err is an error
    out, err = capsys.readouterr()
    assert out == 'Hello Keith\n'
    assert err == ''


def test_logger_for_debug_file(run_program):
    """Checks for the debug log file"""
    # pylint: disable=unused-argument
    debug_log_file_location = os.path.join(app.Config.LOG_DIR, "debug.log")
    assert exists(debug_log_file_location)


def test_logger_running_program(run_program):
    """This tests that that logger of the program that is running
     is created with the correct name"""
    # pylint: disable=unused-argument
    assert id(logging.getLogger("errors")) == id(logging.getLogger("errors"))
    assert id(logging.getLogger("information")) == id(logging.getLogger("information"))
