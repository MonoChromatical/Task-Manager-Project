import unittest
from task_manager_project import add_task, mark_task_completed


class TestTaskManager(unittest.TestCase):

    def test_add_task(self):
        tasks = []
        add_task(tasks, "Test")
        self.assertEqual(tasks, [("Test", False)])

    def test_mark_completed(self):
        tasks = [("Test", False)]
        mark_task_completed(tasks, 0)
        self.assertEqual(tasks[0][1], True)


if __name__ == "__main__":
    unittest.main()