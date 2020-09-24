# Author:  Cheryl Dugas

#  youtube_data.py searches YouTube for videos matching a search term

# To run from terminal window:   python3 youtube_data.py 

from googleapiclient.discovery import build      # use build function to create a service object

# put your API key into the API_KEY field below, in quotes
API_KEY = "AIzaSyD01Rj6CWBQvJhn2THwt0NFwzCRmXADsS8"

API_NAME = "youtube"
API_VERSION = "v3"       # this should be the latest version

#  function youtube_search retrieves the YouTube records

def youtube_search(s_term, s_max):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

    search_data = youtube.search().list(q=s_term, part="id,snippet", maxResults=s_max).execute()
    
    # search for videos matching search term;
    
    for search_instance in search_data.get("items", []):
        if search_instance["id"]["kind"] == "youtube#video":
        
            videoId = search_instance["id"]["videoId"]  
            title = search_instance["snippet"]["title"]
                      
                  
            video_data = youtube.videos().list(id=videoId,part="statistics").execute()
            for video_instance in video_data.get("items",[]):
                viewCount = video_instance["statistics"]["viewCount"]
                if 'likeCount' not in video_instance["statistics"]:
                    likeCount = 0
                else:
                    likeCount = video_instance["statistics"]["likeCount"]
                    
            
            print("")    
            print(videoId, title, viewCount, likeCount)

# main routine

search_term = "computer"
search_max = 5
    
youtube_search(search_term, search_max)
