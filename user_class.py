class User:
    """This class describes a user"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name,
        self.last_name = last_name
    
    def describe_user(self):
        """Description of a user"""
        long_name = f"This is {self.first_name} {self.last_name}"
        return long_name.title()

    def greet_user(self):
        """Greet the user"""
        greeting_message = f"Hello Mr. {self.last_name}, nice to meet you"
        return greeting_message.title()


user_1 = User("albert", "einstein")
print(user_1.describe_user())
print(user_1.greet_user())
