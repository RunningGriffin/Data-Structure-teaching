# Trees

If you have a collection on pens or pencils you still find yourself grabbing the same few more often than the others. The tree data structure is optimal for organization in this way where we put the most common needed things towards the top of the root and less needed things towards the bottom.

**How is this form of data Structure useful?**

- This drasically reduces the average lookup time for commonly serached for nodes

- This orginizes the data in a way to make the most common nodes more accessable and putting less common searched for nodes underneath it

## Example 1

This is commonly used in binaray to reduce the average bit size to encode an image or text. 

![Bianary Encode tree](binaryencodetree.png)

This helps enable the use have potential to need less bits to be able to decifer what a letter or number is by making it so more common nodes need less bits to map to. If we were given a random paragraph, on average we would need less bits using a tree if the common alternative would be using bits equal to the highest potential outcome. In example if there were 16 possible characters in this paragraph we would have to assign each charcater 0 - 11111 alphebetically, the most commone used character could be anywhere from 1 to 5 bits. But with a tree we can decrease the scope so that our most common charcter could be 2 or even 1 bit consistantly. thus reducing the overall memory space needed to decode.
