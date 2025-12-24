songs = [] # 2d list that stores song data in the format of [name, artist, total time played, total number of plays]
def main(filename):
    file = open(filename, "r")
    # store:
        time = # ms_played
        name = # master_metadata_track_name
        artist = # master_metadata_album_artist_name
        skipped = # skipped (for number of plays)
        i = 1
    for line in file:
        # update song name
        if(((i - 6) % 23) == 0): # first time on 6th line, next 23 lines after
            time = int(line[17:].strip(,))
        elif(((i - 10) % 23) == 0): # first name on 10th line, next 23 lines after
            name = line[34:].strip(,)
        elif(((i - 11) % 23) == 0): # first artist on 11th line, next 23 lines after
            artist = line[37:].strip(,)
        elif(((i - 20) % 23) == 0): # first skipped on 20th line, next 23 lines after
            skipped = line[15:].strip(,)
            if(skipped == "true"):
                skipped = True
            else:
                skipped = False
            manage_song(time, name, artist, skipped)
        i += 1
        

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

""" Data template
{
"ts": "YYY-MM-DD 13:30:30",
"username": "_________",
"platform": "_________",
"ms_played": _________,
"conn_country": "_________",
"ip_addr_decrypted": "___.___.___.___",
"user_agent_decrypted": "_________",
"master_metadata_track_name": "_________,
“master_metadata_album_artist_name:_________”,
“master_metadata_album_album_name:_________",
“spotify_track_uri:_________”,
"episode_name": _________,
"episode_show_name": _________,
“spotify_episode_uri:_________”,
"reason_start": "_________",
"reason_end": "_________",
"shuffle": null/true/false,
"skipped": null/true/false,
"offline": null/true/false,
"offline_timestamp": _________,
"incognito_mode": null/true/false,
}
"""