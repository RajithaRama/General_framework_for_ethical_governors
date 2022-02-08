from abc import ABC

from evaluator import Evaluator

class DeontologyEvaluator(Evaluator):

    def evaluate(self, data):
        print("evaluated")
