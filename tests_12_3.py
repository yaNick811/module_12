import unittest

def skip_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_run(self):
        from test_runner import Runner
        runner = Runner("Test", speed=5)
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_frozen
    def test_walk(self):
        from test_runner import Runner
        runner = Runner("Test", speed=5)
        runner.walk()
        self.assertEqual(runner.distance, 5)

    @skip_frozen
    def test_challenge(self):
        from test_runner import Runner
        runner1 = Runner("Test1", speed=5)
        runner2 = Runner("Test2", speed=5)
        self.assertNotEqual(runner1, runner2)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        from test_runner import Runner
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    @skip_frozen
    def test_race_usain_and_nick(self):
        from test_tournament import Tournament
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    @skip_frozen
    def test_race_andrey_and_nick(self):
        from test_tournament import Tournament
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    @skip_frozen
    def test_race_usain_andrey_and_nick(self):
        from test_tournament import Tournament
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

if __name__ == '__main__':
    unittest.main()