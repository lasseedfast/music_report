### Description

I love the Music Report feature built in into [Hindenburg](https://hindenburg.com/products/hindenburg-journalist-pro) but when using many short clips from each song – as I do when editing documentaries – the output gets a bit messy and one have to sum the duration for every title, including converting minutes/seconds forth and back. This script takes the output from Music Report (it gets copied into clipboard) and outputs a csv-file with title, artist and total duration for each song.


### Instructions

_Make sure you have Pandas installed, else run pip install pandas_


**In terminal:**

cd users/path/to/project/folder

_The project folder can be any folder, like the one you use for your Hindenburg project_
  
  
**In Hindenburg:**

Choose File > Music Report, then Copy


**In terminal:**

Write "python" and then drag the musicreport.py file into the terminal window, should then look like _python users/path/to/musicreport.py_


_You can of course start in Hindenburg, just make sure you're not copying anything – like a path – before you run the script as the script gets the info from clipboard._
