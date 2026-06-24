class calculator:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"the square is {self.n * self.n}")
        
    def cube(self):
        print(f"the cube is {self.n * self.n * self.n}")
        
    def squareroot(self):
        print(f"the square root is {self.n ** (1/2)}")        
        
a = calculator (n=int(input("Enter a number: ")))
a.square()
a.cube()
a.squareroot()   

# it is a calculator. which is only perform the square, cube and square root of a number.             
    