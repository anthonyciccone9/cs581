# Author:  Anthony Ciccone

# youtube_data.py searches YouTube for videos matching a search term given by input.
# For sure in Assign03, this file will grab a number given from input.

# Running instructions:
# python3 youtube_date.py and then follow the prompts 

from googleapiclient.discovery import build # use build function to create a service object
import csv #for the csv submission
import unidecode #Used so that the title can be parsed when it has bad ascii values in it. Otherwise it crashed.

API_KEY = "AIzaSyD01Rj6CWBQvJhn2THwt0NFwzCRmXADsS8" #my api key

API_NAME = "youtube"
API_VERSION = "v3" # this should be the latest version

# function youtube_search retrieves the YouTube records after asking for 's_term' and 's_max' from input.

search_term = "" #global variable for the youtube_search method
search_max = 0 #""

def youtube_search(s_term, s_max):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

    search_data = youtube.search().list(q=s_term, part="id,snippet", maxResults=s_max).execute()
    videoInfo = [] #id, publishedAt, title, duration, viewCount, likeCount, and percent is the json format for these indices
    
    # search for videos matching search term;

    for search_instance in search_data.get("items", []): #most of this was given by my professor
        if search_instance["id"]["kind"] == "youtube#video":
        
            videoId = search_instance["id"]["videoId"]  
            publishedAt = search_instance["snippet"]["publishedAt"]
            title = search_instance["snippet"]["title"]
            title = unidecode.unidecode(title) #use of unidecode to make sure the code won't crash from invalid ascii
            duration = "" #necessary duration value
            viewcount = ""#necessary viewcount value
            
            video_data = youtube.videos().list(id=videoId,part="statistics,contentDetails").execute()
            for video_instance in video_data.get("items",[]): #loops through all the videos from the query
                viewCount = video_instance["statistics"]["viewCount"] 
                duration = video_instance["contentDetails"]["duration"]
                if 'likeCount' not in video_instance["statistics"]:
                    likeCount = 0
                else:
                    likeCount = video_instance["statistics"]["likeCount"]
                
                videoInfo.append({ #adds the video after filling all its parameters
                    "id": videoId,
                    "published": publishedAt,
                    "Title": title,
                    "duration": duration, 
                    "views": viewCount,
                    "likes": likeCount,
                    "percent": int(likeCount)/int(viewCount) #makes the percent for the third analysis
                })
        
    print("Search Term: " + search_term)
    print("Search Max: " + search_max)
    print()
    print("List the title, id, date published, and durationfor all videos retrieved, sorted by newest first.")
    printAnalysis(videoInfo)
    print()
    print("List the rank (1 to 5), the title, id, date published, duration, and views for the top 5 videos with the highest views, sorted by highest first.")
    videoInfo.sort(reverse=True,key=lambda x : int(x.get("views")))
    printAnalysisRank(videoInfo[0:5])
    print()
    print("List the rank (1 to 5), the title, id, percentage of likes, views,likes, date published, and durationfor the top 5 videos with the highest like percentage ( like count / view count), sorted by highest percentage first.")
    videoInfo.sort(reverse=True,key=lambda x : float(x.get("percent")))
    printAnalysisRank(videoInfo[0:5])
    csvWriter(videoInfo)

# main routine

def printAnalysis(info): #prints the info to console after the list of all the videos was made.
    for i in range(len(info)):
        print(info[i])
def printAnalysisRank(info): #prints the info to console but ranking them for analysis 2 & 3
    for i in range(len(info)):
        print(str(i + 1) + ": " + str(info[i]))

def csvWriter(info): #Puts the initial row on top, then loops through the video info I saved earlier and creates a row for each.
        csvFile = open('output.csv', 'w')
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(["ID", "Date", "Title", "Duration", "Views", "Likes"])
        for i in range(len(info)):
            csvWriter.writerow(info[i].values())

print('What would you like to search for?')
search_term = input()
print('How many videos would you like to see?')
search_max = input()

youtube_search(search_term, search_max) #running the main code for this to run.

