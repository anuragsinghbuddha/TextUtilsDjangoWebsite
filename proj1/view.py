#we created this file
from re import S
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")


    
def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')#use POST insted of GET so that our enter text cannot go in url
    #checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcap=request.POST.get('fullcap','off')
    newlineremover=request.POST.get('newlineremover','off')
    ExtraSpaceRemover=request.POST.get('ExtraSpaceRemover','off')
    CharCount=request.POST.get('CharCount','off')
    
  
    #checking if checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removed Punctuations", 'analyzed_text': analyzed}
     #Analyse the text
        djtext=analyzed
     
    if(fullcap=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': "Changed to Upper case", 'analyzed_text': analyzed}
     #Analyse the text
        djtext=analyzed
       
    if(newlineremover=='on'):
        analyzed=''
        for char in djtext:
            if(char!="\n" and char!="\r"):
               analyzed=analyzed+char
            
        params = {'purpose': "Removed New Lines", 'analyzed_text': analyzed}
     #Analyse the text
        djtext=analyzed
      
    if(ExtraSpaceRemover=='on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if(djtext[index]==" " and djtext[index+1]==" "):
                pass 
            else:
                analyzed=analyzed+char
        params = {'purpose': "Extra Space Remover", 'analyzed_text': analyzed}
     #Analyse the text
        djtext=analyzed
       
    if(charcount=='on'):
        analyzed=''
        count=0
        for char in djtext:
            count+=1

        params = {'purpose': "CharCount", 'analyzed_text': count}
     #Analyse the text
        djtext=analyzed
        
    if(removepunc != "on" and newlineremover!="on" and ExtraSpaceRemover!="on" and fullcap!="on"):
        return HttpResponse("please select any operation and try again")

    params = {'purpose': "Removed Punctuations", 'analyzed_text': analyzed}
     #Analyse the text
    return render(request,'analyze.html',params)
    #Analyse the text
def capfirst(request):
    return HttpResponse("Captilize first")
def newlineremove(request):
    return HttpResponse("Removing new line")
def spaceremove(request):
    return HttpResponse("Removing spaces")
def charcount(request):
    return HttpResponse("Counting charecter")

