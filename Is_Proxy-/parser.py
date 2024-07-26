import os

# Remove http:// and remove ports from lists.

for file in os.listdir("Lists"):

    nn = []
    nodes = [node.strip() for node in open("Lists/" + file, 'r').readlines()]

    for node in nodes:
        if ":" in node:
            nn.append(node.split(":")[0].replace("http://", ""))
        else:
            nn.append(node.replace("http://", ""))
    with open("Lists/" + file, 'w') as f:
        f.write("\n".join(nn))

        