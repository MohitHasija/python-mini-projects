import re
from math import sqrt
from itertools import count, islice

class InputParser(object):
  exit_pointers = ['Q','q']
  
  def __init__(self):
    self.number_input_from_console = None
  
  def get_number_as_input_from_console(self):
    
    """
    This method is used to get a Number
    from console as a input.
    >Ask the user for input a positive number.
    >Check for the input as a real number or not.
    >If not, ask for input again or 'Q','quit','Quit' to exit.
    """
    exit_me = 'Not yet'
    
    #The regex to check for a positive number.
    num_format = re.compile("^[1-9][0-9]*\.?[0-9]+$") 
    
    while exit_me not in InputParser.exit_pointers:
      console_input = input("Please input the positive Number: ")
      if not re.match(num_format,console_input):
        exit_me = input("Please input a valid number."+ \
        "Press Q/q to Quit or hit any other key to continue.")
      else:
        try:
          print(console_input)
          self.number_input_from_console = int(console_input)
          return self.number_input_from_console
        except ValueError:
          exit_me = input("Please input the number again." + \
          "Press Q/q to Quit or hit any other key to continue.")
    return None
    

class NumberProcessor(object):
  def __init__(self, number):
    self.input_number = number
    
  def is_prime(self,number):
    return number > 1 and all(number%i for i in islice(count(2), int(sqrt(number)-1)))
    
    
  def get_prime_numbers(self,upper_limit=1000000):
    """
    Here we implement the logic to 
    find the prime Numbers.
    
    The logic is as follows:
    
    >>Check that the input number is less than the processable limit. 
    >>start from zero.
    >>In the loop check for each number as prime.
    >>If the number is prime, add it to the prime numbers list.
    >>Finally display all prime numbers.
    """
    UPPER_PROCESSABLE_LIMIT = upper_limit
    
    if self.input_number < UPPER_PROCESSABLE_LIMIT:
      return [number_to_check for number_to_check  in range(self.input_number) if self.is_prime(number_to_check) ]
    else:
      print("The upper limit of the number which can be processed has been reached.")
      return []
      
  def yield_prime_numbers(self):
    """
    Here we implement the logic to 
    yield the prime Numbers.
    
    The logic is as follows:
    
    >>start from zero.
    >>In the loop check for each number as prime.
    >>If the number is prime, add it to the prime numbers list.
    >>Finally display all prime numbers.
    """

    for number_to_check  in range(self.input_number):
      if self.is_prime(number_to_check):
        yield number_to_check
   
class GetPrimeNumbers(object):
  
  def __init__(self,upper_limit):
    self.upper_limit = upper_limit
    self.integer_input_parser = InputParser()
    input_number = self.integer_input_parser.get_number_as_input_from_console()
    if input_number:
      self.prime_number_getter = NumberProcessor(input_number )
    else:
      self.prime_number_getter = None
  
  def get_all_primes(self):
    if self.prime_number_getter:
      print("The prime numbers are: ")
      for x in self.prime_number_getter.get_prime_numbers(self.upper_limit):
        print("{} ,".format(x), end='' )
    else:
      pass
    
  def yield_all_primes(self):
    if self.prime_number_getter:
      print("The prime numbers are: ")
      for x in self.prime_number_getter.yield_prime_numbers():
        print("{} ,".format(x), end='' )
    else:
      pass
    
"""
  We test the code with upper limit of the piece of code till 1000.
  This upper limit of the prime numbers displayer can be changed afterwards as well.
"""
prime_numbers_displayer = GetPrimeNumbers(upper_limit=1000000000)
prime_numbers_displayer.get_all_primes()
prime_numbers_displayer.yield_all_primes()
