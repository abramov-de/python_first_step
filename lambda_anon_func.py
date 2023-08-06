def run_task(task):
    print("Before running task :")
    task()
    print("After running task.")


run_task(lambda: print("Task is complete !"))  # passing an anonymous function
important_task = lambda: print("Important task is complete !")
run_task(important_task)  # passing a lambda function
