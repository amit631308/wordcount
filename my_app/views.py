from django.shortcuts import render
from django.http import HttpResponse
import operator
def index(request):
    return render(request,'1home.html')

def count(request):
    data = request.GET['text']
    data_1 = data.split()
    number = len(data_1)
    word_dict = {}
    for word in data_1:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sortedlist = sorted(word_dict.items(), key = operator.itemgetter(1))
    return render(request, 'counted.html', {'text': data,'text2':number, 'word_dict':sortedlist})
def about(request):
    return render(request, 'about.html')
