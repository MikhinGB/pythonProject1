import csv

def write_holiday_cities(first_letter):
    with open('travel_notes.csv', 'r') as file:
        reader = csv.reader(file)
        matrix = []
        for row in reader:
            row_lst = list(row)
            matrix.append(row_lst)
    # используя СПИСКОВЫЕ ВКЛЮЧЕНИЯ, собираем значения столбца 2 (города, где побывали)
    have_visited = [row[1].split(';') for row in matrix if row[0][0] == first_letter]
    h_visited = []
    for i in range(0, len(have_visited)):
        h_visited += have_visited[i]
    h_visited = set(h_visited)   # преобразуем во множество, дабы избежать повтора

    # используя СПИСКОВЫЕ ВКЛЮЧЕНИЯ, собираем значения столбца 3 (города, где хотят побывать)
    wants_to_visit = [row[2].split(';') for row in matrix if row[0][0] == first_letter]
    w_to_visit = []
    for i in range(0, len(wants_to_visit)):
        w_to_visit += wants_to_visit[i]
    w_to_visit = set(w_to_visit)   # преобразуем во множество, дабы избежать повтора

    uniq_wants = w_to_visit - h_visited  # находим разность множеств, т.е. элементы первого множества, которых нет
                                         # во втором 

    h_visited = list(h_visited)
    w_to_visit = list(w_to_visit)
    uniq_wants = list(uniq_wants)

    h_visited.sort()
    w_to_visit.sort()
    uniq_wants.sort()

    h_visited.insert(0, 'Побывали:')
    w_to_visit.insert(0, 'Хотят побывать:')

    city_of_upcoming_visit = ['Следующим городом будет:', ]
    if uniq_wants:
        city_of_upcoming_visit.append(uniq_wants[0])

    uniq_wants.insert(0, 'Никогда никто не был:')

    print(h_visited)
    print(w_to_visit)
    print(uniq_wants)
    print(city_of_upcoming_visit)

    with open('holiday.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([h_visited, w_to_visit, uniq_wants, city_of_upcoming_visit])


write_holiday_cities('L')

