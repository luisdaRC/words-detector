from nltk.corpus import words
import boto3
import trie
import json
import ast
import os


def findWords(matrix, words):

    n = len(matrix)
    visited = [[False]*n for _ in range(n)]
    local_trie = trie.Trie()
    result = []

    # All the words from nltk dictionary are added to the trie
    for word in words:
        local_trie.add_word(word)

    def dfs(prev, node, i,j):

    	#If we are in the last node of the 
        if node.last and len(''.join(prev))>1:
            result.append(''.join(prev))
            node.last = False

        if not (0 <= i < n) or not (0 <= j < n) or visited[i][j] == True or matrix[i][j] not in node.neighbours or not node.neighbours:
            return 

        node = node.neighbours[matrix[i][j]]
        visited[i][j] = True
        current_node = [matrix[i][j]]
        
        #All the neighbours nodes are recursively visited

        # Goes to the node up
        dfs(prev + current_node, node, i-1, j)
        # Goes to the node down
        dfs(prev + current_node, node, i+1, j)
        # Goes to the left node
        dfs(prev + current_node, node, i, j-1)
        # Goes to the right node
        dfs(prev + current_node, node, i, j+1)
        
        visited[i][j] = False
        return
        
    #The search starts in the root node and with each iteration changes the actual node
    for i in range(n):
        for j in range(n):
            dfs([], local_trie.root, i, j)
    return result


def main():

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

	toFind = []

	for i in range(n):
		rowList = []
		for j in range(n):
			rowList.append(data[i][j].lower())
		toFind.append(rowList)

	#The list of words is obtained from nltk
	wordlist = words.words()
	found = findWords(toFind, wordlist)

	# APIGateway connection data for returning all found words
	URL = "https://25zf7whaca.execute-api.us-east-1.amazonaws.com/dev"
	client = boto3.client("apigatewaymanagementapi", endpoint_url = URL, region_name = "us-east-1")

	message = {"message": json.dumps(found)}

	response = client.post_to_connection(ConnectionId=connection_id, Data=json.dumps(message))



if __name__ == '__main__':

	main()
