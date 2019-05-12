# reading the file


def reading_route(file_name):
    '''
    Reading the route costs from the text file and return
    dictionary {route#: cost}
    '''
    with open(file_name) as f:
    #     d = dict(line.strip().split(',') for line in f)
    # return d

        dict_of_routes = dict()

        for line in f:
            pair = line.strip().split(',')
            # pair[0] = pair[0].replace('+', '')
            # dict_of_routes[pair[0]] = pair[1]

            dict_of_routes[pair[0][1:]] = pair[1]
            # print(pair)

    return dict_of_routes

def reading_phone(file_name):
    '''
    Reading the phone numbers  from the text file and return
    list of phone numbers
    '''
    with open(file_name) as f:
        f = f.read().split('\n')
    return f


def calculate_call_cost(list_of_phone_numbers, cost_of_routes):

    for number in list_of_phone_numbers:
        pass


if __name__ == "__main__":
    route_path = "route-costs-10.txt"
    # phone_path = "project/data/phone-numbers-3.txt"

    call_costs = reading_route(route_path)
    print(call_costs)
    # phone_numbers = reading_phone(phone_path)
    # print(phone_numbers)
