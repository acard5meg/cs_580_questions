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
        diff_iters = itertools.permutations(path[1:len(path)-1], len(path[1:len(path)-1]))
        min_weight = self.path_cost(path)
        min_path = path
        
        path_start = [path[0]]

        for curr_middle in diff_iters:
            new_path = path_start + list(curr_middle) + path_start
            cost = self.path_cost(new_path)
            print(f"Path and cost: {new_path}, {cost}")
            if cost < min_weight:
                min_weight = cost
                min_path = tuple(new_path.copy())

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
    # print("DONE")

if __name__ == "__main__":
    main()