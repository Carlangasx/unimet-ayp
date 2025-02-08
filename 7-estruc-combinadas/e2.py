import typing

def main(): 
    students = [
    {
        "name": "Jose",
        "grade": 16
    },
    {
        "name": "Luis",
        "grade": 17
    },
    {
        "name": "Antonio",
        "grade": 14
    },
    {
        "name": "Gabrielle",
        "grade": 12,
    },
    {
        "name": "Alejandro",
        "grade": 11,
    }
    ]
    grades_sum:int = 0
    grades_prom:int = 0
    for student in students:
        grades_sum += student.get("grade")
    grades_prom:int = grades_sum/ len(students)
    print(grades_prom)

main()
