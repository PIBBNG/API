from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from acamps_questions.models import Alternative, Question, Team, AcampsQuestions, Session
import json

class AcampsQuestionsViews(APIView):

    def post(self, request):
        '''
            Conexão de dados
        '''
        try:
            teams = request.data['teams']
            questions = request.data['questions']
            acamps_questions = request.data['acamps_questions']
            print("[LOG] DADOS RECEBIDOS - NOVO QUESTIONARIO")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        '''
            Salvando questionario
        '''
        try:
            acamps = AcampsQuestions.objects.create(
                title=acamps_questions["title"]
            )
            print("[LOG] NOVO QUESTIONÁRIO SALVO!")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        '''
            Salvando os Times
        '''
        try:
            for team in teams:
                t, created = Team.objects.get_or_create(
                    name=team["name"],
                )
            print("[LOG] TIMES SALVOS!")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        '''
            Salvando Questions
        '''
        try:
            for question in questions:
                q, created = Team.objects.get_or_create(
                    statement=question["statement"]
                )
                for alternative in question["alternatives"]:
                    a = Alternative.objects.create(
                        text=alternative["text"],
                        validate=validate["validate"]
                    )
                    q.alternatives.add(a)
                q.save()
                acamps.questions.add(q)
                acamps.save()
            print("[LOG] TODAS QUESTÕES SALVAS!")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"acamps_questions_id":acamps.id},status=status.HTTP_200_OK)

    def get(self, request):
        acampsQuestions = AcampsQuestions.objects.all()
        response = []
        for questions in acampsQuestions:
            q = {}
            q['id'] = questions.id
            q['title'] = questions.title
            response.append(q)
        return Response(response,status=status.HTTP_200_OK)

class QuestionsView(APIView):

    def get(self, request):
        try:
            acamps_id = request.data["acamps_id"]
            question_id = request.data["question_id"]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            acamps = AcampsQuestions.objects.get(id=acamps_id)
            question = acamps.questions.get(id=question_id)
            print("[LOG] QUESTÃO ENCONTRADA!")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        q = {}
        q["statement"] = question.statement
        a = []
        for alternative in question.alternatives.all():
            a_body = {}
            a_body["text"] = alternative.text
            a_body["validate"] = alternative.validate
            a.append(a_body)
        q["alternatives"] = a

        return Response(response=q,status=status.HTTP_200_OK)

class SessionView(APIView):

    def post(self, request):
        try:
            teams = request.data['teams']
            acampsQuestions_title = request.data['acampsQuestions']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

        print(f"[LOG] Criando uma nova sessão com: {acampsQuestions_title}")
        try:
            acampsQuestions = AcampsQuestions.objects.get(title=acampsQuestions_title)
            session = Session.objects.create(
                acamps_questions=acampsQuestions
            )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        teams_ids = []
        for team in teams:
            t = Team.objects.get_or_create(
                name=team,
            )
            t = t[0]
            t.hits = 0
            t.points = 0
            t.session = session
            t.save()
            teams_ids.append({"id":t.id,"name":t.name, "hits":t.hits, "points":t.points})

        response = {}
        response['session'] = {"session_id": session.id}
        response['teams'] = teams_ids
        print(f"[LOG] Sessão criada com sucesso!")
        return Response(response, status=status.HTTP_200_OK)

class QuestionsIds(APIView):

    def get(self, request):
        session_id = request.data['session_id']
        session = Session.objects.get(id=session_id)
        questions = session.acamps_questions.questions.all()
        questions_ids = []
        
        index = 1
        for q in questions:
            id = {}
            id['number'] = index
            id['question_id'] = q.id
            questions_ids.append(id)
            index += 1
        
        return Response(questions_ids, status=status.HTTP_200_OK)

class QuestionView(APIView):

    def get(self, request):
        question_id = request.data['question_id']
        question = Question.objects.get(id=question_id)
        
        question_response = {}
        question_response['statement'] = question.statement
        question_response['winner'] = question.winner.name
        question_response['alternatives'] = []

        for alt in question.alternartives.all():
            alternative = {}
            alternative["text"] = alt.text
            alternative["validate"] = alt.validate
            question_response['alternatives'].append(alternative)

        return Response(question_response, status=status.HTTP_200_OK)

class TeamView(APIView):

    def get(self, request):
        # session = Session.objects.get(id=request.data['session_id'])
        teams = Team.objects.filter(session_id=request.data['session_id'])

        t = []
        for team in teams:
            aux = {}
            aux['name'] = team.name
            aux['points'] = team.points
            aux['hits'] = team.hits
            t.append(aux)
        
        return Response(t, status=status.HTTP_200_OK)
        
    def post(self, request):

        team = Team.objects.get(name=request.data['team_name'])
        question = Question.objects.get(id=request.data['question_id'])
        team.points += 100
        team.hits += 1
        team.save()
        question.winner = team
        question.save()

        return Response(status.HTTP_200_OK)
    