#! python3
import pyperclip

def get_seconds(t):
    """ Translates duration to seconds """
    return int(t[: t.find(":")]) * 60 + int(t[t.find(":") + 1 :])

# Get data from clipboard
rows = pyperclip.paste().split('\n')

# Dict to fill with info
d = {}

# Get data into dict
for row in rows:
    l = row.split('\t')
    if len(l) < 3: # Filter out empty rows
        continue
    title = l[2]
    duration = l[1]
    if title in d:
        d[title] = {'duration': d[title]['duration'] + get_seconds(duration), 'artist': l[3]}
    else:
        d[title] = {'duration': get_seconds(duration), 'artist': l[3]}

# Write to file
with open("Music Report.csv", "a+") as f:
    f.truncate(0)
    f.write("Title\tArtist\tDuration\n")
    for key, value in d.items():
        minutes = str(int(value['duration'] / 60))
        seconds = str(int(value['duration'] % 60))
        if len(seconds) == 1:
            seconds = seconds + str(0)
        f.write(
            "{title}\t{artist}\t{duration}\n".format(
                title=key,
                artist=value['artist'],
                duration=minutes + ":" + seconds,
            )
        )