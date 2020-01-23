from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from acamps_questions.models import Alternative, Question, Team, AcampsQuestions

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
        
        return Response(response={"acamps_questions_id":acamps.id},status=status.HTTP_200_OK)


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
