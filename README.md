# Cryptopals

Set 1 was ok, but set 1 challenge 6 was incredibly confusing. I guess easy to implement, but wrapping my mind on the concept is just holy cow. Learned great concepts from this set, mainly **frequency anaylsis**. It's easy to just brute force and find the key if its just a small amount of text and just find the key. But what happens if the text is 1000+ characters and you have to XOR it agaisnt every printable character? That's where frequency analysis come to help and it makes it so much easier to find where the key as the scoring will tell you what the plaintext is.  

Also side note, another way to analyze words quipquip.com. To solve substituion ciphers, you can take the ciphertext and replace it with ACBEF...Z. And feed that sentence into quipquip and it should be able to solve the key. Pretty cool. 

## Set 1 Challenge 6: Break repeating-key XOR
Wow this one was a real head scratcher. I really struggled trying to figure this out. Unlike the other problems, this actually required some good amound of coding, meaning more than 30+ lines of code. To be completely honest, I had no problem drafting up the code, it was understanding the concept. Holy cow was that so confusing. First half I was doing something completely wrong because I didn't understand what I was doing. Took a lot of trial and error and thats exactly what this challenge called for. The concept was, ok youre given a huge wall of text. Now find the repeating XOR key that is used to create this ciphertext. Wow, great! Quickkkk shoutout to https://matthewdavidrodgers.com/posts/cryptopals-in-c-part-2/ and https://arpitbhayani.me/blogs/decipher-repeated-key-xor/ for helping me truly grasp the concept of this challenge. If I never came across those blogs, I would have gave up. 

The first task is to write a short function that can find the *hamming distance* of two strings. Hamming distance is basically the amount of differences between two strings, but on the binary level. So the string '0110' and '0000' would have a hamming distance of **2** because there is a difference of two characters between the two strings. You're gonna use the Hamming Distance to figure out what the keysize is, as the less difference two strings have against each other, it means they share something and that will be the key. Once I got the keysize it was now time to guess what the key was. Keysize is 29 btw. 

Finding the key was quite possibly the hardest part of this challenge. Trying to figure out what the logic was and what the hell it was telling me to do, was just confusing to me. I could not for the life of me wrap my head around the concept. You're only given 8 sentences of instructions and they're short af. "Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on." Like what the heck does that mean? I only understood after doing some heavy research. So then I finally got that it meant break the ciphertext into blocks of the key length. Right? Then once you have 29 blocks of however long the cipher text, you will then gather all the first values together, all the second values togher, and so on. So for example, in my implemenation, I got 100 blocks of 29 bytes, from breaking up the ciphertext. Now I take those 100 blocks, and I will group all the blocks[1] together and all the blocks[2] together. Does that make sense? So once I have done that, there's going to be a list that is size 29, right cuz the key is length 29? And each index in the list of 29 elements, will be another list with 100 elements, to represent the 100 [1] indexes. Does that makes sense? I hope it does, maybe take a quick break to try to draw it out and digest it. It took me a whole long time to grasp that. 

Once were done 'transposing' the ciphertext and gathered all the respective indexes together, we now XOR them. Right so remember how theres a list of 29 elements where each index contains 100 elements? Ok, were going to XOR all those 100 elements together. 

### quick example 
> **plaintext**: secretattack <br>
> **key**: ice <br>

To represent this problem:
> s e c r e t a t t a c k
> i c e i c e i c e i c e
