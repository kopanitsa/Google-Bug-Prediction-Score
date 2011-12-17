#!/bin/python

import sys, os
import math
import datetime
import commands
import csv

def str2time(v):
    return datetime.datetime.strptime(v, "%Y-%m-%d")
    
def daydifference(after, before):
    return (str2time(before)-str2time(after)).days

def text2date(line):
    date = line[8:18]
    if date[0] == "2":
        return date
    
def getdates(lines):
    datelist = []
    for line in lines:
        h = line.find("Date:")
        if h != -1:
            date = text2date(line)
            if date != None:
                datelist.append(date)
    return datelist
        
def get_gitlog(path):
    command = "git log --date=short " + path
    text = commands.getoutput(command)
    lines = text.split("\n")
    return lines

def google_score(duration, existing):
    ti = 0
    if (existing != 0):
        ti = duration*1.0 / existing
    return 1.0 / (1.0+math.exp((-12.0*ti)+12.0))

def calc_fix_score(datelist):
    if len(datelist) < 1:
        return 0
    first_commit_date= datelist[len(datelist)-1]
    existing_days = daydifference(first_commit_date, datetime.date.today().isoformat())
    score = 0
    for date in datelist:
        duration = daydifference(first_commit_date, date)
        score += google_score(duration, existing_days)
    return score

def calc_score_from_path(path):
    lines = get_gitlog(path)
    datelist = getdates(lines)
    score = calc_fix_score(datelist)
    return score

def get_file_pathes(root):
    filelist = []
    for dpath, dnames, fnames in os.walk(root):
        for fname in fnames:
            path = dpath+"/"+fname
            filelist.append(path)
    return filelist            

# how to use
# 1. change directory to git root
# 2. input "python bugfix_ratio.py <full path to src directory>"
print "=====start======"
outputfile = "bugfix_score.csv"
writercsv = csv.writer(file(outputfile,"w"))

filelist = get_file_pathes(sys.argv[1])
for f in filelist:
    score = calc_score_from_path(f)
    print f
    print score
    writercsv.writerow([f, score])
    
print "=====end======"

