# Challenge Summary
<!-- Description of the challenge -->
Write a function called repeated word that finds the first word to occur more than once in a string
## Whiteboard Process
<!-- Embedded whiteboard image -->
![](code-challenges/challenge-31.png)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
create a function called repeated_word that take a string with multiple words
check if the string is empty
find the first word in the string
split all the string to array and remove the marks and change it to lower case
check if the word is repeated or not by looping through the string and checking the hash table if it contain the word or not

Big O:
Time--> O(n)
space--> O(n)

