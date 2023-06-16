class Human:
    height = 180
    weight = 55
    def sleep(self, number_of_hours):
        print(self.weight * number_of_hours)
        # print("Human has gone to sleep")
    def walk(self):
        print("Human has gone to walk")

# Human
number_of_hours = int(input("Enter the number of hours you sleep:\n"))
man = Human()
man.sleep(number_of_hours)
man.walk()