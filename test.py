import collections
import enchant

dictionary = enchant.Dict("en_CA")
found = set()
graph = {}
graph_numbers = collections.defaultdict(list)


def traverse_all_paths(source: int, target: int, visited, word):
    visited[source] = True
    word.append(graph[source])

    if source is target:
        formatted_word = ''.join(word).capitalize()

        if dictionary.check(formatted_word):
            found.add(formatted_word)

    else:
        for i in graph_numbers[source]:

            if visited[i] is False:
                traverse_all_paths(i, target, visited, word)

    word.pop()
    visited[source] = False


def main():
    data = [['a','c','b','n','h'],['n','a','t','e','o'],['a','d','r','p','v'],['v','f','e','t','t'],['w','u','a','d','k']]

    cont = 0
    n = len(data)
    testWord = ""

    try:
    	testWord = os.environ.get("Test")
    	print(testWord +" from environment")

    except:
    	error = ''
    	print("Im in the except of test.py")

    for i in range(n):
        for j in range(n):

            graph[cont] = data[i][j]

            # Append the element up
            if i - 1 >= 0:
                graph_numbers[cont].append(cont - n)

            # Append the element down
            if i + 1 < n:
                graph_numbers[cont].append(cont + n)

            # Append the left element
            if j - 1 >= 0:
                graph_numbers[cont].append(cont - 1)

            # Append the right element
            if j + 1 < n:
                graph_numbers[cont].append(cont + 1)

            cont = cont + 1

    for source in graph_numbers.keys():
        for target in graph_numbers.keys():

            if source is not target:
                visited = [False] * (n ** 2)
                word = []
                traverse_all_paths(source, target, visited, word)

    print(found)


if __name__ == '__main__':
    main()
