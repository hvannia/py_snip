from bisect import bisect

def grade(score, breakpoints=[60,70,80,90], grades = ['F','D','C','B','A']):
    i = bisect(breakpoints, score)
    return grades[i]

[grade(score) for score in [33,99,77,70,89,90,100]]