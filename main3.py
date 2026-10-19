class India:
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most spoken language in India")

    def type(self):
        print("India is the developing country")

class USA:
    def capital(self):
        print("Wasington D.C is the capital of USA")

    def language(self):
        print("English is the most spoken language in USA")

    def type(self):
        print("USA is the developing country")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital
    country.language
    country.type
