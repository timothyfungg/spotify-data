songs = [] # 2d list that stores song data in the format of [name, artist, total time played, total number of plays]
def main(filename):
    file = open(filename, "r")
    for line in file:
        # store:
        time = # ms_played
        name = # master_metadata_track_name
        artist = # master_metadata_album_artist_name
        skipped = # skipped (for number of plays)
        
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

def check_song(index, time, skipped):
    songs[index][2] += time
    if(skipped == True):
        songs[index][3] += 1

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