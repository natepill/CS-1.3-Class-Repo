# reading the file
from trie_tree import TrieTree


def load_routes(file_name):
    '''
    Reading the route costs from the text file and return
    dictionary {route#: cost}
    '''
    with open(file_name) as f:

        for line in f:
            pair = line.strip().split(',')
            route = pair[0].replace('+', '')
            price = pair[1]

            route_and_price = [route, price]
            print(route_and_price)

            route_tree = TrieTree(route_and_price)


    # return route_tree


def reading_phone_numbers(file_name):
    '''
    Reading the phone numbers  from the text file and return
    list of phone numbers
    '''
    with open(file_name) as f:
        # remove the '+' sign and reads new line
        f = f.read().replace('+', '').split('\n')
    return f


def call_costs():
    """Return a price for each phone number"""
    phone_number, price = 0, 0
    call_cost = [phone_number, price]

    # file_paths
    route_costs_4 = "data/route-costs-10.txt"
    phone_numbers_3 = "data/phone-numbers-10.txt"
    # route_costs_10 = "project/data/route-costs-100.txt"
    # phone_numbers_10 = "project/data/phone-numbers-100.txt"


    # read routes and phone numbers
    route_costs = load_routes(route_costs_4)

    print(route_costs.size)

    # create a trie with all the routes
    # route = TrieTree(route_costs)
    # # read phone numbers
    # phone_numbers = reading_phone_numbers(phone_numbers_3)
    # phone_num_price = route.search("19876543210")
    # print("size of trie: ", route.size)
    # print(phone_num_price)
    # return call_cost



if __name__ == "__main__":
    call_costs()
