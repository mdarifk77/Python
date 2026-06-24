class employee:
    language = "Python"
    salary = 25000
    def getinfo(self):
        print(f"the language is {self.language}")
        print(f"the salary is {self.salary}")
arif = employee()
# arif.language = "JavaScript" 
# print(arif.language, arif.salary)
arif.getinfo()   
