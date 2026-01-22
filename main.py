class Foydalanuvchi:
    def __init__(self, fullname, username, password, age, phone, email):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.age = age
        self.phone = phone
        self.email = email

    def show_info(self):
        print("Full name:", self.fullname)
        print("Username:", self.username)
        print("Password", self.password)
        print("Age:", self.age)
        print("Phone number:", self.phone)
        print("Email:", self.email)

fullname = input('toliq ismni kiriting: ')
username = input('ismni kiriting: ')
password = input('parol kiriting: ')
age = int(input('yosh kiriting: '))
phone = int(input('raqam kiriting: '))
email = input('email kiriting: : ')

user1 = Foydalanuvchi(fullname, username, password, age, phone, email)

user1.show_info()
