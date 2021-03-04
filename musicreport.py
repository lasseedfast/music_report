#! python3
import pandas as pd

# Import clipboard to dataframe
## There's something off with the format when copied frmo Hindenburg,
## therefore the extra column
df = pd.read_clipboard(
    sep="\t", names=["offset", "duration", "title", "artist", "album", ""]
)
df.drop(["album", "", "offset"], axis=1, inplace=True)

# Translate duration for each clip to seconds
df["seconds"] = df.duration.apply(
    lambda x: int(x[: x.find(":")]) * 60 + int(x[x.find(":") + 1 :])
)

# Open and prepare file
with open("Music Report.csv", "a+") as f:
    f.truncate(0)
    f.write("Title\tArtist\tDuration\n")

    # Sum the duration for all clips with the same title
    for title in df.groupby("title"):
        minutes = str(int(title[1].seconds.sum() / 60))
        seconds = str(int(title[1].seconds.sum() % 60))
        if len(seconds) == 1:
            seconds = seconds + str(0)

        # Write to file
        f.write(
            "{title}\t{artist}\t{duration}\n".format(
                title=title[0],
                artist=title[1].artist.tolist()[0],
                duration=minutes + ":" + seconds,
            )
        )
