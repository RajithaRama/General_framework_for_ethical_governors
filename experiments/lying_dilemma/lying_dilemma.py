import blackboard.blackboard as bb

blackboard = bb.Blackboard("Lying_dilemma.yaml", "lying_dilemma_deontology_conf.yaml")
blackboard.run_tests()
blackboard.recommend()