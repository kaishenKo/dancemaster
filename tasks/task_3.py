"""
Task 3: Tim Tams

Daniel likes tim tams ... there's a packet of 11, he eats two at a time until there's only one left.

Please print this out.

Some variable: name, number_of_tim_tams
"""


name = "Daniel"

action = "has eaten 2 tim tams at a time, number of tim tams left is"

number_of_tim_tams = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

number_of_tim_tams_eaten = number_of_tim_tams[:(2*5)]

number_of_tim_tams[:(2*5)] = []

print(name, action, number_of_tim_tams)





