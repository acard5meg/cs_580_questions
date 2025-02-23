from collections import deque
import heapq
import pdb
import copy
# 
# 
class Exercise2:
    def __init__(self, countries = ['G', 'P', 'CR', 'S', 'SW', 'A', 'H', 'I', 'SL'], \
                 domains = ['Red', 'Green', 'Blue', 'Yellow']):
        self.countries = countries
        self.domains = {}
        self.map = {}
        self.colors = {}

        for i in self.countries:
            self.domains[i] = domains.copy()
            self.map[i] = []

    def get_countries(self):
        return self.countries.copy()
    
    def get_connections(self, country):
        return self.map[country].copy()
    
    def is_colored(self, country):
        return True if country in self.colors else False
    
    def get_color(self, country):
        return self.colors[country]

    def add_branch(self, country1, connects):

        # if country1 in self.map:
        #     print(f"{country1} is in map with the connections {self.map[country1]} ", end='')
        #     print("do you want to continue Y/N: ")
        #     ans = input()

        #     if ans == 'N':
        #         return

        if isinstance(connects, list):
            for i in connects:
                self.map[country1].append(i)
        else:
            self.map[country1].append(connects)

    def color(self, country, color):
        if country in self.colors:
            print("REASSIGNMENT")
            return
        
        self.colors[country] = color


    def is_valid_assignment(self, country, curr_color):

        if country in self.colors:
            return False
        
        for connected_country in self.map[country]:
            if connected_country in self.colors:
                if curr_color == self.colors[connected_country]:
                    return False
                
        return True


    def get_degree_of_unassigned(self, country):
        degree = 0

        self.__inclusion_check(country)

        for i in self.map[country]:
            if i not in self.colors:
                degree += 1

        return degree
    
    def get_domain_size(self, country):
        
        self.__inclusion_check(country)

        return len(self.domains[country])
    
    def get_domain(self, country):
        
        self.__inclusion_check(country)

        return self.domains[country].copy()
    

    
    def remove_color_from_domain(self, country, color):
        if color in self.domains[country]:
            self.domains[country].remove(color)
            return True
        else:
            return False
    

    # Pretty problem specific
    # def fill_heap(self, csp, heap):
    def give_me_country(self):
        # min_domain, -1 * max_degree, country
        heap = []
        for curr_country in self.get_countries():
            if not self.is_colored(curr_country):
                domain_size = self.get_domain_size(curr_country)
                degree = self.get_degree_of_unassigned(curr_country)
                heapq.heappush(heap, (domain_size, -degree, curr_country))

        _, _, country = heapq.heappop(heap)
        return country
    
    def remove_colors_from_neighbors(self, curr_country):
        # abbreviated AC-3 algo for coloring
        # q = deque()

        curr_country_color = self.get_color(curr_country)

        for neighbor in self.get_connections(curr_country):
            self.remove_color_from_domain(neighbor, curr_country_color)

            if self.get_domain_size(neighbor) == 0:
                return False
            

        return True


    def is_complete_assignment(self):
        return True if  len(self.map) == len(self.colors) else False

    def current_assignment(self):
        print("This is the current assignment")
        for i in self.colors:
            print(f"Country {i}: {self.colors[i]}")

    def return_current_assignment(self):
        return self.colors.copy()


    def __inclusion_check(self, country):
        if country not in self.map:
            print(f"{country} not in map")
            return        


def backtrack_search(csp, print_steps = False, start = 'A'):
    ### Could make a flexible initialization
    # current_iteration = 0

    # heap = []
    stack = deque()

    # csp.fill_heap(csp, heap)

    # pdb.set_trace()
    stack.append(copy.deepcopy(csp))

    while stack:

        curr_class = stack.pop()

        if curr_class.is_complete_assignment():
            return curr_class.return_current_assignment()

        curr_country = curr_class.give_me_country()

        for curr_color in curr_class.get_domain(curr_country):

            new_class = copy.deepcopy(curr_class)

            if new_class.is_valid_assignment(curr_country, curr_color):
                new_class.color(curr_country, curr_color)

                if new_class.remove_colors_from_neighbors(curr_country):
                    stack.append(new_class)
        
                if print_steps:
                    # print(f"STACK ELEMENTS: {current_iteration}")
                    print(f"STACK ELEMENTS")
                    print()
                    new_class.current_assignment()
                    print()
                    for i in new_class.get_countries():
                        if new_class.is_colored(i):
                            continue
                        else:
                            print(f"Domain and degree of {i}: ", end='')
                            print(f"{new_class.get_domain(i)}, ", end='')
                            print(f"{new_class.get_degree_of_unassigned(i)}")
                    print()
        # current_iteration += 1

def main():
    ex2_map = Exercise2()

    ex2_map.add_branch('G', ['SW', 'A', 'CR', 'P'])
    ex2_map.add_branch('P', ['G', 'CR', 'S'])
    ex2_map.add_branch('CR', ['G', 'P', 'S', 'A'])
    ex2_map.add_branch('SW', ['G', 'A', 'I'])
    ex2_map.add_branch('A', ['I', 'SL', 'H', 'SW', 'S', 'CR', 'G'])
    ex2_map.add_branch('S', ['H', 'A', 'CR', 'P'])
    ex2_map.add_branch('H', ['A', 'SL', 'S'])
    ex2_map.add_branch('I', ['SW', 'A', 'SL'])
    ex2_map.add_branch('SL', ['I', 'A', 'H'])

    # for i in ex2_map.get_countries():
    #     print(f"Degree of {i} : {ex2_map.get_degree_of_unassigned(i)}")
    #     print(f"Domain size of {i}: {ex2_map.get_domain_size(i)}")

    print(backtrack_search(ex2_map, print_steps=True))



if __name__ == "__main__":
    main()