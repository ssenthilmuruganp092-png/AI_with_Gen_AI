"""grade_utils.py - helper module for the Student Grade Management System."""

GRADE_SCALE = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (0, "F")]
PASS_MARK = 50


def calculate_average(marks):
    """Return the average of a list of marks (0 if the list is empty)."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def assign_grade(average):
    """Convert an average mark into a letter grade."""
    for cutoff, grade in GRADE_SCALE:
        if average >= cutoff:
            return grade
    return "F"


def get_result(average):
    """Return PASS or FAIL based on the pass mark."""
    return "PASS" if average >= PASS_MARK else "FAIL"


def is_valid_mark(value):
    """A valid mark is a number between 0 and 100."""
    return 0 <= value <= 100