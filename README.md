# Words detector supported in batch processing

This application consist in a script that searches inside a matrix all words in english using Depth Fisrt Search algorithm.

It traverses all possible paths from all nodes to all nodes with the purpose of visit neighbour nodes both horizontal or vertical way and append letters to find words.

# Continuous Deployment
The continuous deployment of the solution is supported in Docker Hub and set up so that each commit to this GitHub repo be immediately processed.

Once Docker Hub has finished its process, the image will be available to be run by a job definition in AWS Batch.

# Process summary
In the following image, can be seen the flow of data betwen client and AWS components.

![Diagram](./"Cloud flow.png")
