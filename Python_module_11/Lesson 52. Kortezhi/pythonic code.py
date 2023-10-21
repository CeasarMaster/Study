students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer Games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(students):
    lst = []
    string = ''
    id_age = []
    for i in students:
        lst += (students[i]['interests'])
        string += students[i]['surname']
        id_age.append((i, students[i]['age']))
    cnt = 0
    for _ in string:
        cnt += 1
    return lst, cnt, id_age
