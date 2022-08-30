"""
Task 3: Tim Tams

Daniel likes tim tams ... there's a packet of 11, he eats two at a time until there's only one left.

Please print this out.

Some variable: name, number_of_tim_tams
"""


# name = "Daniel"

# action = "has eaten 2 tim tams at a time, number of tim tams left is"

# number_of_tim_tams = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]#, "foo"]

# number_of_tim_tams_eaten = number_of_tim_tams[:(2*5)]
#
# print("number_of_tim_tams_eaten", number_of_tim_tams_eaten)
#
# print(number_of_tim_tams[0:10])
#
# print("number_of_tim_tams[:(2*5)]", number_of_tim_tams[:(2*5)])
#
# number_of_tim_tams[:(2*5)] = []
#
# print("number_of_tim_tams", number_of_tim_tams)
# print(name, action, number_of_tim_tams)

# print(number_of_tim_tams[-1])
# print(sorted(number_of_tim_tams))

# print(number_of_tim_tams)


name = "Daniel"
eaten_number_of_tim_tams = 2 #number of tim tams eaten at a time
stops_eating_at_this_number_of_tim_tams = 1
number_of_tim_tams = 22

print((name), "eats", (eaten_number_of_tim_tams), "tim tams at a time, until", (stops_eating_at_this_number_of_tim_tams), "tim tam(s) is/are left")

if number_of_tim_tams >= 20:
    print("No, don't do it. Put down the tim tam and go for a run,", (name))

while number_of_tim_tams >= stops_eating_at_this_number_of_tim_tams:
    print("Number of tim tams left is")
    print(number_of_tim_tams)
    number_of_tim_tams -= eaten_number_of_tim_tams


