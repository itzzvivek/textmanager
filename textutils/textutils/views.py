#created by me
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("<h1>Hello CliX</h1>")
#
# def about(request):
#     return HttpResponse("Hi this side CliX")
#
# def yt(request):
#     return HttpResponse('''<a href="https://www.youtube.com/channel/UCjDU4KTL379anIbUbGsvsvw">itzzCliX</a>''')
#



def index(request):
    return render(request,'index.html')

def ex1(request):
    sites = ['''<h1>For Entertainment</h1><a href = "https://www.youtube.com">youtube video</a>''',
             '''<h1>For Interaction</h1><a href = "https://www.facebook.com">Facebook</a>''',
             '''<h1>For Insight </h1><a href = "https://www.ted.com/talks">Ted Talk</a>''',
             '''<h1>For Intership </h1><a href = "https://internshala.com">Inrtenship</a>''',
           ]
    return HttpResponse((sites))

def analyze(request):
    #get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    print(removepunc)
    print(djtext)
    # analyzed = djtext
    if removepunc == "on":
     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
    params = {'purpose' : 'Removed Punctutions','analyzed_text': analyzed}
    #analyze the text
    return render(request, 'analyze.html', params)

    # elif fullcaps == "on":
    # analyzed = ""
    # for char in djtext:
    #     analyzed = analyzed+char.upper()
    # params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
    # return render(request, 'analyze.html', params)
    #
    # else:
    #     return HttpResponse('Error')

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def comments(request):
#     return HttpResponse("comment<a href='/''>Back</a>")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount")

