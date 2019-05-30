# Check if a book is existing in your collection
collectionOfBooks = ["The Alchemist", "How to win friends and influence people","The seven habbits of highly efffective people"]
print("Enter the name of the book")
bookToBeChecked = input()
for book in collectionOfBooks:
    if book == bookToBeChecked:
        print("Yes, I do have the book!")
        break
else:
        print("No, I do not have the book!")
