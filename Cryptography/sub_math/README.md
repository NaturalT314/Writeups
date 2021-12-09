**sub_math - JUSTCTF 2021**

**_________________________________________________________________________________________________________________**

First look at the python script provided:

![image](https://user-images.githubusercontent.com/74961214/145368713-2a4a74ff-bd05-44a7-8808-07bf5bc94969.png)

1.The flag is stored in a flag.txt and is read as text
2.Some cryptic function enc is defined
3.The flag is sent to enc and converted to bytes after
4.written as bytes to cipher.enc

Taking a look at cipher.enc:

![image](https://user-images.githubusercontent.com/74961214/145369514-7c7d4d4d-cefa-4c5b-ae9f-d80b9c3107e7.png)

**Solution**

The way I would go around solving this problem would be to analyze the encrypting function and try to reverse
```
return''.join([str((( 51415 & 5 + 314) | ord(t) << 15 ))  for t in flag ]) 
```
1. Iterating on every letter in our flag since flag is a string
```
for t in flag
```
2. A fancy way of generating the number 23, you can check using python
```
( 51415 & 5 + 314)
```
3. Multiplying the ASCII of t by 2*/*15
4. 
