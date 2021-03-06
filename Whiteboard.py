"""
Given the following array of values, print out all the elements in reverse order, with each element on a new line.
For example, given the list
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Your output should be
0
1
2
3
4
5
6
7
8
9
10
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""

# Create a arrar:

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Use for loop to print the elements:

arr.reverse()
for i in arr:
    print(i)


"""
Given a hashmap where the keys are integers, print out all of the values of the hashmap in reverse order, ordered by the keys.
For example, given the following hashmap:
{
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}
The expected output is:
widescreen
views
tissue
coffee
inbox
vs code
alloc
bottle
window
since "widescreen" has the largest integer key, "views" has the second largest, etc.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""
# create a dictionary:
hmap = {
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}
# Create a list of keys:
keys = []
for k, v in hmap.items():
  keys.append(k)

# Sort and reverse the list
keys2 = sorted(keys)
keys2 =reversed(keys2)

# Print the values:
for i in keys2:
  print(hmap[i])
