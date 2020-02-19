from acamps_questions.models import Alternative, Question, AcampsQuestions
import json


file = open('./assets/questions_example.json')
with file as f:
    data = json.load(f)

acampsQuestion, created = AcampsQuestions.objects.get_or_create(
    title='Exemplo_3'
)

for q in data['questions']:
    question, created = Question.objects.get_or_create(
        statement=q['statement'],
        acamp_questions=acampsQuestion
    )

    for a in q['alternatives']:
        alternative = Alternative.objects.create(
            text=a['text'],
            validate=a['validate'],
            question=question
        )
