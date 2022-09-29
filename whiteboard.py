# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).		
# Example Input: ‘racecar’
# Example Output: True

# print(input("Type a word and I'll tell you if it's a palindrome: "))

# if input == input[::-1]:
#     return "That's a palindrome"
# else:
#     return "Not a palindrome"


# print(return)

# build a shopping cart
# takes in input
# stores input into dictionary
# user can add and remove items
# user can see current shopping list
# program runs in until quit
# upon quitting print shopping list


# def shopping_cart():

#     shopping_list = []
    
#     while True:

#         user_question = input("Welcome to you shopping list\n" + "Do you want to Store[s], Add[a], Delete[d], clear[c] or [q] to Quiz")

#         for ans in user_question:
#             user_question.lower() == 'a'
#             add = input("what would you like to add? ")
#             shopping_list.append(add)
        
#         if user_question.lower() == 's':
#             print(f"Here's you list {shopping_list}")
            

        

#         #show = input('s')
#         # add = input('a')
#         # delete = input('d')
#         # clear = input('c')


# shopping_cart()

def shopping_cart():

    shopping_list = []

    while True:

        user_question = input("\nWelcome to your shopping list\n\n" + "Do you want to Show [s], Add [a], Delete [d], clear [c] or [q] to Quit: ")

        if user_question.lower() == 's':
            print(f"\nYour current shopping list:\n{shopping_list}")

        if user_question.lower() == 'a':
            add = input("what would you like to add? ")
            shopping_list.append(add)
            print(f"\nYour current shopping list:\n{shopping_list}")
        
        if user_question.lower() == 'd':
            remove = input("which item would you like to remove? ")
            shopping_list.remove(remove)
            print(f"\n{remove} was removed from your shopping list.\n\n Here is your updated list:\n\n{shopping_list}\n")
            # if len(shopping_list) == 0:
            #     print("Nothing to remove")
        if user_question.lower() == 'c':
            shopping_list.clear()
            print(f"\nYour shopping list has been cleared... no going back...\n") 

        if user_question.lower() == 'q':
            print(f"\nHere's your shopping list... did you forget anything?\n{shopping_list}")
            break

shopping_cart()



