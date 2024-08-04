s1 = "Make a lot of Money"
s2 = "Buy NOW"
s3 = "Subscribe to this"
s4 = "Click this to win Cars, Bikes and many more"
s5 = "Follow this account ASAP"
s6 = "Win coupons and gift cards here"

comment = input("Enter your comment: ")

if((s1 in comment) or (s2 in comment) or (s3 in comment) or (s4 in comment) or (s5 in comment) or (s1 in comment)):
    print("This comment is hidden from the admin as it is noticed as spam")
    
else:
    print("Your comment will be displayed to the admin as it contains no spam content and \n  Your comment is: ", comment)
