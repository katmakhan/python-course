import asyncio

async def fetch_data():
	print("Start Fetching data function")
	await asyncio.sleep(2)
	var_data={'message':'Sucess'}
	print("done fetching")
	print(var_data)
	print("-----------------FETCH D")
	return var_data

async def print_numbers():
	print("Started Printing Numbers")
	for i in range(10):
		print(i)
		print("Wait Before")
		await asyncio.sleep(0.25)
		print("Wait Done")
		print("-----------------FETCH N")
	print("Finished Printing Numbers")
		
async def main():
	fetch_d=asyncio.create_task(fetch_data())
	fetch_n=asyncio.create_task(print_numbers())
	
	await fetch_d
	await fetch_n
	
asyncio.run(main())