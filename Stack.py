"""
# Project 4
# Name: Chris Maidlow
# PID: A49592527
"""

class Stack:
    """
    Stack class
    """

    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"
        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))
    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False
        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1
        return True
    def stack_size(self):
        """
        This simple function returns the current size of the Stack
        :return: size attribute
        """
        #return size
        return self.size
    def is_empty(self):
        """
        This function test whether the Stack is currently empty
        :return: True if empty, false otherwise
        """
        #return True if size is 0
        if self.size == 0:
            return True
        else:
            return False
    def top(self):
        """
        This function allows the user to see the top item of the Stack
        :return: None if stack is empty, last item in Stack.data otherwise
        """
        #return none if no value
        if self.is_empty() is True:
            return None
        return self.data[self.size - 1]
    def push(self, val):
        """
        Simply append value to the end of stack without using append
        :param val: this parameter is the value that is being appended to the end of the stack
        :return: no return
        """
        #check size and double capacity
        if self.size == self.capacity:
            self.grow()
        #add value to top of stack
        self.data[self.size] = val
        self.size += 1
    def pop(self):
        """
        Pop item off of the top of the stack and return it, list size is decremented
        :return: the top item of the stack
        """
        #if empty can't pop
        if self.is_empty() is True:
            return None
        #save top in temp value
        top = self.data[self.size - 1]
        #last value is now none
        self.data[self.size - 1] = None
        #decrement size
        self.size -= 1
        #if size below threshold call shrink
        if self.size <= (self.capacity//2):
            self.shrink()
        return top
    def grow(self):
        """
        Function creates a new list of none values twice the capacity,
        fills it with the values of self.data and then
        sets self.data as the new array.
        :return: no return
        """
        #create new array
        old_cap = self.capacity
        self.capacity = (self.capacity * 2)
        new_array = [None] * self.capacity
        #add values from old array
        for i in range(0, old_cap):
            new_array[i] = self.data[i]
        self.data = new_array
    def shrink(self):
        """
        Like the prior function, creates new array of none values half the size of self.data
        then iterates through self.data assigning values to new array and then swaps.
        :return: no return
        """
        #check for minimum cap
        if self.capacity == 2:
            return
        #create new array
        self.capacity = (self.capacity // 2)
        new_array = [None] * self.capacity
        #add values from old array and swap
        for i in range(0, self.size):
            new_array[i] = self.data[i]
        self.data = new_array
def reverse(stack):
    """
    Pops each item off of the top of variable stack and pushes it onto the new stack
    effectively reversing the order
    :param stack: The stack to be reversed
    :return: The stack but reversed
    """
    #create new stack
    fresh_stack = Stack(stack.capacity)
    i = 0
    #pop from old array and add to new
    while i <= stack.capacity + 1:
        plate = stack.pop()
        fresh_stack.push(plate)
        i += 1
    return fresh_stack
def replace(stack, old, new):
    """
    This class iterates through stack.data pushing the values onto a new stack.
    Whenever a desired "old" value is found via the parameters it instead pushes new
    onto the new stack
    :param stack: Stack to replace values in
    :param old: value to be replaced
    :param new: value to replace old
    :return: Stack with replacement values
    """
    #create new stack
    fresh_stack = Stack(stack.capacity)
    #if item matches old value push new val instead
    for item in stack.data:
        if item == old:
            fresh_stack.push(new)
        else:
            fresh_stack.push(item)
    return fresh_stack
    