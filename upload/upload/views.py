from django.shortcuts import render
from django.http import HttpResponse
from .models import Document, seops
import csv
from pathlib import Path

def index(request):
    return HttpResponse("Hello, World. You're at the index.")

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = Document.objects.all()

    return render(request, "upload/upload-file.html", context = {"files": documents})

def csvToModel(request):
        path = '../media/Uploaded Files/email3.csv'
        abs_path = Path(__file__).parent.resolve().joinpath(path)

        file = open(abs_path)
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(seops(name=row[0],
                              email=row[1]))
            seops.objects.bulk_create(list)

        return HttpResponse('create model')