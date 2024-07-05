from prettytable import PrettyTable

class ToDoList():
    def __init__(self):
        self.p = PrettyTable()
        print("This is simple Todo List Application\n")

        self.header = ["To Do List"]
        self.data = ["Its a nice day to work","keep track of your work here :)"]
        self.p.field_names = self.header
        self.showToDoList()
        
    def welcome(self):
        print("\n\nwhats in your mind?\n1.create todolist\n2.Update todolist\n3.track todolist\nPRESS ANY KEY OTHER KEY TO EXIT\n")
        c = input("Enter your choice:\t")
        if c == '1':
            self.createToDoList()
        elif c == '2':
            self.updateToDoList()
        elif c == '3':
            self.showToDoList()
        else:
            pass

    def showToDoList(self):
        
        self.p.field_names = self.header
        for data in self.data:
            self.p.add_row([data])
        print(self.p)
        self.p.clear_rows()
        self.welcome()

    def createToDoList(self):
        self.data.clear()
        print("\npress 0 when done adding task\n")
        task = ''
        i = 1
        while(1):
            
            if task == '0':
                break
            else:
                task = input("Enter the task else Press 0 when done:\t")
                if task !='0':
                    self.data.append(str(i)+". "+task)
                    i=i+1
                    
        print("New ToDo-List is created :)")
        self.welcome()

    def updateToDoList(self):
        while(1):
            row = int(input("Enter the task no. you have completed to update the todo-list Else press 0 to exit:\t"))
            if row != 0:
                self.data[row-1] = self.data[row-1]+u'\u2713'
                print("todo list is updated")
            else:
                break

        self.welcome()
        
        

if __name__ == '__main__':
    ob = ToDoList()