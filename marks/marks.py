import numpy
from scipy import stats
marksstudents = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

#central tendency
my_mean = numpy.mean(marksstudents)
my_median = numpy.median(marksstudents)
print(my_mean)
print(my_median)

my_mode = stats.mode(marksstudents)
print(my_mode)

#Variation
my_range = numpy.ptp(marksstudents)
print(my_range)
interquatile_range = numpy.percentile(marksstudents, 25)
print(interquatile_range)
