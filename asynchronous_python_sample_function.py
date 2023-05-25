
import asyncio

async def get_watches():
    await asyncio.sleep(3)
    print("richard mille")
    
    
    
async def fn():
    print('This is ')
    await get_watches()
    print('asynchronous programming')
    #await asyncio.sleep(3)
    print('and not multi-threading')
  
asyncio.run(fn())
