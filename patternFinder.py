
def detect_crossover(notesByMeasures):
	foot = False  # false = left foot, true = right foot
	arrow = 0
	firstNote = False
	count = 0;
	f = open('output.txt', 'w')
	for x in range(0, len(notesByMeasures)):
		arrow = check_step(notesByMeasures[x])
		if arrow == -1:
			#print notesByMeasures[x], '\t', arrow
			continue
		if firstNote == False:
			if arrow == 0:  # determines which foot hits first note of song
				foot = False
			else:
				foot = False
			firstNote = False
		if foot and check_step(notesByMeasures[x + 1]) == 3:
			count += 1
			print "Crossover at line: ", x + 1
			f.write("Crossover at line: " + str(x + 1) + '\n')
		if not foot and check_step(notesByMeasures[x + 1]) == 0:
			count += 1
			print "Crossover at line: ", x + 1
			f.write("Crossover at line: " + str(x + 1) + '\n')
	print "check crossover done"
	print "number of crossovers", count
	f.write("number of crossovers: " + str(count))
	f.close


def check_step(line):
	"""
	checks left/up/right/down/leftright/updown
	"""
	if line.count("0") == 4:
		return -1  # returns -1 if there are no notes on the line
	for x in range(0, len(line)):
		if line[x] == '0':  # if 0, keep going until there's a note
			continue
		# if 1 and only 1 note, return the pos of note
		elif line[x] == '1' and line.count('1') == 1:
			return x
		elif line.count('1') > 1:  # a jump
			return -1

	return -1
