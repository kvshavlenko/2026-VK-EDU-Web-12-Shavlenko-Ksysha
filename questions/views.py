from django.shortcuts import render
from .utils import paginate
from .data import QUESTIONS, ANSWERS

def index(request):
    page_obj = paginate(QUESTIONS, request, per_page=20)
    return render(request, 'questions/index.html', {'page_obj': page_obj})

def hot(request):
    page_obj = paginate(QUESTIONS, request, per_page=20)
    return render(request, 'questions/hot.html', {'page_obj': page_obj})

def tag(request, tag_name):
    page_obj = paginate(QUESTIONS, request, per_page=20)
    return render(request, 'questions/tag.html', {'page_obj': page_obj, 'tag_name': tag_name})

def question(request, pk):
    page_obj = paginate(ANSWERS, request, per_page=30)
    return render(request, 'questions/question.html', {'page_obj': page_obj, 'question_id': pk})

def ask(request):
    return render(request, 'questions/ask.html')