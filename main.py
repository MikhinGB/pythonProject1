import json

def employees_rewrite(sort_type):


    srt_type = sort_type.lower()

    if srt_type.startswith('last'):
        sort_type = 'lastName'
    elif srt_type.startswith('first'):
        sort_type = 'firstName'
    elif srt_type.startswith('sal'):
        sort_type = 'salary'
    elif srt_type.startswith('depart'):
        sort_type = 'department'
    else:
        raise ValueError('Bad key for sorting')


    with open('employees.json') as file:
        data = json.load(file)
        employees = data.get('employees')

        employees_sorted = sorted(employees, key=lambda x: x[sort_type], reverse=True) \
            if isinstance(employees[0][sort_type], int) else sorted(employees, key=lambda x: x[sort_type])

        data = {'employees': employees_sorted}
        # print(data)

        file_out = 'employees_' + srt_type + '_sorted.json'
        with open(file_out, 'w') as f:
            json.dump(data, f, indent=4)

employees_rewrite('department')