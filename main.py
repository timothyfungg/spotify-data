songs = [] # 2d list that stores song data in the format of [name, artist, total time played, total number of plays]
def main(filename):
    file = open(filename, "r")
    # store:
        time = 0 # ms_played
        name = "" # master_metadata_track_name
        artist = "" # master_metadata_album_artist_name
        skipped = False # skipped (for number of plays)
        line_num = 1
    for line in file:
        # update song name
        if(((line_num - 6) % 23) == 0): # first time on 6th line, next 23 lines after
            time = int(line[17:].strip(,))
        elif(((line_num - 10) % 23) == 0): # first name on 10th line, next 23 lines after
            name = line[34:].strip(,)
        elif(((line_num - 11) % 23) == 0): # first artist on 11th line, next 23 lines after
            artist = line[37:].strip(,)
        elif(((line_num - 20) % 23) == 0): # first skipped on 20th line, next 23 lines after
            skipped = line[15:].strip(,)
            if(skipped == "true"):
                skipped = True
            else:
                skipped = False
            manage_song(time, name, artist, skipped)
        line_num += 1
    print(print_songs())
        

def check_song(index, time, skipped):
    songs[index][2] += time
    if(skipped == True):
        songs[index][3] += 1

def manage_song(time, name, artist, skipped):
    # Boolean to keep track of whether the song is in the list or not
    present = False
    
    # Checks entire list to check if song is present, updates data if so
    for i in range(0, len(songs)):
        if(songs[i][0] == name):
            check_song(i, time, skipped)
            present = True
    
    # Adds song to list if not present and updates its data
    if(present == False)
        songs.append([name, artist, 0, 0])
        check_song(len(songs - 1), time, skipped)

def print_songs():
    output = ""
    for i in range(0, len(songs)):
        for j in range(0, len(songs[i])):
            output += f"Name: {songs[i][0]}\nArtist: {songs[i][1]}\nTime Played: {(songs[i][2] / 3600000):.1f} seconds\nTotal Plays: {songs[i][3]}\n\n"
    return output