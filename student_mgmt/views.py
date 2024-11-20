from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
def show_panel(request):
    html_content = """
        <html>
            <head>
                <style>
                    body {
                        display: flex;
                        flex-direction: column; /* Stack elements vertically */
                        justify-content: center;
                        align-items: center;
                        height: 100vh; /* Full height of the viewport */
                        margin: 0; /* Remove default margin */
                        text-align: center; /* Center text */
                    }
                    h1 {
                        font-size: 48px; /* Bigger text size */
                        font-weight: bold; /* Bold text */
                    }
                    h2 {
                        font-size: 24px; /* Slightly smaller size for the subheading */
                        font-weight: normal; /* Normal weight for subheading */
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to the Knowledge Sharing Session</h1>
                <h2>By, Ganesh Prasad</h2>
            </body>
        </html>
        """
    return HttpResponse(html_content)

class StudentData(APIView):
    def get(self, request):
        try:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response({"error":False, "details": serializer.data})
        except Exception as e:
            print(e)
            
class CreateStudentRecord(APIView):
    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"error":False, "message": "Student record created successfully"})
            return Response({"error":True, "message": serializer.errors})
        except Exception as e:
            return Response({"error":True, "message": str(e)})

class UpdateStudentRecord(APIView):
    def post(self, request, id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"error": False, "message": "Student record updated successfully"})
            return Response({"error": True, "message": serializer.errors})
        except Student.DoesNotExist:
            return Response({"error": True, "message": "Student not found"})
        except Exception as e:
            return Response({"error": True, "message": str(e)})

class RemoveStudentRecord(APIView):
    def post(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({"error": False, "message": "Student record deleted successfully"})
        except Exception as e:
            return Response({"error": True, "message": str(e)})
