#creationg a string, single quotes or double quotes
greeting = "Hello, World!"
name = 'Joe'
#This is a bad example
#complex_example = 'I'm not sure what to do here
complex_example = "I'm not sure what to do here"
complex_example = 'I\'m not sure what to do here'
#print(complex_example)


#String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
#print(full_name)
#print(first_name, last_name)
#f string
#print(f'This is a string. Hello {first_name} {last_name}.')

repeated_text = "Python " * 3
#print(repeated_text)

#Substrings
message = "The quick brown fox jumped over the lazy dog."
first_letter = message[0] #WE ALWAYS START COUNTING FROM 0
second_letter = message[1]
substring_example = message[10:15]
#print(substring_example)

#Getting the length of a string
#print(f'The length of the sentence is {str(len(message))}.')

#get the last half of a string?
lenth_of_full_string = len(message)
half_length = int(lenth_of_full_string/2)
#print(type(half_length))
#print(type(lenth_of_full_string))
#print(message[half_length:lenth_of_full_string])

#print("fox" in message)
#print("kangaroo" in message)
#print(message.find("fox"))
#print(message.replace("fox", "kangaroo"))

#string functions
#print(message.upper())
#print(message.lower())

#Split
the_output = message.split(" ")
#print(type(the_output))
#print(the_output)
a_list = ['apple', "banana", 2, 3.6]

#print(the_output[2])

#print(the_output[2:5])
a_list[2] = "testing"
#print(a_list)

added = the_output + a_list
#print(added)



primes = [2, 3, 5]
primes.append(7)
additional_primes = [11, 13]
primes.extend(additional_primes)
#print(primes)

unsorted_example = [9,3,4,5]
unsorted_example.sort()
#print(unsorted_example.sort())
#print(unsorted_example)
unsorted_example.reverse()
#print(unsorted_example)


#   A     B   C
#1    |     |    |
#2    |     |    |
#3    |     |    |


#   0     1   2
#0  A |  B  |  C  |
#1  D |  E  |  F  |
#2  G |  H  |  I  |

nested_lists= [["A", "B", "C"],["D", "E", "F"] , ["G", "H", "I"]]

print(nested_lists[0]) #entire first row
print(nested_lists[0][0]) #0 element of first row
print(nested_lists[1][1])
