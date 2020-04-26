import heapq,os


#  creating class node 
class Node:
	def __init__(self,character,frequency):
		self.char=character
		self.freq=frequency
		self.left=None
		self.right=None

	# overloading lt(less than)	and eq(equal to) operators on class Node objects

	def __lt__(self,b):
		return self.freq<b.freq
	def __eq__(self,b):
		return self.freq==b.freq

# this is first task that need to be done in order to compress a file	
# the function takes the text of the file to be compressed as input and returns a dictionary containg the frequency of each character present in the text

def build_dict(text):
	d={}
	for char in text:
		d[char]=d.get(char,0)+1	
	return d	

# a dictionary stores its elements in unknown order...to maintain the order we store the objects in a maxheap..elemenys stored in the heap are
# class node objects. Alongwith the heap the function also returns the size of heap (which we use later).

def build_heap(d):
	l=len(d)
	heap=[]
	for key in d:
		node=Node(key,d[key])
		heapq.heappush(heap,node)
	return heap,l


# the function accepts the maxheap and its size as parameters and returns the root of binary tree.

def build_btree(heap,l):
	while(l>1):
		node1=heapq.heappop(heap)
		node2=heapq.heappop(heap)
		node3=(Node(" ",node1.freq + node2.freq))
		heapq.heappush(heap,node3)
	
		node3.left=node1
		node3.right=node2
		l-=1
	root=heapq.heappop(heap)	
	return 	root

#finally...each character in the text is assigned a unique code by the following function(with the help of the tree we build earlier)
#final_d is used for encoding while rev_d is exactly reverse of final_d which is used for decoding of file

def build_finaldict(root,s,final_d,rev_d):
	if root is None:
		return 
	if root.left is None and  root.right is None:
		final_d[root.char]=s
		rev_d[s]=root.char
		return
	build_finaldict(root.left,s+'0',final_d,rev_d)
	build_finaldict(root.right,s+'1',final_d,rev_d)

# this is the last step for encoding a file....each character in the file is replaced with its code(actually we do it in a different file)...
# using the actual text and final_d the function creates a newtext(consisting of characters(0 and 1))...which is further converted to an array of integers
# padding is done to avoid mistake regarding size of newtext
def encode_text(final_d,text):
	new_text=""

	for c in text:
		new_text=new_text+final_d[c]
	padding=8-(len(new_text)%8)
	for i in range(padding):
		new_text=new_text+"0"

	new_text="{0:08b}".format(padding)+new_text
	arr=[]
	for i in range(0,len(new_text),8):
		ele=new_text[i:i+8]
		arr.append(int(ele,2))
	return arr


# the function accepts encoded text and the dictionary(as we created earlier) and gives the actual text as output
def decompress_help(text,hdict):
	output=""
	i=0
	s=""
	while i<len(text):
		s=s+text[i]
		if hdict.get(s,0)!=0:
			output=output+hdict[s]
			s=""
		i+=1

	return output

def compress(path):

	f_name,f_text=os.path.splitext(path)
	output_path=f_name+"_compressed.txt"

	with open(path,'r+') as file, open(output_path,'wb') as output:
		text=file.read()
		text=text.rstrip()
		d=build_dict(text)	
		a,b=build_heap(d)
		root=build_btree(a,b)
		rev_d={}
		final_d={}
		build_finaldict(root,"",final_d,rev_d)
		arr=encode_text(final_d,text)
		finalarr=bytes(arr)
		output.write(finalarr)


	return output_path,rev_d	


def decompress(path,hdict):

	f_name,f_text=os.path.splitext(path)
	output_path=f_name+"_decompressed.txt"


	with open(path,'rb') as file, open(output_path,'w') as output:
		bitstring=""
		byte=file.read(1)
		while byte:
			byte=ord(byte)
			bits=bin(byte)[2:].rjust(8,'0')
			bitstring+=bits
			byte=file.read(1)
		padding=bitstring[0:8]
		padding=int(padding,2)
		bitstring=bitstring[8:-padding]
		ans=decompress_help(bitstring,hdict)
		output.write(ans)
		

	return output_path
path=input()
com_path,help_dict=compress(path)
print(com_path)
decom_path=decompress(com_path,help_dict)
print(decom_path)

