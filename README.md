# Script for adding times

This python script adds times given in the format **`hour:minutes:seconds`** as command line arguments, and outputs the total time in the same format.

## Usage 

Best way to use it is to give the program a file with times in each line:
```bash
$ more file.txt
01:54:53
02:16:55
$ ./add_times.py < file.txt
4:11:48
```
**Note**: use one line per time and in the format expressed in the description.


## LICENSE
GPLv3
Copyright © 2015 Antonio Gutierrez 
