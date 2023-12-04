# №1
import threading
import time

def fast_operation(a, b):
    result = a + b
    return result

def slow_operation(a):
    time.sleep(a)
    result = a ** 2
    return result

def execute_fast_operation(a, b):
    result = fast_operation(a, b)
    print("Быстрая операция, result:", result)

def execute_slow_operation(a):
    result = slow_operation(a)
    print("Медленная операция result:", result)

a = 2
b = 3

fast_thread = threading.Thread(target=execute_fast_operation, args=(a, b))
slow_thread = threading.Thread(target=execute_slow_operation, args=(a,))

fast_thread.start()
slow_thread.start()

fast_thread.join()
slow_thread.join()

print("Оба потока завершили выполнение.")

# №2
import asyncio

async def handle_phone_calls():
    while True:
        await asyncio.sleep(1)
        print("Обработка телефонных звонков")

async def handle_visitors():
    while True:
        await asyncio.sleep(2)
        print("Обработка посетителей")

async def book_flight_tickets():
    while True:
        await asyncio.sleep(3)
        print("Бронирование билетов на самолет")

async def control_meeting_schedules():
    while True:
        await asyncio.sleep(4)
        print("Контроль графиков встреч")

async def fill_documents():
    while True:
        await asyncio.sleep(5)
        print("Заполнение документов")

async def secretary():
    tasks = [
        handle_phone_calls(),
        handle_visitors(),
        book_flight_tickets(),
        control_meeting_schedules(),
        fill_documents()
    ]
    await asyncio.gather(*tasks)

asyncio.run(secretary())




