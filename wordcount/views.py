 # -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def dev(request):
    return HttpResponse('Jai Shree Ram !')

def count(request):
    fulltext = request.GET['fulltexts'] 
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
           worddict[word] += 1
        else:
            worddict[word] = 1
    sortedDict = sorted(worddict.items(), key = operator.itemgetter(1), reverse = True)        
    #print(fulltext)
    return render(request, 'count.html',{'fulltext':fulltext,'len':len(wordlist),'wordlist':sortedDict})