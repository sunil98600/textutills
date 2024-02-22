from django.http import  HttpResponse
from django.shortcuts import render

def index (request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    removepunc=request.POST.get('removepunc','off')
    extraspaceremover=request.POST.get('removewhitwspace','off')
    lengthcounter=request.POST.get('countlength','off')
    caps=request.POST.get('caps','off')
    if (removepunc == "on"): 
        punctuations = '''{!()-[]};:'"\,<>./?@#$%^&*_~'''
        analyze=''
        for char in djtext:
            if char not in punctuations :
                analyze = analyze + char

        params = {'purpose': 'Removed Punctuations','analyzed_text':analyze}
        djtext = analyze 
    if (caps == "on"):
        analyze=''
        for char in djtext:
                analyze = analyze + char.upper()

        params = {'purpose': 'Capitalized','analyzed_text':analyze}
        djtext =analyze
    if(extraspaceremover=="on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyze = analyze + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyze}

        # Analyze the text
        djtext = analyze  
    


    if removepunc != "on" and caps != "on" and extraspaceremover!="on" :
        return HttpResponse("Error")
    

    return render(request, 'analyze.html', params)    
       


    

