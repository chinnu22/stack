class Stack:

    def __init__(self):
        self.st = []
        
        
    def push(self,ele):
        self.st.append(ele)
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele = self.st.pop()
            print(f"Element {ele} is removed from the stack")

    def search(self,searchEle):
        if self.is_empty():
            print("Stack is empty")
        else:
            for index,ele in enumerate(self.st):
                if ele == searchEle:
                    return index
            return -1


        
    def show(self):
        if self.is_empty():
            print("Stack is empty to display")
        else:
            print(self.st)



    def is_empty(self):
        return len(self.st) == 0



if __name__ == "__main__":
    st = Stack()
    opt_dict = {1:st.push,2:st.pop,3:st.search,4:st.show,5:exit}
    while True:
        print("1.Push 2.Pop 3.Search 4.Dislpay 5.Exit")
        try:
            ch = int(input("Enter your choice:"))
            if ch == 1:
                ele = input("Enter the element to push:")
                st.push(ele)
            elif ch == 2:
                st.pop()
            elif ch == 3:
                ele = input("Enter the element to search:")
                res =st.search(ele)
                if res!=-1:
                    print(f"Element {ele} found at location :{res}")
                else:
                    print(f"Element {ele} not found ")
            elif ch == 4:
                st.show()
            elif ch == 5:
                exit(0)
            else:
                raise ValueError

        except(ValueError,KeyError):
            print("Enter only numbers 1 to 5")