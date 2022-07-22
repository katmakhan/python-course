from multiprocessing.pool import ThreadPool

#Function that takes 2 argument
def function1(arg1,arg2):
	while True:
		print("This is working with ",arg1,arg2)
		
def main():
	pool=ThreadPool(3)
	#using pool.starmap for multiple argument function
	pool.starmap(function1,[("val_arg1","val_arg11"),
	("val_arg2","val_arg22"),
	("val_arg3","val_arg33")])
	