def average(marks): return sum(marks) / len(marks) if marks else 0.0
def grade(avg): return "A" if avg >= 80 else "B" if avg >= 60 else "C"