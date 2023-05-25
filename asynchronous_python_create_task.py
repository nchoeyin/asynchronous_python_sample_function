import asyncio

async def fetch_data(): #async keyword creates a wrapped function which can be called as coroutine
    print('start fetching')
    await asyncio.sleep(2) #Since this function statement has to wait for 2 seconds, the execution is forwarded to the task2 in the main function
    print('done fetching')
    return {'data':1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25) #To run  a coroutine, we need to await or add it to event loop by creating task to run concurrently

async def main():
    task1 = asyncio.create_task(fetch_data()) #Since this function returns a json or a value in general, it is called to provide a future 
    task2 = asyncio.create_task(print_numbers()) #print_numbers function prints 0-7 (0.25*8=2seconds)and after exact 2 seconds, returns the execution to fetch_data function's print statement
    value = await task1 
    print(value)
    await task2 #await ensures that task2 is eventually completed

asyncio.run(main()) #The execution runs from here
#An event loop is started here using the asyncio.run which takes in coroutine as the entry point

'''
Output:
start fetching
0
1
2
3
4
5
6
7
done fetching
{'data': 1}
8
9
'''
