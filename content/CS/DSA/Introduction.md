Following are collection of data structures and algorithms planned to be implemented in Mojo.

## Resources

- [ ] [Data Structures and Algorithms Roadmap](https://roadmap.sh/datastructures-and-algorithms
- [ ] [GitHub - jwasham/coding-interview-university: A complete computer science study plan to become a software engineer.](https://github.com/jwasham/coding-interview-university?tab=readme-ov-file)
- [ ] [GitHub - keon/algorithms: Minimal examples of data structures and algorithms in Python](https://github.com/keon/algorithms)
- [ ] [GitHub - TheAlgorithms/Python: All Algorithms implemented in Python](https://github.com/TheAlgorithms/Python)
- [ ] 
## Data structures

[Top Data Structures That Every Programmer Must Know - GeeksforGeeks](https://www.geeksforgeeks.org/top-data-structures-that-every-programmer-must-know/)
[Seven (7) Essential Data Structures for a Coding Interview and associated common questions | by Aqeel Anwar | Towards Data Science](https://towardsdatascience.com/seven-7-essential-data-structures-for-a-coding-interview-and-associated-common-questions-72ceb644290)


1. Array
2. String
3. Linked List
4. Stacks
5. Queues
6. Trees
7. Heaps
8. Graphs
9. Hash Tables
10. Matrix
11. Tries

## Algorithms
[10 Most Important Algorithms For Coding Interviews - GeeksforGeeks](https://www.geeksforgeeks.org/algorithms-for-interviews/)
[🚀 DSA Master (interviewmaster.io)](https://www.interviewmaster.io/p/dsa-master)


1. Sorting Algorithms
2. Searching Algorithms
3. String Algorithms
4. Divide and Conquer
5. Recursion & Backtracking
6. Greedy Algorithms
7. Dynamic Programming
8. Tree-Related Algo
9. Graph Algorithms
10. Sliding Window


## To Do:
[LeetCode was HARD until I Learned these 15 Patterns (algomaster.io)](https://blog.algomaster.io/p/15-leetcode-patterns)

LeetCode was HARD until I Learned these 15 Patterns:  
  
1. Prefix Sum  
2. Two Pointers  
3. Sliding Window  
4. Fast & Slow Pointers  
5. LinkedList In-place Reversal  
6. Monotonic Stack  
7. Top ‘K’ Elements  
8. Overlapping Intervals  
9. Modified Binary Search  
10. Binary Tree Traversal  
11. Depth-First Search (DFS)  
12. Breadth-First Search (BFS)  
13. Matrix Traversal  
14. Backtracking  
15. Dynamic Programming Patterns  
  
I wrote a detailed article on these patterns and provide links to leetcode problems you can practice to learn them better.  
  
Check it out here: [https://lnkd.in/gPEcjyxW](https://lnkd.in/gPEcjyxW)

1. Heap - Heapsort, Dijkstra, Median of a Stream
2. Binary Tree - Traversals(Pre-Order, Post-Order, In-Order, Level Order) - Lowest Common Ancestor, Left View of a Binary Tree, Maximum Path Sum 
3. HashMap - Whenever a quick lookup is needed
4. Stack/Queue - Largest Rectangle in a Histogram
5. Graphs - Graph Search(BFS, DFS, Dijkstra), Topological Sort, Loop in a Graph - Bus Routes

1. Top-k Largest Elements(from array)
2. Sliding Window(longest substring without repeating characters) 
3. Backtracking(combination/target sum, word ladder, permutation, sudoku solver)
4. Dynamic Programming(combination/target sum)
5. DFS(implemented using stack(LIFO)) and BFS(implemented using queue(FIFO)) ex-Dijkstra's Algorithm, Topological sort


Algorithms:
[Top 7 Algorithms for Coding Interviews Explained SIMPLY (youtube.com)](https://www.youtube.com/watch?v=kp3fCihUXEg)

- Algorithms Binary Search: 
	- Used to find a specific element in a sorted list efficiently. 
	- Inefficient: O(n) for linear search, incrementally guessing from start to end. 
	- Efficient: O(log2(n)) for binary search, repeatedly dividing the search interval in half until the correct element is found. 
- Depth-First Search (DFS): 
	- Begins at the root node and explores as far as possible along each branch before backtracking. 
	- Utilizes a visited array to track already visited nodes. 
	- Continues backtracking until all nodes are visited. 
	- Real-life example: Solving a maze by systematically exploring paths until the exit is found. 
- Breadth-First Search (BFS): 
	- Looks at every node at one level before going down to the next level. 
	- Utilizes a visited array to track already visited nodes and a queue to keep track of neighbors. 
	- Begins at the root node and adds it to the visited array and all its connected nodes to the queue, then continues to explore nodes level by level. 
	- Real-life example: Chess algorithms predict the best move by exploring possible moves at each level of the game tree. 
	- Runtime: O(V + E), where V is the number of vertices and E is the number of edges. 
- Insertion Sort: 
	- Examine’s each element in the list, comparing it with the previous elements and shifting them to the right until the correct position for insertion is found.
	- Simple sorting algorithm suitable for small datasets or nearly sorted arrays. 
	- Runtime: 
		- Best case: O(n) when the list is already sorted. 
		- Worst case: O(n^2) when the list is sorted in reverse order. 
		- Efficient for small or nearly sorted lists, but inefficient for large unsorted lists. 
- Merge Sort: 
	  - A divide-and-conquer sorting algorithm that breaks the problem into smaller subproblems and solves them recursively. 
	  - Starts by splitting the array into halves recursively until each subarray consists of single elements. 
	  - Merges pairs of subarrays by comparing elements and placing them in sorted order. 
	  - Continues merging subarrays until the full array is sorted. 
	  - Runtime: O(n log(n)) in both best and worst cases, making it efficient for large datasets. 
- Quick Sort: 
	- A complex sorting algorithm that follows the divide-and-conquer approach and is recursive. 
	- Selects a pivot element, ideally close to the median, and partitions the list into two sublists: one with elements greater than the pivot and the other with elements less than the pivot.
	- Continues the process recursively on each sublist until the entire list is sorted. 
	- Utilizes a pivot element that is moved to the end of the list, with pointers positioned at the leftmost and rightmost elements. 
	- Compares the elements pointed to by the left and right pointers, swapping them if necessary, until the pointers cross. 
	- Once the pivot is correctly positioned, the process repeats on the sublists. 
	- Runtime: 
	    - Best case: O(n log(n)), when the pivot consistently divides the list into approximately equal halves. 
	    - Worst case: O(n^2), when the pivot selection consistently results in unbalanced partitions. 
- Greedy Algorithm: 
	  - A problem-solving approach that makes the locally optimal choice at each stage with the hope of finding a global optimum. 
	  - May not always guarantee an optimal solution but is often simple and efficient. 
	  - Real-life example: Finding the shortest path in a weighted graph using Dijkstra's algorithm, where at each step, the algorithm selects the vertex with the smallest distance from the source.