**Separate Chaining:** We can maintain a linked list within every hash-map entry, and grow this to be longer as we continue to add elements. The down-side to this is that there could be a lot of "unused" space within our hash-table (for example if the entire chain clumps together on one element). 

**Open Addressing:** This is a technique that is used to resolve collisions within our hash map. In linear probing, if h(y) is hashed to the same place as h(x), then we should place our element immediately to the right of the collision area. To overcome the problems with linear probing, we should try **quadratic probing**. We begin with our hash value (the first element that we put in this space), and if we have a collision, we should try put our element in $h + 1^2, h + 2^2, h + 3^2$ and so on, in order to prevent data from "clumping" together. Our last solution is to maintain two hash function, as this allows us to prevent a collision by using the second hash function whenever the first hash function leads to a collision as we map between x and y. 

1. Universal and k-wise independent

<p align="center">
<img width="646" alt="image" src="https://user-images.githubusercontent.com/49863684/192110507-13b36628-d0de-4d00-b3d6-9a86bae09421.png">
</p>

One hash function we can choose is a "totally random" hash function, where we uniformly at random choose an element in the range to assign to an element in the domain in order to generate our hash function. This falls in the domain of a more general class of hash functions called universal hash functions, where we restrict the hash function space to a smaller family H', that satisfies the probability of collision being on the order of O(1/m). Two examples can be found below:

<p align="center">
<img width="601" alt="image" src="https://user-images.githubusercontent.com/49863684/192110668-8fbea3bd-0f5b-4535-bc93-e491c7d0d43b.png">
<img width="637" alt="image" src="https://user-images.githubusercontent.com/49863684/192110711-01e100e1-a844-4959-933f-22a25578a1d2.png">
</p>

**k-wise independence:** We would like to find a family $H$ of hash functions that satisfies the following:

<p align="center">
<img width="635" alt="image" src="https://user-images.githubusercontent.com/49863684/192110832-a4734230-5635-4d8e-b6cf-b99562bc908a.png">
</p>

In general, we can construct a polynomial of degree k, take that modulo p and modulo m (where the coefficients are arbitrary numbers between $0$ and $p$. Note that this is a very expensive $O(k)$ hash function. 

2. Simple tabulation hashing
3. Chaining and perfect hashing
4. Linear probing
5. Cuckoo hashing
