#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def main():
	start = 60000.0
	avk = 1.05
	#avg = 0.005 # 0.5%
	avg = 0.0170 # 1.85%
	year = 12

	perfect = []
	perfect.append(start)

	print "Avkastning: %s\nAvgift: %s\nAr: %s\n" % (avk, avg, year)

	for x in range(1, year + 1):
		tmp = (start*avk**(x))
		perfect.append(tmp)
		print "Ar %d: %d" % (x, tmp)
	print perfect

	nonperfect = []
	nonperfect.append(start)
	diff = [perfect[0] - nonperfect[0]]
	for x in range(1, year + 1):
		before_avg = nonperfect[x - 1] * avk
		after_avg = before_avg - (before_avg * avg)
		nonperfect.append(after_avg)
		diff.append(perfect[x - 1] - nonperfect[x - 1])
		print "Ar: %d, before: %d, after: %d" % (x, before_avg, after_avg)

	plt.plot([x for x in range(0, year + 1)], perfect, 'g-', nonperfect, 'r-', diff, 'b-')
	#plt.axis([0, 6, 0, 20])
	plt.xlabel('Year')
	plt.ylabel('Money in kronor')
	plt.title('Money after %s years' % year)
	plt.grid(True)
	plt.text(year - 1, int(perfect[-1]), str(int(perfect[-1])) + "kr")
	plt.text(year - 1, int(nonperfect[-1]), str(int(nonperfect[-1])) + "kr")
	plt.text(year - 1, int(diff[-1]), str(int(diff[-1])) + "kr")
        offset = year / 3
	plt.text(1, int(perfect[-1]), "Start: " + str(start))
	plt.text(offset, int(perfect[-1]), "Avkastning: " + str(avk) + "%")
	plt.text(offset * 2, int(perfect[-1]), "Avgift: " + str(avg*100) + "%")
	plt.text(1, start / 2, "Total avgift i procent efter " + str(year) + " ar: " + str(round(((perfect[-1] / nonperfect[-1])*100)-100, 2)) + "%", color='red')
	plt.show()

if __name__ == '__main__':
	main()
