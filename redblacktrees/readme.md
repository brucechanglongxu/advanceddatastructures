What hapepns when our binary search tree is unbalanced? A red-black-tree is a specific type of balanced search tree that satisfies the following criteria (the colouring is a mechanism used to ensure the balanced property). 

1. A node is either red or black
2. The root and leaves (NIL) are black
3. If a node is red, then its children are black
4. All paths from a node to its NIL descendants contain the same number of black nodes (we don't count the root node itself) 

<p align="center">
<img width="935" alt="image" src="https://user-images.githubusercontent.com/49863684/192351950-4a92cd54-84e2-4baf-bac6-8a7cfb7692a7.png">
</p>

**Extra Notes:** Nodes require one storage bit to keep track of colour. The longest path (root to farthest NIL) is no more than twice the length of the shortest path (root nearest NIL). The shortest path is all black nodes, whilst the longest path alternates between red and black. 

Search is the same as for a normal binary search tree, however insertion and deletion require "swaps" in order to maintain the red-black-tree properties. 
