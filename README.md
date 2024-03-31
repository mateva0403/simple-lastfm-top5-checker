# simple-lastfm-top5-checker

This is a Python script that uses the Last.FM API and checks a list of users and their top 5 artists within a 1 month period, and compares them with a list of artists.

The usernames are provided to a .txt file that must be titled "users.txt" and artists to cross reference with are labeled in "index.txt" wherein entries in both files are separated by a line. Then after running the python script, a file titled "output.txt" is generated which lists the user, whether they had a match (true/false), and which artists matched. If there are none, it will simply say "None."

This simple project makes use of the requests library and the Last.FM API. This is a very surface level project just to demonstrate the usage of the API.

## How To Run

For this project, you will need your own API Key from Last.FM. You will then replace the value of the variable API_KEY with a string containing your own API key in main.py. Change the values in the index.txt and users.txt files to your own liking, and compile. This repository provides a sample index file containing some artists on Last.FM's database, along with a template user file. Note that entries on both files are case sensitive.

Also uploaded is a folder containing the files used for a past run of the program. This includes a populated index and users file taken from a comment section of a randomly selected Last.FM shoutbox, along with the output after running it through the program.

## Known Issues

Including non-alphabetic characters in either the index or users file causes issues with the program. There are also errors when you include users that do not exist. This program also does take a while to load which is most likely due to the request handling aspect. 
