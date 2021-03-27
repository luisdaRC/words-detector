import collections
import enchant
import boto3
import json
import ast
import os

dictionary = enchant.Dict("en_CA")
found = set()
graph = {}
graph_numbers = collections.defaultdict(list)

'''
Function designed for trasversing all possible paths
from a given source to a given target
'''
def traverse_all_paths(source, target, visited, word):
    visited[source] = True
    word.append(graph[source])

    # When the path is trasversed, is checked in the dictionary if the appended word exists
    if source is target:
        formatted_word = ''.join(word).capitalize()

        if dictionary.check(formatted_word):
            found.add(formatted_word)

    # If the path is not completed, then the graph is looped through all it's nodes
    else:
        for i in graph_numbers[source]:

            if visited[i] is False:
            	# In each iteration, the source node is updated so that it can reach the target
                traverse_all_paths(i, target, visited, word)

    word.pop()
    visited[source] = False


'''
In the main function are received the parameters arriving from the lambda function(my-lambda-function),
the incoming matrix is parsed into a graph-like data structure and all the elements are related to its
neighbour element (up, down, left and right).

The graph is traversed from all to all nodes and trasversed_all_paths() is in charge of returning all
found words.

The set of all found words is sent to APIGateway along with the client ConnectionId data.
'''
def main():

    cont = 0
    matrix = ""
    connection_id = ""

    # Getting parameters from the lambda function
    try:
    	matrix = os.environ.get("Matrix")
    	connection_id = os.environ.get("ConnectionId")
    	print(matrix +" from environment")

    except:
    	print("Im in the except of test.py")

    data = ast.literal_eval(matrix)
    n = len(data)

    for i in range(n):
        for j in range(n):

            graph[cont] = data[i][j].lower()

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

    # Traversing the graph from all to all its nodes
    for source in graph_numbers.keys():
        for target in graph_numbers.keys():

            if source is not target:
                visited = [False] * (n ** 2)
                word = []
                traverse_all_paths(source, target, visited, word)

    print(found)

    # APIGateway connection data for returning all found words
    URL = "https://25zf7whaca.execute-api.us-east-1.amazonaws.com/dev"
    client = boto3.client("apigatewaymanagementapi", endpoint_URL=URL)

    message = {"message": json.dumps(found)}

    response = client.post_to_connection(ConnectionId=connection_id, Data=json.dumps(message))


if __name__ == '__main__':
    main()
