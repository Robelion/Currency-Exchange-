"""
User interface for module currency

When run as a script, this module prompts the user for two currencies
and amount.
It prints out the result of converting the first currency to the second.

Author: Robel Ayalew rsa83 
Date:   9/19/18
"""
import a1

first = str(input("3-letter code for original currency: "))
second = str(input("3-letter code for the new currency: "))
last = float(input("Amount of the original currency: "))

a = a1.exchange(first, second, last)

print ("You can exchange " + str(last) + " " + first + " for " + str(a) + " " +
      second + ".")
