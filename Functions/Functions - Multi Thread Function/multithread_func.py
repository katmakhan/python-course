from multiprocessing.pool import ThreadPool

#Function that takes only one argument
def function1(arg1):
	while True:
		print("This is working with ",arg1)
		
def main():
	pool=ThreadPool(3)
	#using pool.map for 1 argument function
	pool.map(function1,[("val_arg1"),
	("val_arg2"),
	("val_arg3")])
	