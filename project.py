class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        name = self.name.upper()
        return name

    def age(self, current_year):
        age = int(current_year) - int(self.birthyear)
        return age
    

user = User("John", 1999)
print(user.age(2023))
print(user.get_name())