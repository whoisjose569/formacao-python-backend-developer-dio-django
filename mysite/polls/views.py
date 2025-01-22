from django.http import Http404, HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

from django import template

register = template.Library()

@register.filter
def add_emoji(texto):
    return f"{texto} 😊"

faculdade = {"Unimar", "Univem"}
endereco = {"cidade": "Ubirajara",
            "estado": "SP"
        }

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
        "emoji": add_emoji("BEM VINDO"),
        "faculdades": faculdade,
        "endereco": endereco
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)