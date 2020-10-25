import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform
    
def my_func(cons):
	if cons == True:
		for i in range (100):
			if i%2==0:
				print(i, end=' ')
	elif cons == False:
		for i in range (100):
			if i%2==1:
				print(i, end=' ')

