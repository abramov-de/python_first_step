import time
import asyncio


async def func1(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print('function 1 complete')


async def func2(x):
    print(x ** 0.5)
    await asyncio.sleep(3)
    print('function 2 complete')


# async def main():
#     await func1(4)
#     await func2(4)


async def main():
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))

    print(type(task1))
    print(task1.__class__.__bases__)

    await task1
    await task2


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))

# print(type(func1))
# print(type(func1(4)))
