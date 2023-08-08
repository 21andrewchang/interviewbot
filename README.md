# ChatGPT Interview Bot

### Functionality

A bot that can generate interview questions based on a directory of resumes.
Give the bot a name of who you want questions for and it will look through their
resume and generate interview questions specifically for them.

### To Use

Make sure you are in the bot directory and run

```
python3 chatgpt.py "{enter a name}"
```

### Logs

Made a slight change so that it now looks through the files directory to look for
a resume file that is named with the name provided. This way the information doesnt
get mixed together and cause occasional inaccuracies.
