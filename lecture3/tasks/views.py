from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)#blank arguments to print new as blank
        #filled up to collect all the data from user

        # Check if form data is valid (server-side)
        if form.is_valid():
            task = form.cleaned_data["task"]#to get access of all the data that user submitted
            
            #to append the task in the list
            request.session["tasks"] += [task]
            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("index"))
        else:
             return render(request, "tasks/add.html", {
        "form": form
    })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
