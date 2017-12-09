

currentLineNumber = 0
notesByMeasures = []



def initialize_notes(file_directory):
	"""
	Initializing notes depending on song selected in 'file_directory'
	input : file_directory - the directory of file to be used.
	output : TODO:: returns 2 dimm array. First dimension for each 'measures' and second dimension for notes.
	"""
	notes = []
	file_sm = open(str(file_directory), 'r')
	for line in file_sm:
		#notesByMeasures = []
		try:
			int(line[0])
			int(line[1])
			int(line[2])
			int(line[3])
			notes.append(line[:4])
		except:
			pass
		# if "measure" in line:
		# 	measure += 1
		# 	notesByMeasures.append("")
		# 	notesByMeasures[measure].append(line)
            # if len(line) == 6
            # print line[:4]
	#print notes
	return notes

def detect_crossover():
	foot = false #false = left foot, true = right foot
	arrow = 0
	firstNote = false
	for x in range(0, len(notesByMeasures)):
		arrow = check_step(notesByMeasures[x])
		if arrow == -1:
			continue
		if firstNote == false:
			if arrow == 0:			#determines which foot hits first note of song
				foot = false
			else:
				foot = true
			firstNote = true
		if foot and check_step(notesByMeasures[x+1]) == 3:
			print("Crossover at line: ", x + 1)
		if not foot and  heck_step(notesByMeasures[x+1]) == 0:
			print("Crossover at line: ", x + 1)

    	


def check_step(line):
	"""
	checks left/up/right/down/leftright/updown
	"""
	if line.count(0) == 4:
		return -1 						#returns -1 if there are no notes on the line
	for x in range(0,len(line)):
		if line[x] == 0:				#if 0, keep going until there's a note
			continue
		elif line[x] == 1 and line.count(1) == 1: #if 1 and only 1 note, return the pos of note
			return x
		elif line.count(1) > 1:			#a jump
			return -1

	return -1

