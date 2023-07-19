# Cryptopals

Set 1 was ok, but set 1 challenge 6 was incredibly confusing. I guess easy to implement, but wrapping my mind on the concept is just holy cow. Learned great concepts from this set, mainly **frequency anaylsis**. It's easy to just brute force and find the key if its just a small amount of text and just find the key. But what happens if the text is 1000+ characters and you have to XOR it agaisnt every printable character? That's where frequency analysis come to help and it makes it so much easier to find where the key as the scoring will tell you what the plaintext is.  

Also side note, another way to analyze words quipquip.com. To solve substituion ciphers, you can take the ciphertext and replace it with ACBEF...Z. And feed that sentence into quipquip and it should be able to solve the key. Pretty cool. 

## Set 1 Challenge 6: Break repeating-key XOR
Wow this one was a real head scratcher. I really struggled trying to figure this out. Unlike the other problems, this actually required some good amound of coding, meaning more than 30+ lines of code. To be completely honest, I had no problem drafting up the code, it was understanding the concept. Holy cow was that so confusing. First half I was doing something completely wrong because I didn't understand what I was doing. Took a lot of trial and error and thats exactly what this challenge called for. The concept was, ok youre given a huge wall of text. Now find the repeating XOR key that is used to create this ciphertext. Wow, great! Quickkkk shoutout to https://matthewdavidrodgers.com/posts/cryptopals-in-c-part-2/ and https://arpitbhayani.me/blogs/decipher-repeated-key-xor/ for helping me truly grasp the concept of this challenge. If I never came across those blogs, I would have gave up. 

Essentially though, 

The first task is to write a short function that can find the *hamming distance* of two strings. Hamming distance is basically the amount of differences between two strings, but on the binary level. So the string '0110' and '0000' would have a hamming distance of **2** because there is a difference of two characters between the two strings. 
