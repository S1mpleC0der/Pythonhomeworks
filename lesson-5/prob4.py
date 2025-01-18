universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = [univ[1] for univ in universities]
    tuitions = [univ[2] for univ in universities]
    return students, tuitions

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]


students, tuitions = enrollment_stats(universities)
print("******************************")
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuitions):,}")
print()
print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,.0f}")
print()
print(f"Tuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {median(tuitions):,.0f}")
print("******************************")
