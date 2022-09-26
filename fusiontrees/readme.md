Fusion Trees:

1. Sketch and why it's enough
2. Approximate sketch via. multiplication
3. Parallel comparison
4. Most significant set bit 

Fusion trees provide us with $O(log_w n)$ predecessor and successor. With the two of them together, we obtain $\text{min} ( \log w, \log_w n ) \le \sqrt{\log n}$. We are going to cover the **static** version, which is also linear space and runs on the word RAM model (fredman and willard). There is also a version of fusion trees for $AC^0$ RAM ($AC^0$ represents any constant-depth unbounded fan circuit). 

**Word RAM Model:** 

There are dynamic versions of fusion trees, which is $O(\log_w + \log \log n)$ deterministic. 
