# def test(student, *scores):
#     print("Фамилия студента и его баллы:", student)
#     for score  in scores:
#         print(score)
#
# test("Иванов", 100, 95, 88, 92, 99)

def test_2(student, **scores):
    print("Фамилия студента:", student, "и его баллы:")
    for key, value in scores.items():
        print(key, '=', value)

test_2("Иванов", Информатика=100, Физика=95, Химия=88, История=92, Математика=99)