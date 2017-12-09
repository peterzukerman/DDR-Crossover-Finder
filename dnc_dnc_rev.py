import glob
import os
import sys


from pygame import mixer  # pip install pygame

currentLineNumber = 0
mixer.init()

def check_step():
	"""
	checks left/up/right/down/leftright/updown
	"""


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

def create_list_songs():
	"""
	Creates list of songs refering to 'Songs' directory. 
	output : list of songs available in 'Songs' directory
	"""
	avail_songs = os.walk("./Songs").next()[1]
	print "\tlist of songs available"
	for idx, songs in enumerate(avail_songs):
		print '\t\t', idx, ' : ', songs
	return avail_songs

def check_yes_no():
    """
    checks if user input is yes('y') or no('n'). Calls function itself if invalid input entered.
    output : boolean. True if 'y' False if 'n'
    """
    input = raw_input()
    if input == 'y':
        return True
    elif input == 'n':
        return False
    else:
        print "Wrong input"
        check_yes_no()


def choose_songs():
    """
    chooses song from list of songs created from function create_list_songs().
    output : directory of chosen song.
    """
    list_of_songs = create_list_songs()
    input = raw_input("\t Choose song to play :")
    while int(input) > len(list_of_songs) - 1:
        input = raw_input("\t Wrong input, choose song to play :")
    print "'" + list_of_songs[int(input)] + "'" + " was chosen. Wold you like to continue? (y/n)"

    if check_yes_no():
		directory = "./Songs/"
		directory += list_of_songs[int(input)]
		directory += '/'
		files = os.listdir(directory)
		for file in files:
			if str(file).endswith(".sm") or str(file).endswith(".ssc"):
				directory += file
				return str(directory)
    else:
        return choose_songs()


def detect_crossover():
    """
	TODO: detects crossover pattern throughout the file(.sm or .ssc). 
    """
    print "YES"


def main():
    file = choose_songs()
    initialize_notes(file)

main()


"""
Properties of sm files.
#TITLE:Satisfy;
#SUBTITLE:;
#ARTIST:YUNG BAE;
#TITLETRANSLIT:;
#SUBTITLETRANSLIT:;
#ARTISTTRANSLIT:;
#GENRE:Future Funk;
#CREDIT:;
#BANNER:Satisfy-bn.png;
#BACKGROUND:Satisfy-bg.png;
#LYRICSPATH:;
#CDTITLE:cd-title-Benpai.png;
#MUSIC:Satisfy.ogg;
#OFFSET:0.000000;
#SAMPLESTART:50.000000;
#SAMPLELENGTH:16.000000;
#SELECTABLE:YES;
#DISPLAYBPM:120.000000;
#BPMS:0.000000=120.000000
;
#STOPS:
;
#BGCHANGES:;
#KEYSOUNDS:;
#ATTACKS:;

example crossovers
	basically, if we just have the boolean variable deciding which foot it is, then for example if the left foot is already down and the next arrow is a left arrow, we know it's a crossover
there are still a couple of ambiguous cases, but that makes it a ton easier

1000
0100
0001
0100

1000
0010
0001
0010

0001
0100
1000
0100

0001
0010
1000
0010

"""
