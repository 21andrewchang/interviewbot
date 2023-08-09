# ChatGPT Interview Bot

### Functionality

A bot that can generate interview questions based on a directory of resumes.
Give the bot a name of who you want questions for and it will look through their
resume and generate interview questions specifically for them. You can also ask
the bot to include the persons contact information such as email or phone number.
An error will be returned if you ask for someone and the bot could not find a resume
with their name.

### To Use

Create a constants.py file in the bot directory and put in ur api key

```
APIKEY="replace with apikey"
```

Make sure you are in the bot directory and run

```
python3 chatgpt.py "{enter a name}"
```
