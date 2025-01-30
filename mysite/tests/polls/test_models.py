import pytest
from django.utils import timezone
from polls.models import Question

@pytest.mark.django_db
def test_question_create():
    question_text = "Qual a sua linguagem de programação favorita?"
    pub_date = timezone.now()
    active = True
    
    question = Question.objects.create(question_text= question_text, pub_date=pub_date, active=active)
    
    assert question.question_text == question_text
    assert question.pub_date == pub_date
    assert question.active == active