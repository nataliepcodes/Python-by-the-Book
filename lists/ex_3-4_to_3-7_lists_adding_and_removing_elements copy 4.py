# 3-4 guest list: make a list that includes at least 3 people to invite to dinner
# use a list to print a message to each person

guest_list = ["Anne", "Peter", "Marie"]
print(guest_list)
print(f"Dear {guest_list[0]}, you have been invited to dinner!")
print(f"Dear {guest_list[1]}, you have been invited to dinner!")
print(f"Dear {guest_list[2]}, you have been invited to dinner!")

# 3-5 changing guest list: one of the guests cannot make it, invite someone else
# print who can't make it
print("Anne can't make it")
# remove from the list
guest_list.remove('Anne')
print(guest_list) #['Peter', 'Marie']
# add a new guest
guest_list.insert(0, "George")
print(guest_list)
print(f"Dear {guest_list[0]}, you have been invited to dinner!")
print(f"Dear {guest_list[1]}, you have been invited to dinner!")
print(f"Dear {guest_list[2]}, you have been invited to dinner!")

# 3-6 more guests: you found a bigger dinner table, invite 3 more guests
print(f"Dear {guest_list[0]}, {guest_list[1]} and {guest_list[2]} I have found a bigger table and will invite 3 more guests.")
guest_list.insert(0, "Lucy")
guest_list.insert(2, "Rufus")
guest_list.append("Kate")
print(guest_list)
print(f"Dear {guest_list[0]}, you have been invited to dinner!")
print(f"Dear {guest_list[1]}, you have been invited to dinner!")
print(f"Dear {guest_list[2]}, you have been invited to dinner!")
print(f"Dear {guest_list[3]}, you have been invited to dinner!")
print(f"Dear {guest_list[4]}, you have been invited to dinner!")
print(f"Dear {guest_list[5]}, you have been invited to dinner!")

# 3-7 shrinking guest list: dinner table can't arrive on time, now there is space only for 2 guests
# send a message notifying that only 2 people can be invited for dinner
print(f"Dear {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]} and {guest_list[5]} apologies but a dinner table won't arrive on time, now I can invite only two guests.")

# use pop() to remove guest from list one at a time until only 2 names remain
# after removing a name, send them a message that you cannot invite them

print(f"\nInitial List >> {guest_list}\n")
removed_guest = guest_list.pop()
print(guest_list)
print(f"Dear {removed_guest}, unfortunately I cannot invite you for dinner anymore!\n")
removed_guest = guest_list.pop()
print(guest_list)
print(f"Dear {removed_guest}, unfortunately I cannot invite you for dinner anymore!\n")
removed_guest = guest_list.pop()
print(guest_list)
print(f"Dear {removed_guest}, unfortunately I cannot invite you for dinner anymore!\n")
removed_guest = guest_list.pop()
print(guest_list)
print(f"Dear {removed_guest}, unfortunately I cannot invite you for dinner anymore!\n")

# use del to delete the last two guests from the list
del guest_list[0]
del guest_list[0]
print(guest_list)