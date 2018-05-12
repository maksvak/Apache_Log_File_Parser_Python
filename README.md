# Apache_Log_File_Parser_Python
Python Apache Log File Parser I created for a job interview


Place weblog csv into same folder as alp.py on desktop - or alter code as it is hard pathed. Then simply navigate to python.exe and run

python.exe C:\Users\...\Desktop\ALP\alp.py

You will generate two print outs. The first is a list of unique IP's that appear. The script is commented heavily, but as a general explanation:

the function unique basically compares each new string to the stored list. Any new strings get appeneded, any duplicates rejected.

The dictionary is a key/value store. We have a key that is the host name file, and the value is actually a list, using a similar sort we add the IPs for each key to the list thats stored as it value. Duplicates are ignored.
