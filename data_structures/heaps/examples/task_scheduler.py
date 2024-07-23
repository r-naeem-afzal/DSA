import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from heaps.min_heap import MinHeap


class TaskScheduler:
    def __init__(self) -> None:
        self.tasks = MinHeap()

    def add_task(self, task: str, priority: int) -> None:
        self.tasks.insert((priority, task))
        print(f'Task "{task}" added to the scheduler.')

    def get_next_task(self) -> None:
        task = self.tasks.extract_min()
        if task:
            print(f'Next task: "{task[1]}"')
        else:
            print("No tasks in the scheduler.")

    def show_tasks(self) -> None:
        tasks = self.tasks.heap
        if tasks:
            print("Tasks in Scheduler:", [task[1] for task in tasks])
        else:
            print("No tasks in the scheduler.")

    def show_priority(self) -> None:
        tasks = self.tasks.heap
        if tasks:
            print("Task priorities:", [task[0] for task in tasks])
        else:
            print("No tasks in the scheduler.")

    def show_all(self) -> None:
        tasks = self.tasks.heap
        if tasks:
            print("Tasks in Scheduler:")
            for task in tasks:
                print(f'Priority: {task[0]}, Task: "{task[1]}"')
        else:
            print("No tasks in the scheduler.")

    def clear_all(self) -> None:
        self.tasks.heap = []
        print("All tasks cleared from the scheduler.")


if __name__ == "__main__":
    task_scheduler = TaskScheduler()
    task_scheduler.add_task(
        "Task 1", 3
    )  # Output: Task "Task 1" added to the scheduler.
    task_scheduler.add_task(
        "Task 2", 1
    )  # Output: Task "Task 2" added to the scheduler.
    task_scheduler.add_task(
        "Task 3", 2
    )  # Output: Task "Task 3" added to the scheduler.
    task_scheduler.show_all()
    # Output: Tasks in Scheduler:
    # Priority: 1, Task: "Task 2"
    # Priority: 3, Task: "Task 1"
    # Priority: 2, Task: "Task 3"
    task_scheduler.get_next_task()  # Output: Next task: "Task 2"
    task_scheduler.get_next_task()  # Output: Next task: "Task 3"
    task_scheduler.get_next_task()  # Output: Next task: "Task 1"
    task_scheduler.get_next_task()  # Output: No tasks in the scheduler.
    task_scheduler.show_all()  # Output: No tasks in the scheduler.
    task_scheduler.clear_all()  # Output: All tasks cleared from the scheduler.
    task_scheduler.show_all()  # Output: No tasks in the scheduler.
