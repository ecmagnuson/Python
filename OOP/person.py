from datetime import datetime
today = datetime.today()

class PersonAge:
    
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        
    def get_age(self):
        print(f'{self.name}\'s age is: ')
        print(f'{abs(today.year - self.year)} years')
        print(f'{abs(today.month - self.month)} month')
        print(f'{abs(today.day - self.day)} days')
        
joe = PersonAge('Joe', 2000, 1, 9)

joe.get_age()
