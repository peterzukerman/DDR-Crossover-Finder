import sys
import glob
import os
from pygame import mixer  # Load the required library

currentLineNumber = 0
notesByMeasures = []
mixer.init()


def initialize_notes(file_directory):
    file_sm = open(str(file_directory), 'r')
    for line in file_sm:
	print line
        measure = -1
        if "measure" in line:
            # print line.split("measure ")[1][:2]
            measure += 1
            # if len(line) == 6:
            # print line[:4]

def create_list_songs():
    avail_songs = os.walk("./Songs").next()[1]
    print "\tlist of songs available"
    for idx, songs in enumerate(avail_songs):
        print '\t\t', idx, ' : ', songs
    return avail_songs


def check_yes_no():
    input = raw_input()
    if input == 'y':
        return True
    elif input == 'n':
        return False
    else:
        print "Wrong input"
        check_yes_no()


def choose_songs():
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
    print "YES"


def main():
    file = choose_songs()
    initialize_notes(file)
    # mixer.music.load('')
    # mixer.music.play()


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
