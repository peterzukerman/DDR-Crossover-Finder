import os
import patternFinder as pf


def initialize_notes(file_directory):
    """
    Initializing notes depending on song selected in 'file_directory'
    input: file_directory - the directory of file to be used.
    output: returns array with each containing 4 digits.
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
    return notes


def create_list_songs():
    """
    Creates list of songs refering to 'Songs' directory. 
    output : list of songs available in 'Songs' directory
    """
    avail_songs = next(os.walk("./Songs"))[1]
    print ("\tlist of songs available")
    for idx, songs in enumerate(avail_songs):
        print ('\t\t' + str(idx) + ' : ' + songs)
    return avail_songs


def check_yes_no(res):
    """
    checks if user input is yes('y') or no('n'). Calls function itself if invalid input entered.
    output : boolean. True if 'y' False if 'n'
    """
    if res == 'y':
        return True
    elif res == 'n':
        return False
    else:
        print ("Wrong input")


def choose_songs():
    """
    chooses song from list of songs created from function create_list_songs().
    output : directory of chosen song.
    """
    list_of_songs = create_list_songs()
    user_input = input("\tChoose song to play : ")
    try:
        int(user_input)
    except:
        print ("Wrong Input")
    while int(user_input) > len(list_of_songs) - 1:
        user_input = input("\t Wrong input, choose song to play :")
    response = input("'" + list_of_songs[int(user_input)] + "'" +
                     " was chosen. Wold you like to continue? (y/n) : ")
    if check_yes_no(response):
        directory = "./Songs/"
        directory += list_of_songs[int(user_input)]
        directory += '/'
        files = os.listdir(directory)
        for file in files:
            if str(file).endswith(".sm") or str(file).endswith(".ssc"):
                directory += file
                return str(directory)
    else:
        return choose_songs()

def check_option(notes, title):
    option_num = input("\t\t0: Play(unavailable) \n\t\t1: show crossovers \n\tChoose Options : ")
    if option_num == '0':
        print ("not available yet")
        check_option(notes, title)
    elif option_num == '1':
        pf.detect_crossover(notes, title)
    elif option_num == '9':
        print ("exit")
    else:
        print ("\tno options selected.")
        check_option(notes, title)

def main():
    file_dir = choose_songs()
    title = file_dir.split("/")[2]
    notes = initialize_notes(file_dir)
    check_option(notes, title)


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

#note: Initial Consonant Game
"""
