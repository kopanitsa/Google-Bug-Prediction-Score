implemented google's bug prediction score.
To know algorithm, please see
http://www.publickey1.jp/blog/11/post_193.html
or
http://google-engtools.blogspot.com/2011/12/bug-prediction-at-google.html

This script calculate the score of each class recursively.
Result is outputted as csv file.

How To Use:
$ cp <this script> <root of your project>
$ cd <root of your project>
$ python bugfix_score.py <full path to target directory>

Note:
Project must be managed with git.

Contact:
Takahiro Okada (@kopanitsa)
