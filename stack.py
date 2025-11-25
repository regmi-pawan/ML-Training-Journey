class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def push(self, items):
        if self.top == self.size - 1:
            print('stack overflow!!!!')
        else:
            self.top += 1
            self.stack[self.top] = items
            print(f"{items} is pushed into the stack")

    def pop(self):
        if self.top == -1:
            print('stack underflow!!!')
        else:
            removed = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"{removed} is popped from the stack")

    def peek(self):
        if self.top == -1:
            print("stack underflow!!!")
        else:
            print(f'{self.stack[self.top]} is the topmost value present in the stack')

    def display(self):
        if self.top == -1:
            print('stack underflow')
        else:
            print('The items present in the stack are:')
            for i in range(self.top, -1, -1):
                print(self.stack[i])


def main():
    size = int(input('enter the size of the stack'))
    s = Stack(size)

    while True:
        print('Menu: Stack operations\n')
        print('1. push')
        print('2. pop')
        print('3. peek')
        print('4. display')
        print('5. Exit')

        choice = input('Enter the choice to perfrom in the stack')

        if choice == '1':
            value = int(input('Enter the value'))
            s.push(value)
        elif choice == '2':
            s.pop()
        elif choice == '3':
            s.peek()
        elif choice == '4':
            s.display()
        elif choice == '5':
            print('Exiting...!!')
            break
        else:
            print('Invalid choices!!!')


if __name__ == "__main__":
    main()