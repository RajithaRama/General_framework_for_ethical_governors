import blackboard.blackboard as bb

blackboard = bb.Blackboard("speeding_dilemma.yaml", "speeding_dilemma_conf.yaml")
blackboard.run_tests()
blackboard.recommend()