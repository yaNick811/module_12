import unittest
from unittest.runner import TextTestRunner


suite = unittest.TestSuite()


from tests_12_3 import RunnerTest, TournamentTest
suite.addTests(unittest.makeSuite(RunnerTest))
suite.addTests(unittest.makeSuite(TournamentTest))


runner = TextTestRunner(verbosity=2)


runner.run(suite)