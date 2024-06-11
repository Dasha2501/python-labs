from datetime import date, datetime, timedelta
from typing import List, Optional, Tuple

class Task:
    def __init__(self, title: str, description: str, due_date: date, status: str = "Pending", priority: str = "Medium", notes: str = "", duration: int = 0, recurrence: str = "", dependencies: List["Task"] = []):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.dependencies = dependencies

    def is_due_today(self) -> bool:
        return self.due_date == date.today()

class Schedule:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.history.append(("added", task))

    def remove_task(self, task_title: str):
        task = self.get_task(task_title)
        if task:
            self.tasks.remove(task)
            self.history.append(("removed", task))

    def get_task(self, task_title: str) -> Optional[Task]:
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def list_overdue_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.due_date < date.today()]

    def list_tasks_due_today(self) -> List[Task]:
        return [task for task in self.tasks if task.is_due_today()]

    def sort_tasks_by_due_date(self) -> List[Task]:
        return sorted(self.tasks, key=lambda task: task.due_date)

    def update_task(self, task_title: str, **kwargs):
        task = self.get_task(task_title)
        if task:
            for key, value in kwargs.items():
                setattr(task, key, value)
            self.history.append(("updated", task))

    def weekly_schedule(self, start_date: date) -> List[Task]:
        end_date = start_date + timedelta(days=6)
        return [task for task in self.tasks if start_date <= task.due_date <= end_date]

    def monthly_schedule(self, year: int, month: int) -> List[Task]:
        first_day = date(year, month, 1)
        last_day = date(year, month + 1, 1) - timedelta(days=1)
        return [task for task in self.tasks if first_day <= task.due_date <= last_day]

    def list_tasks_by_priority(self, priority: str) -> List[Task]:
        return [task for task in self.tasks if task.priority == priority]

    def save_to_file(self, filename: str):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.status},{task.priority},{task.notes},{task.duration},{task.recurrence},{','.join([dep.title for dep in task.dependencies])}\n")

    def load_from_file(self, filename: str):
        self.tasks = []
        with open(filename, "r") as file:
            for line in file:
                title, description, due_date_str, status, priority, notes, duration_str, recurrence, dependencies_str = line.strip().split(",")
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                duration = int(duration_str) if duration_str else 0
                dependencies = [self.get_task(dep_title) for dep_title in dependencies_str.split(",")] if dependencies_str else []
                task = Task(title, description, due_date, status, priority, notes, duration, recurrence, dependencies)
                self.add_task(task)

    def list_tasks_with_notes(self) -> List[Task]:
        return [task for task in self.tasks if task.notes]

    def mark_as_completed(self, task_title: str):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
            self.history.append(("updated", task))

    def list_completed_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.status == "Completed"]

    def find_task_by_keyword(self, keyword: str) -> List[Task]:
        return [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]

    def check_deadlines(self) -> List[Task]:
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        return [task for task in self.tasks if today <= task.due_date <= tomorrow]

    def list_all_tasks(self) -> List[Task]:
        return self.tasks

    def list_tasks_by_duration(self, min_duration: int, max_duration: int) -> List[Task]:
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def task_history(self) -> List[Tuple[str, Task]]:
        return self.history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_recurring_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, task_title: str, reminder_date: date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self) -> float:
        if not self.tasks:
            return 0.0
        completed_tasks = len(self.list_completed_tasks())
        total_tasks = len(self.tasks)
        return (completed_tasks / total_tasks) * 100