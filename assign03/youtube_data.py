# Author:  Anthony Ciccone

#  youtube_data.py searches YouTube for videos matching a search term
# For sure in Assign03, this file will grab 5

# To run from terminal window:   python3 youtube_data.py 

from googleapiclient.discovery import build      # use build function to create a service object

# put your API key into the API_KEY field below, in quotes
API_KEY = "AIzaSyD01Rj6CWBQvJhn2THwt0NFwzCRmXADsS8"

API_NAME = "youtube"
API_VERSION = "v3"       # this should be the latest version

#  function youtube_search retrieves the YouTube records

search_term = ""
search_max = 0

def youtube_search(s_term, s_max):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

    search_data = youtube.search().list(q=s_term, part="id,snippet", maxResults=s_max).execute()
    videoInfo = [] #id, publishedAt, title, duration, viewCount, likeCount
    
    # search for videos matching search term;
    
    for search_instance in search_data.get("items", []):
        if search_instance["id"]["kind"] == "youtube#video":
        
            videoId = search_instance["id"]["videoId"]  
            publishedAt = search_instance["snippet"]["publishedAt"]
            title = search_instance["snippet"]["title"]
            duration = ""
            viewcount = ""
            likecount = ""
              
            video_data = youtube.videos().list(id=videoId,part="statistics,contentDetails").execute()
            for video_instance in video_data.get("items",[]):
                viewCount = video_instance["statistics"]["viewCount"]
                duration = video_instance["contentDetails"]["duration"]
                if 'likeCount' not in video_instance["statistics"]:
                    likeCount = 0
                else:
                    likeCount = video_instance["statistics"]["likeCount"]
                
            videoInfo.append("ID: " + videoId + ", Published: " + publishedAt + ", Title: " +  title + ", Duration: " + duration + ", Views: " + viewCount + ", Likes: " + likeCount)
            
# Analysis–be sure each analysis section has descriptive information as a header before printing theresults:  
# 1.List the title, id, date published, and duration for all videos retrieved, sorted by newest first.
# 2.List the rank (1 to 5), the title, id, date published, duration, and views for the top 5 videos with the highest views, sorted by highest first.
# 3.List the rank (1 to 5), the title, id, percentage of likes, views, likes, date published, and duration for the top 5 videos with the highest like percentage ( like count / view count), sorted by highest percentage first.
    print("first analysis")
    printAnalysis(videoInfo)
    print("second analysis")
    print("third analysis")

# main routine

def printAnalysis(info):
    for i in range(len(info)):
        print(info[i])
def printAnalysisRank(info):
    for i in range(len(info)):
        print(i: info[i])

print('What would you like to search for?')
search_term = input()
print('How many videos would you like to see?')
search_max = input()

youtube_search(search_term, str(int(search_max) + 1))

