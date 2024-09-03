#1. Python Sets Adventure
#Objective: The aim of this assignment is to deepen your understanding and application of Python sets.


#Task 1: Flight Route Comparison Imagine you work for an airline and need to compare
# the flight routes of your airline with a competitor.


# You have two sets of flight destinations, one for each airline. Write a Python program to find out:
#1. Destinations that both airlines fly to.
#2. Destinations unique to your airline.
#3. Whether there are any destinations that neither airline shares.

#Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


#1. Destinations that both airlines fly to.
print("Destinations that both airlines fly to")
for our_route in our_routes:
    if our_route in competitor_routes: 
        print(our_route)
    break
#2. Destinations unique to your airline.
    print("Destinations unique to your airline.")
for our_route in our_routes:
    if our_route not in  competitor_routes:
        print(our_route)
    break
#3. Whether there are any destinations that neither airline shares.
print("destinations that neither airline shares")
for our_route in our_routes:
    if our_route not in  competitor_routes:
         print(our_route)
    break

# 2. Set Operations in Data Analysis
# Task 1: Duplicate Entries Cleanup 

def remove_duplicates(customer_ids):
    unique_ids = set()
    for customer_id in customer_ids:
        unique_ids.add(customer_id)
    unique_ids_list = list(unique_ids)
    unique_ids_list.sort()
    for unique_id in unique_ids_list:
        print(unique_id)
    # return unique_ids   # unique_ids  is a set
    # We can return unique_ids  or  unique_ids_list 
    return unique_ids_list

# Example usage:
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_customer_ids = remove_duplicates(customer_ids)
print(unique_customer_ids)
