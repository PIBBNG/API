from django.db import models

class Alternative(models.Model):
    text = models.CharField("Texto da alternativa", max_length=150, null=False, default="")
    validate = models.BooleanField("Validador da alternativa", default=False)
    question = models.ForeignKey("Question", null=False, on_delete=models.CASCADE, related_name='alternartives')


class Question(models.Model):
    statement = models.CharField("Enunciado da questão", max_length=255, null=False, default="")
    acamp_questions = models.ForeignKey("AcampsQuestions", null=False, on_delete=models.CASCADE, related_name='questions')
    winner = models.ForeignKey("Team", null=True, on_delete=models.CASCADE, related_name='winner')


class Team(models.Model):
    name = models.CharField("Nome da equipe", max_length=150, null=False, default="", unique=True)
    hits = models.IntegerField("Acertos", null=False, default=0)
    points = models.IntegerField("Pontuação", null=False, default=0)


class AcampsQuestions(models.Model):
    title = models.CharField("Título do Questionario", max_length=100, null=False, unique=True)

