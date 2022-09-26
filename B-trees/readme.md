Generally, a B-tree will have $n$ nodes, and $n+1$ children. The question is why we would prefer to use B-trees over binary-search trees (even though all of the operations are still on the order of O(log n)). The reason is we can take advantage of the inherent memory-hierarchy of our computation model. The diagram below is a 2-3 tree, a special case of a B-tree. 

<p align="center">
<img width="661" alt="image" src="https://user-images.githubusercontent.com/49863684/192345471-a6bdbba6-04be-4626-864b-153b7d0342e7.png">
</p>

In general, we would like to make the number of nodes in a B-tree equal to the word-size in the cache. This will allow us to get an entire node from the disk, work on this, then get an entire node from the disk, which allows us to speed up operations since although we are still accessing the disk every time we go down a level, we are utilizing the whole block when we do so every time. 

<p align="center">
<img width="367" alt="image" src="https://user-images.githubusercontent.com/49863684/192346102-d70c5998-312f-4bd2-9e06-52a4fb02a234.png">
</p>

A B-tree has a parameter called the branching factor, which is a lower bound on the number of chidlren of every node (except for the root node and the leaves). 
$$B \le \textit{Number of Children} < 2B$$
$$B - 1 \le \textit{Number of Keys} < 2B - 1$$
Furthermore, we find that our B-tree is completely balanced i.e. all of the leaves are at the same depth. 
