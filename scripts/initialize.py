from acamps_questions.models import *


file = open('./assets/true_questions.json')
with file as f:
    data = json.load(f)

acampsQuestion, created = AcampsQuestions.objects.get_or_create(
    title='noite-especial'
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

teams = [
    {
        "name": "Gênesis"
    },
    {
        "name": "Apocalipse"
    }
]

saved_teams = []
for team in teams:
    t, created = Team.objects.get_or_create(name=team['name'])
    saved_teams.append(t)

questions = AcampsQuestions.objects.get(title='noite-especial')

session, created = Session.objects.get_or_create(acamps_questions=questions)

for t in saved_teams:
    t.session.add(session)