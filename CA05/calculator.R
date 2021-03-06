####################################################################################
#                           Calculator Functions
####################################################################################

# Function1: add two numbers together
add_two_numbers <- function(num1, num2){ 
  if (is.numeric(num1) & is.numeric(num2))
  {
    num1 + num2 
  } else {
    'error'
  }
}

# Function2: subtract one number from another
subtract_two_numbers <- function(num1, num2){ 
  if (is.numeric(num1) & is.numeric(num2))
  {
    num1 - num2 
  } else {
    'error'
  }
}

# Function3: multiply two numbers
multiply_two_numbers <- function(num1, num2){ 
  if (is.numeric(num1) & is.numeric(num2))
  {
    num1 * num2 
  } else {
    'error'  
  }
}

# Function4: divide one number by another
divide_two_numbers <- function(num1, num2){ 
  if (is.numeric(num1) & is.numeric(num2)) {
    if (num2 == 0) {
      'undefined' 
    } else {
      num1 / num2
    }
  } else {
    'error'
  }
}

# Function5: exponentiate one number by another
exponentiate_two_numbers <- function(num1, num2){ 
  if (is.numeric(num1) & is.numeric(num2))
  {
    num1 ** num2
  } else {
    'error'  
  }
}

#Function6: square a number
my_square <- function(num){ 
  if (is.numeric(num))
  {
    num ** 2
  } else {
    'error'  
  }
}

# Function7: cube a number
my_cube <- function(num){ 
  if (is.numeric(num))
  {
    num ** 3
  } else {
    'error'  
  }
}

# Function8: get the sqare root of a number (exponentiate by 0.5)
my_sqrt <- function(num){ 
  if (is.numeric(num) & num > 0)
  {
    num ** 0.5
  } else {
    'error'  
  }
}

# Function9: return the sine of x radians
my_sin <- function(num){
  if (is.numeric(num))
  {
    sin(num)
  } else {
    'error'  
  }
}

# Function10: return the cosine of x radians
my_cos <- function(num){
  if (is.numeric(num))
  {
    cos(num)
  } else {
    'error'  
  }
}

####################################################################################
#                           Calls
####################################################################################

# Test add_two_numbers function
add_two_numbers(5,3)
add_two_numbers(4,0)
add_two_numbers('fred',0)

# Test subtract_two_numbers function
subtract_two_numbers(5,3)
subtract_two_numbers(4,0)
subtract_two_numbers(3,4)
subtract_two_numbers('fred',4)

# Test multiply_two_numbers function
multiply_two_numbers(5,3)
multiply_two_numbers(4,0)
multiply_two_numbers(3,-4)
multiply_two_numbers(3,'fred')

# Test divide_two_numbers function
divide_two_numbers(6,2)
divide_two_numbers(6,0)
divide_two_numbers(6,-2)
divide_two_numbers(6,'fred')

# Test exponentiate_two_numbers function
exponentiate_two_numbers(5,3)
exponentiate_two_numbers(4,1)
exponentiate_two_numbers(4,0)
exponentiate_two_numbers(2,-2)
exponentiate_two_numbers(2,'fred')

# Test my_square function
my_square(3)
my_square(5)
my_square(-3)
my_square('fred')

# Test my_cube function
my_cube(2)
my_cube(5)
my_cube(-2)
my_cube('fred')

# Test my_sqrt function
my_sqrt(9)
my_sqrt(25)
my_sqrt(5)
my_sqrt(-4)
my_sqrt('fred')

# Test my_sine function
my_sin(3)
my_sin(-3)
my_sin(0)
my_sin('fred')

# Test my_cos function
my_cos(0)
my_cos(3)
my_cos(-3)
my_cos('fred')
