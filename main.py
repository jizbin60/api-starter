import requests

URL = "http://www.omdbapi.com/?t=open+season+3&apikey=a7ad1aed"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

print("Who's your favorite actor from Open Season 3?")
print(res["Actors"])
input()
print("What is the plot of the movie Open Season 3?")
input()

import requests


URL = "http://www.omdbapi.com/?t=secret+life+of+pets&apikey=a7ad1aed" 

res = requests.get(URL)
res = res.json()


print("What year was the movie The Secret Life of Pets released?")
input()
print("Was The Secret Life of Pets released during the summer or winter?")
input()