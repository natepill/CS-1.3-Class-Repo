# reading the file
from Trie_tree import TrieTree

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
            pair[0] = pair[0].replace('+', '')
            dict_of_routes[pair[0]] = pair[1]

            # dict_of_routes[pair[0][1:]] = pair[1]
            # print(pair)
    return dict_of_routes

def reading_phone(file_name):
    '''
    Reading the phone numbers  from the text file and return
    list of phone numbers
    '''
    with open(file_name) as f:

        list_of_phone_numbers = list()

        for line in f:
            line = line.strip()
            number = line.replace('+', '')
            list_of_phone_numbers.append(number)


    return list_of_phone_numbers


def call_costs():
    """Return a price for each phone number"""
    phone_number, price = 0, 0
    call_cost = [phone_number, price]

    # file_paths
    route_costs_4 = "project/data/route-costs-4.txt"
    phone_numbers_3 = "project/data/phone-numbers-3.txt"
    # route_costs_10 = "project/data/route-costs-100.txt"
    # phone_numbers_10 = "project/data/phone-numbers-100.txt"

    # read routes and phone numbers
    route_costs = reading_route(route_costs_4)
    # phone_numbers = reading_phone_numbers(phone_numbers_3)

    # create a trie with all the routes
    route = TrieTree(route_costs)

    print(route.size)

    return call_cost


if __name__ == "__main__":
    route_path = "data/route-costs-10.txt"
    phone_path = "data/phone-numbers-10.txt"

    # call_costs = reading_route(route_path)
    # print(call_costs)
    phone_numbers = reading_phone(phone_path)
    print(phone_numbers)
