import pdb
import itertools
class Exercise1:
    def __init__(self, locations = ["A", "M", "B", "S", "C", "E"]):
        ## Working with fully connected graph

        self.graph = {}

        for i in locations:
            self.graph[i] = {}
            for j in locations:
                if i != j:
                    self.graph[i].update({j : 0})

    def add_weight(self, start, end, weight):
        self.graph[start][end] = weight

    def add_all_weights(self, start, all_weights):
        # all_weights is list of lists [[city, weight]]
        for end, weight in all_weights:
            # pdb.set_trace()
            #  = elem
            self.graph[start][end] = weight

    def path_cost(self, path):
        cost = 0
        start = path[0]
        for city in path[1:]:
            cost += self.graph[start][city]
            start = city

        return cost
    
    def tsp(self, path):
        # diff_iters = itertools.permutations(path[1:len(path)-1], len(path[1:len(path)-1]))
        # min_weight = self.path_cost(path)
        # min_path = path
        
        # path_start = [path[0]]

        # for curr_middle in diff_iters:
        #     new_path = path_start + list(curr_middle) + path_start
        #     cost = self.path_cost(new_path)
        #     print(f"Path and cost: {new_path}, {cost}")
        #     if cost < min_weight:
        #         min_weight = cost
        #         min_path = tuple(new_path.copy())

        # return min_weight, min_path
        all_idx = [i for i in range(1, len(path)-1)]
        # diff_iters = itertools.permutations(path[1:len(path)-1], 2)
        # diff_iters = itertools.permutations(all_idx, 2)
        min_weight = self.path_cost(path)
        min_path = list(path)
        prevoius_weight = min_weight + 1
        
        # path_start = [path[0]]

        iterations = 0
        past_paths = {tuple(path)}
        while min_weight < prevoius_weight:
            prevoius_weight = min_weight
            print(f"Current path and cost: {min_path}, {min_weight}\n")
            temp_weight, temp_path = min_weight, min_path.copy()
            iterations += 1
            # for curr_middle in diff_iters:
            for curr_middle in itertools.permutations(all_idx, 2):
                # pdb.set_trace()
                # new_path = path_start + list(curr_middle) + path_start

                if curr_middle[0] > curr_middle[1]:
                    continue
                
                temp_set = {curr_middle[0]-1, curr_middle[0], curr_middle[1]-1, curr_middle[1]}
                
                
                if len(temp_set) == 3:
                    continue

                new_path = min_path[:curr_middle[0]] + [min_path[curr_middle[1]]]

                if len(min_path[curr_middle[0]+1 : curr_middle[1]]) > 0:
                    new_path = new_path + min_path[curr_middle[0]+1 : curr_middle[1]]

                new_path = new_path + [min_path[curr_middle[0]]] + min_path[curr_middle[1]+1 : ]

                if tuple(new_path) in past_paths:
                    continue
                cost = self.path_cost(new_path)

                print(f"Possible path and cost: {new_path}, {cost}")
                # if cost < min_weight:
                #     min_weight = cost
                #     # min_path = tuple(new_path.copy())
                #     min_path = new_path.copy()
                if cost < temp_weight:
                    temp_weight = cost
                    # min_path = tuple(new_path.copy())
                    temp_path = new_path.copy()
            print(f"Iteration: {iterations} path and cost: {temp_path}, {temp_weight}\n")
            min_weight, min_path = temp_weight, temp_path 
            past_paths.add(tuple(min_path))

        return min_weight, min_path


def main():
    ex1 = Exercise1()

    arlington = [["M", 11], ["B", 10], ["S", 10], ["C", 15], ["E", 14]]
    medford = [["A", 11], ["B", 15], ["S", 9], ["C", 16], ["E", 9]]
    belmont = [["A", 10], ["M", 15], ["S", 9], ["C", 8], ["E", 13]]
    somerville = [["A", 10], ["M", 9], ["B", 9], ["C", 10], ["E", 6]]
    everett = [["A", 14], ["M", 9], ["B", 13], ["S", 6], ["C", 11]]
    cambridge = [["A", 15], ["M", 16], ["B", 8], ["S", 10], ["E", 11]]

    ex1.add_all_weights("A", arlington)
    ex1.add_all_weights("M", medford)
    ex1.add_all_weights("B", belmont)
    ex1.add_all_weights("S", somerville)
    ex1.add_all_weights("E", everett)
    ex1.add_all_weights("C", cambridge)

    path = ("M","B","E","A","C","S","M")
    # ex1.get_all_iterations(path)


    # pdb.set_trace()
    print(ex1.tsp(path))

    # for i in itertools.permutations([1,2,3,4,5], 2):
    #     print(i)
    # print("DONE")

if __name__ == "__main__":
    main()