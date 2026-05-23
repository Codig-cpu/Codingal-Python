class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language in India")

class USA():
    def capital(self):
        print("Washington , D.C is the capital of USA")

    def language(self):
        print("English is the primary language of USA")

obj_ind1=India()
obj_usa2=USA()

for country in (obj_ind1 , obj_usa2):
    country.capital()
    country.language()