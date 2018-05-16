# Define the stack structure // Edited==> add a reverse function
""""stack.items      ---> list of elements                <<<>>>
    stack.size()     ===> Return length                   <<<>>>  stack.isEmpty   ===> Return true/false
    stack.push(item) ===> appending item                  <<<>>>  stack.reverse() ===> reverse the stack to use as QUEUE
    stack.pop()      ===> popping last                    <<<>>>  stack.peek()    ===> Return the last element"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def reverse(self):
            for i in range (0,Stack.size(self)//2):
                self.items[i] , self.items[Stack.size(self)-1-i] = self.items[Stack.size(self)-1-i] , self.items[i]


# Define reverse list ===> Return reverse of a list
def reversed_list(alist):
    n = len(alist)
    for i in range (0,n//2):
        alist[i] , alist[n-1-i] = alist[n-1-i] , alist[i]
    return  alist


# Define Binary search ===> Return true or false
def binary_search(lista, item):
    first = 0
    last = len(lista) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if lista[midpoint] == item:
            found = True
        else:
            if item < lista[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


# Define Merge Sort ===> sorting the array ascending
'''
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(lefthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
'''

# Define digits characters ===> Return a list of numbers
def number_list():
    return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Define operators list ===> Return a list of sorted operators by asciis
def operators_list():
    return ['*', '+', '-', '/', '^']


# Define the allowed chars ===> Return a list of sorted chars by asciis , it can't be sorted automatically
def sorted_chars():
    sorted_c = [' ', '*', '+', '-', '.', '/','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '^']
    return sorted_c


# Define is operator? ===> Return true/false
def isoperator(c):
    if binary_search(operators_list(), c):
        return True
    return False


# Remove every extra white space
def remove_extra_spaces(statement):
    statement = statement.strip()
    for i in range(0, len(statement)):
        statement = statement.replace('  ', ' ')
    return statement


# Check eligible characters
def check_chars(statement):
    for i in range(0,len(statement)):
        if i < len(statement)-1 :
            #if isoperator(statement[i]) and statement[i+1] =='.' :
                #return 'syntax'
            if statement[i]=='.' and isoperator(statement[i+1]):
                return False
        if not binary_search(sorted_chars(),statement[i]) :
            return False
    return True

# Check if there is any missing brackets
'''
def check_brackets(statement):
    left = 0
    right = 0
    for char in statement:
        if char == '(':
            left = left + 1
        if char == ')':
            right = right + 1
    if left != right:
        return False
    return True
'''

# Check the duplicated operators from list 1 at list 2
def check_duplicated(list1, list2):
    for i in range(0, len(list2)):
        if binary_search(list1, list2[i]) and list2[i] == list2[i + 1]:
            return False
    return True


# General check on the statement ===> Return True statement only if there is no errors in brackets or chars
def checking_statement_chars(state):
    state = remove_extra_spaces(state)
    if check_chars(state) == 'syntax':
        return "this(.A) is not a valid syntax , replace with 0.A"
    if not check_chars(state):
        return "Invalid Chars"
    '''
    elif not check_brackets(state):
        return "brackets error"

    elif not check_duplicated(operators_list(),state):
        return "duplicated operators"
        '''
    return 'True'


# Define do maths calculations ===> Return the result of operation of  {+,-,*,/ or ^}
def do_math(op1,op2,operator):

    if operator == '+':
        return  op1 + op2

    elif operator == '-':
        return  op1 - op2

    elif operator == '*':
        return  op1 * op2

    elif operator == '/':
        if op2 == 0:
            return 'zero divide'
        return  op1 / op2

    else:
        if op1 == 0:
            return 'zero exp'
        return  op1 ** op2


# Split statement to a list of operands and operators
def split_equation(entered_eqn):
    eqn = remove_extra_spaces(entered_eqn)
    splitter_equation=[]
    digits = ''
    for i in range(0,len(eqn)):
        # if char is whitespace
        if eqn[i] == ' ':
            if  digits != '':
                splitter_equation.append(digits)
            digits = ''
        # if char is an operator
        elif isoperator(eqn[i]):
            if  digits != '':
                splitter_equation.append(digits)
            digits = ''

            if i != len(eqn)-1 and eqn[i]=='-' and(not isoperator(eqn[i+1])) and eqn[i+1] !=' ':
                digits = digits + eqn[i]
            else:
                splitter_equation.append(eqn[i])
        # if char is a digit
        else:
            digits = digits + eqn[i]
    if digits !='':
        splitter_equation.append(digits)
    return splitter_equation


# Define Calculate a reversed prefix eqn
def calculate(statem):
    global op1, op2
    temp = Stack()
    #if check(statem) == 'True statement':
    equate = reversed_list(split_equation(statem))
    for i in  equate:
        if not isoperator(i):
            temp.push(i)
        else:

            # getting first operand
            if temp.isEmpty():
                return 'error'
            elif isoperator(temp.peek()):
                return 'error'
            else:
                op1 = float(temp.pop())
            # getting second operand
            if temp.isEmpty():
                return 'error'
            elif isoperator(temp.peek()):
                return 'error'
            else:
                op2 = float(temp.pop())
            # pushing the result

            temp_result = (do_math(op1, op2, i))
            if temp_result =='zero divide':
                return 'zero divide'
            elif temp_result=='zero exp':
                temp.push('0')
            else:
                temp.push(str(temp_result))

    if temp.isEmpty():
        return 'error'
    elif isoperator(temp.peek()):
        return 'error'
    return float(temp.pop())


# format printing
def printing(result):
    if result.is_integer():
        print('= ',int(result))

    else:
        print('= ',float(result))


#############################################################################
########################  MAIN CODE   #######################################
#############################################################################

user_input= input("Please enter a prefix expression: ")    # Taking input from the user
while user_input != 'end':
    check = checking_statement_chars(user_input)
    if check != 'True':        # check if user has entered an eligible chars or a missing brackets
        print(check)
    else:
        result = calculate(user_input)
        if result == 'error':
            print('This is not prefix expression')
        elif result == 'zero divide':
            print('Not allowed to divide by 0')
        else:
            printing(result)
    user_input= input("Please enter a prefix expression or enter 'end' to terminate: ")    # Taking input from the user
print('ended')
