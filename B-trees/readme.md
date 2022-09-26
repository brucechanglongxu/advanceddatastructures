Generally, a B-tree will have $n$ nodes, and $n+1$ children. The question is why we would prefer to use B-trees over binary-search trees (even though all of the operations are still on the order of O(log n)). The reason is we can take advantage of the inherent memory-hierarchy of our computation model. The diagram below is a 2-3 tree, a special case of a B-tree. 

<p align="center">
<img width="661" alt="image" src="https://user-images.githubusercontent.com/49863684/192345471-a6bdbba6-04be-4626-864b-153b7d0342e7.png">
</p>

In general, we would like to make the number of nodes in a B-tree equal to the word-size in the cache. This will allow us to get an entire node from the disk, work on this, then get an entire node from the disk, which allows us to speed up operations since although we are still accessing the disk every time we go down a level, we are utilizing the whole block when we do so every time. 

<p align="center">
<img width="367" alt="image" src="https://user-images.githubusercontent.com/49863684/192346102-d70c5998-312f-4bd2-9e06-52a4fb02a234.png">
</p>

A B-tree has a parameter called the branching factor ($B$ is chosen according to the cache size e.g. $2B$ should be around the size of the cache), which is a lower bound on the number of chidlren of every node (except for the root node and the leaves). 
$$B \le \textit{Number of Children} < 2B$$
$$B - 1 \le \textit{Number of Keys} < 2B - 1$$
Furthermore, we find that our B-tree is completely balanced i.e. all of the leaves are at the same depth. 

**How search works:** In general, we bring in a key $k$, and search through all of the values within the node that we are looking at. Find where $k$ fits in, and go down the appropriate path (either left or right); this is very similar to a normal binary search tree. 

**How insertion works:** We can begin by inserting as usual, searching through the tree until we land upon a node where we would like to insert. However there is a risk that this node will overflow. Suppose that we have a B-tree with $B = 4$. We see that in this case, the minimum number of keys is equal to $3$, whilst the maximum number of keys is equal to $6$. Suppose, however we do have a case where we insert into the seventh node. 

**How insertion works:** We can begin by inserting as usual, searching through the tree until we land upon a node where we would like to insert. However there is a risk that this node will overflow. Suppose that we have a B-tree with $B = 4$. We see that in this case, the minimum number of keys is equal to $3$, whilst the maximum number of keys is equal to $6$. Suppose, however we do have a case where we insert into the seventh node.

<p align="center">
<img width="254" alt="image" src="https://user-images.githubusercontent.com/49863684/192348894-a6bda45e-61e5-4c33-95d7-acf454d84ebc.png">
</p>

Now that we have an overflowed node, we will apply the **split** operation. We will split the node into two parts, by removing the middle node, and moving this into the parent node. Now if our **root** begins to overflow, we should apply this split property on the root, and move the middle node upwards. If we need to continue to do this all the way to the root, then we should split the root and introduce a new singular node as the new root. 

<p align="center">
<img width="230" alt="image" src="https://user-images.githubusercontent.com/49863684/192349506-cf0209a4-c002-44f1-9447-050032da5b54.png">
</p>

**How Deletion Works:** For deletion, again we can begin by using the normal deletion heuristic for BSTs. A problem will occur when we delete a node, and it becomes underfull "move the deletion to the leaf" [continue] 
