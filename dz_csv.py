import csv

def write_holiday_cities(first_letter):
    with open('travel_notes.csv', 'r') as file:
        reader = csv.DictReader(file, fieldnames=['student', 'cities_visited', 'want_to_visit'])

        have_visited = set()
        wants_to_visit = set()

        for data in reader:
            if data['student']:
                if data['student'][0] == first_letter:
                    visited = data['cities_visited'].split(';')
                    have_visited.update(visited)
                    wants = data['want_to_visit'].split(';')
                    wants_to_visit.update(wants)

        uniq_wants = wants_to_visit - have_visited

        have_visited = list(have_visited)
        wants_to_visit = list(wants_to_visit)
        uniq_wants = list(uniq_wants)

        have_visited.sort()
        wants_to_visit.sort()
        uniq_wants.sort()

        have_visited.insert(0, 'Побывали:')
        wants_to_visit.insert(0, 'Хотят побывать:')


        city_of_upcoming_visit = ['Следующим городом будет:', ]
        if uniq_wants:
            city_of_upcoming_visit.append(uniq_wants[0])

        uniq_wants.insert(0, 'Никогда никто не был:')

        print(have_visited)
        print(wants_to_visit)
        print(uniq_wants)
        print(city_of_upcoming_visit)

        with open('holiday.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([have_visited, wants_to_visit, uniq_wants, city_of_upcoming_visit])


write_holiday_cities('L')