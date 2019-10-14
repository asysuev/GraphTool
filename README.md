# GraphTool

Adding some useful tools for nx graphs

## Converters

### Graph to tree
Given starting point unpacks (Multi)DiGraph to Tree (represented by Digraph)

### Tree to graph
Packs Digraph(Tree) to Graph, using node data to identify same nodes

## Loaders

### DB Loader
Loads nx graph from a db query (query results can be either edge list or adjacency matrix (--for god sake, no!--)). 