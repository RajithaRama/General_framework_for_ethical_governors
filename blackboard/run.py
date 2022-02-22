import blackboard

if __name__ == "__main__":
    # blackboard = Blackboard("../Lying_dilemma.yaml", "lying_dilemma_deontology_conf.yaml")
    # blackboard = Blackboard("../obedience_dilemma.yaml", "obedience_dilemma_utilitarian_conf.yaml")
    blackboard_1 = blackboard.Blackboard("../speeding_dilemma.yaml", "speeding_dilemma_conf.yaml")
    blackboard_1.run_tests()
    print(blackboard_1.recommend())