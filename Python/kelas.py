import datetime as dt


# Membuat class Member
class Members:
    free_days = 365

    def __init__(self, username, fullname):
        # memberikan atribut dan nilai
        self.username = username
        self.fullname = fullname
        # Memberikan default value pada atribtut
        self.date_joined = dt.date.today()
        self.active = True
        self.hari = dt.timedelta(days=Members.free_days)
        self.free_expires = dt.date.today() + self.hari
        # Default secret code is nothing
        self.secret_code = ""

    # Method
    def show_dateJoined(self):
        return f"{self.username} joined on {self.date_joined:%d-%m-%Y}"

    # Method
    def activated(self, yesno):
        self.active = yesno

    # Method
    def get_status(self):
        return f"{self.fullname} is an Member"

    # Method Option 2
    @classmethod
    def setfreedays(cls, days):
        cls.free_days = days

    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%I:%m %p}"


# Inheritance Class
class Admin(Members):
    expiry_days = 365.2422 * 100

    # Subclass Parameter
    def __init__(self, username, fullname, secret_code):
        # pass member parameters on up to Member class
        super().__init__(username, fullname)
        # Assign the remaining parameter to this object
        self.secret_code = secret_code

    def get_status(self):
        return f"{self.fullname} is an Admin"


class User(Members):
    def get_status(self):
        return f"{self.fullname} is an User"


new_guys = Members('Mukti', 'Mukti Dwi Jatmoko')
# cetak class
print(new_guys)
print(type(new_guys))
# changeing the value of a attribute
new_guys.username = 'King Mukti'
print(new_guys.username)
print(new_guys.fullname)
print(new_guys.date_joined)
new_guys.active = False
print(new_guys.active)
# Alternative 1 call the method
print(new_guys.show_dateJoined())
# Alternative 3 call the method
print(Members.show_dateJoined(new_guys))
# Passing parameter to methods
print(new_guys.active)
new_guys.activated(True)
# Using class variabel call
print(new_guys.free_expires)
# call method option 2
new_guys.setfreedays(730)
print(new_guys.free_expires)
# call static method
print(new_guys.currenttime())


print("=" * 50)
Ann = Admin('Annie', 'Annie Muktia', 'hellowordl')
print(Ann.username, Ann.fullname, Ann.secret_code, Ann.expiry_days)
# calling the method
print(Ann.show_dateJoined())
print(Ann.get_status())

print("*" * 50)
John = User('Johnie', 'John Doe')
print(John.username)
print(John.fullname)
print(John.secret_code)
print(John.free_expires)
# calling the method
print(John.show_dateJoined())
print(John.get_status())

print("*" * 50)
# print(help(Admin))