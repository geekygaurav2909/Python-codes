class User:
    
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0


user_1 = User("001", "Gaurav")

print(user_1.followers)



# user_2 = User()

# user_2.id = 54
# user_2.name = "Anjula"

# print(user_1.name, "WEDS", user_2.name)