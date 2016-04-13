from master import RunTests
RunTests.political_attr= RunTests.soc_array

runtests = RunTests()

# compare = RunTests.compare()


# sum_dist = RunTests.sum_dist()
# pandafy = RunTests.pandafy()

runtests.compare()
runtests.sum_dist()
runtests.pandafy()