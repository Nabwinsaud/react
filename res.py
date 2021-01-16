
#
import os


def main():
   print('Main func is here')


def user():
	user=input('Eneter the name:')
	try:
	    if user.isUpper():
	       print(user) 
Except:
      print('please type string')	


if __name__ =='__main__':
    main()
    user()