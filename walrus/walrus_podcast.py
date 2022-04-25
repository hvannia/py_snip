# pip install realpython-reader parse statistics
import parse
from reader import feed  # real python feed
import statistics


#titles= feed.get_titles()[:3]
pattern = parse.compile("The Real Python Podcast – Episode #{num:d}: {name}")
#pattern.parse(titles[2])

podcasts = [
    pattern.parse(title)["name"] 
    for title in feed.get_titles() 
    if pattern.parse(title)
]
 

 # avoid title twice

 podcasts = [
     podcast["name"]
     for title in feed.get_titles()
     if (podcast := pattern.parse(title))
 ]

 # generator experssion fro titles over 50- chars lomg

long_average =  statistics.mean(
    title_length
    for title in podcasts
    if (title_length := len(title)) > 50 
)
print(long_average)