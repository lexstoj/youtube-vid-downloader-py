
from pytube import YouTube


link = input ("enter the link: ")
yt = YouTube(link)


print("Title: ",yt.title)

print("Number of views: ",yt.views)

print("Length of video: ",yt.length,"seconds")

print("Description: ",yt.description)

print(yt.streams)
print (yt.streams.filter(only_audio=True))
print(yt.streams.filter(only_video=True))
print(yt.streams.filter(progressive=True))
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download("C:/enterspecifiedpath")
print("download done enjoy the vid nerd")
