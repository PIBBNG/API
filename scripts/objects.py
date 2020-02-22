from acamps_questions.models import *
import json

print("[LOG] Inicializando...")
print("[LOG] Abrindo arquivo...")
file = open('./assets/true_questions.json')
with file as f:
    data = json.load(f)

print("[LOG] Criando set de questoes...")
acampsQuestion, created = AcampsQuestions.objects.get_or_create(
    title='noite-especial'
)
print(f"[LOG] Set de questões {acampsQuestion.title} criado com sucesso!")

print("[LOG] Criando questões...")
index = 0
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
    index += 1
print(f"[LOG] {index} foram criadas com sucesso")

print("[LOG] Criando nova sessão...")
session, created = Session.objects.get_or_create(acamps_questions=acampsQuestion)
print(f'[LOG] Sessão criada com sucesso utilizando {session.acamps_questions.title}')

teams = [
    {
        "name": "Gênesis"
    },
    {
        "name": "Apocalipse"
    }
]

print("[LOG] Criando times...")
saved_teams = []
index = 0
for team in teams:
    t, created = Team.objects.get_or_create(name=team['name'])
    t.session = session
    t.save()
    print(f"[LOG] Time {t.name} criado e adicionado a sessao {session.acamps_questions.title}...")
    index += 1
print(f"[LOG] {index} times foram criados com sucesso")
print("[LOG] Inicialização concluída!")