# class student:
#     def __init__(self,name,rollnumber,javamarks,pythonmarks):
#             self.name=name
#             self.rollnumber=rollnumber
#             self.javamarks=javamarks
#             self.pythonmarks=pythonmarks

# obj = student("siva","4v7",56,60)
# print(obj.name)
# print(obj.rollnumber)
# print(obj.pythonmarks)
# print(obj.javamarks)

# obj2=student("jatin","4v9",55,60)
# print(obj2.name)
# print(obj2.rollnumber)
# print(obj2.pythonmarks)




class student:
    def __init__(self,name,rollnumber,javamarks,pythonmarks):
           self.name=name
           self.rollnumber=rollnumber
           self.javamarks=javamarks
           self.pythonmarks=pythonmarks
    def alldetails(self):
          print(self.name)
          print(self.rollnumber)
          print(self.javamarks)
          print(self.pythonmarks)

        
obj = student("siva","4v7",56,60)
obj.alldetails()

obj2=student("jatin","4v9",55,60)
obj2.alldetails()