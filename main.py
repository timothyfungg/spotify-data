class Main:
    def main(filename):
        songs = [] # 2d list that stores song data in the format of [name, artist, total time played, total number of plays]
        file = open(filename, "r")
        for line in file:
            # store:
            time = # ms_played
            name = # master_metadata_track_name
            artist = # master_metadata_album_artist_name
            skipped = # skipped (for number of plays)
            
            # add song to list of not already there
            # update data of corresponding song in list

    def check_song(songs, index, time, skipped):
        songs[index][2] += time
        if(skipped == True):
            songs[index][3] += 1
        return songs

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