import unittest
from Module_12_1.runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("John")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Alice")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    def test_challenge(self):
        runner1 = Runner("Bob")
        runner2 = Runner("Charlie")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)  # Ожидаем, что дистанция будет разной


# # Запуск тестов
if __name__ == '__main__':
    unittest.main()