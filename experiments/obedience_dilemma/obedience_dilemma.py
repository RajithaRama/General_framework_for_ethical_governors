import blackboard.blackboard as bb

blackboard = bb.Blackboard("obedience_dilemma.yaml", "obedience_dilemma_utilitarian_conf.yaml")
blackboard.run_tests()
blackboard.recommend()