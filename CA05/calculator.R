#Function1: add two numbers together
add_two_numbers <- function(num1, num2){ 
  num1 + num2 
}

#Function2: subtract one number from another
subtract_two_numbers <- function(num1, num2){ 
  num1 - num2 
}

#Function3: multiply two numbers
multiply_two_numbers <- function(num1, num2){ 
  num1 * num2 
}

#Function4: divide one number by another
divide_two_numbers <- function(num1, num2){ 
  if (num2 == 0) {
    'undefined' 
  } else {
    num1 / num2
  }
}

#Function5: exponentiate one number by another
exponentiate_two_numbers <- function(num1, num2){ 
  num1 ** num2 
}

#Function6: square a number
square <- function(num){ 
  num ** 2
}

#Function7: cube a number
cube <- function(num){ 
  num ** 3
}

#Function8: get the sqare root of a number (exponentiate by 0.5)
square_root <- function(num){ 
  if (num < 0) {
    'error' 
  } else {
    num ** 0.5
  }
}

#Function9: return the sine of x radians
my_sin <- function(num){
  sin(num)
}

#Function10: return the cosine of x radians
my_cos <- function(num){
  cos(num)
}