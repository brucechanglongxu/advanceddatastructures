Generally, a B-tree will have $n$ nodes, and $n+1$ children. The question is why we would prefer to use B-trees over binary-search trees (even though all of the operations are still on the order of O(log n)). The reason is we can take advantage of the inherent memory-hierarchy of our computation model. 

<p align="center">
<img width="661" alt="image" src="https://user-images.githubusercontent.com/49863684/192345471-a6bdbba6-04be-4626-864b-153b7d0342e7.png">
</p>

<p align="center">
<img width="367" alt="image" src="https://user-images.githubusercontent.com/49863684/192346102-d70c5998-312f-4bd2-9e06-52a4fb02a234.png">
</p>
