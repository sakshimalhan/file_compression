# Huffman Coding
<a id="top"></a>

### About the algorithm
 
Huffman coding is a lossless data compression algorithm. In this algorithm, a variable-length code is assigned to input different characters. Length of the code for every character depends on the frequency of that character.Every  character takes one byte of space in memory. Idea behind the huffman coding algorithm is to minimize the space occupied by the characters that occur frequently in a file.

### Data structures used
* dictionary
* heap
* binary tree

## Steps followed
* Build a dictionary containing distinct characters of the file as key as frequency as value.


* Build a min_heap consisting of binary tree nodes and each node object carrying the information of character it stores and frequency of that character.


* With the min_heap,build a binary tree. Extract two nodes with the minimum frequency from the min heap.Create a new internal node with a frequency equal to the sum of the two nodes frequencies.


* Traverse the tree formed starting from the root. Maintain a dictionary and a string. While moving to the left child, write 0 to the string. While moving to the right child, write 1 to the string. Add dtring to the dictionary when a leaf node is encountered. Do it rescursively.


* This way we have unique prefix free codes for every character. Repalce each character with its code.

## Try it!


* Clone the repository to your local system using the commands below.
```
git clone https://github.com/sakshimalhan/huffman_coding
cd huffman_coding
```

* Run the python interpreter.
```
python main.py
```
* Give the path of the file to be compressed as input.


* Check the output files(printed on your console).


