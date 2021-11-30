from django.shortcuts import render
import pytube
from .models import Categories, Playlists
import pytube

##################
# 1. Categories
##################
def home(request):
    '''
    Displays all the categories in the home page
    '''
    cat_obj = Categories.objects.all()
    context = {
        'cat_obj': cat_obj,
    }
    return render(request, "back/index.html", context)


# Get the title of the playlist
def get_title(url):
    playlist_obj = pytube.Playlist(url=url)
    title = playlist_obj.title
    # channelName = playlist_obj.owner
    return title


###############################
# 2. Category wise playlists
###############################
def categories(request, id):
    '''
    This function returns all the playlists with a specific category
    data is from the model
    '''
    playlists = Playlists.objects.filter(category=id)
    code_list = []
    for index in range(len(playlists)):
        code_list.append(str(playlists[index].url).split("=")[1])
    context = {
        'code_list': code_list,
    }
    return render(request, "back/categories.html", context)


################################################
# 3. Playlists wise (All videos in playlist)
################################################
def list_url(request, code):
    '''
    This function returns all the video urls in a playlist
    '''
    url = "https://www.youtube.com/playlist?list=" + code
    playlist_obj = pytube.Playlist(url=url)
    vid_url = playlist_obj.videos
    vid_urls = []
    for index in vid_url:
        urls = index.streams.filter(progressive="True").filter(res="720p")[0]
        vid_urls.append(urls)
    return render(request, "back/list.html", context={'vid_urls': vid_urls})


# 4. Detail (Video click urls)