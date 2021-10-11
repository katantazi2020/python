#def even_numbers(function):
    #def wrap(numbers):
        
        #print(function())
        #if numbers % 2 == 0:
        
           # return wrap
def even_numbers(function):
    def wrap(numbers):
        result = list(filter(lambda x: x % 2 == 0, numbers))
        return function(result)
    return wrap

@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))