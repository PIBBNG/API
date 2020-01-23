from django.db import models

class Alternative(models.Model):
    text = models.CharField("Texto da alternativa", max_length=150, null=False, default="")
    validate = models.BooleanField("Validador da alternativa", default=False)
    question = models.ForeignKey("Question", null=False, on_delete=models.CASCADE, related_name='alternartives')


class Question(models.Model):
    statement = models.CharField("Enunciado da questão", max_length=255, null=False, default="")
    difficulty = models.CharField("Dificuldade", max_length=1, null=False, default="M")
    acamp_questions = models.ForeignKey("AcampsQuestions", null=False, on_delete=models.CASCADE, related_name='questions')
    winner = models.ForeignKey("Team", null=False, on_delete=models.CASCADE, related_name='winner')


class Team(models.Model):
    name = models.CharField("Nome da equipe", max_length=150, null=False, default="", unique=True)
    hits = models.IntegerField("Acertos", null=False, default=0)
    points = models.IntegerField("Pontuação", null=False, default=0)


class DifficultySet(models.Model):
    easy = models.IntegerField("F - Fácil", null=False, default=50)
    medium = models.IntegerField("M - Médio", null=False, default=100)
    hard = models.IntegerField("H - Difícil", null=False, default=150)
    expert = models.IntegerField("E - Expert", null=False, default=200)


class AcampsQuestions(models.Model):
    title = models.CharField("Título do Questionario", max_length=100, null=False, unique=True)
    difficulty_set = models.ForeignKey("DifficultySet", null=False, on_delete=models.CASCADE, related_name='difficulty_set')

