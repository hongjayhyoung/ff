from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

# Create your views here.
def home(request):
    persons = Person.objects
    return render(request, 'portfolio/home.html')

def detail(request, person_id):
    person_detail = get_object_or_404(Person, pk = person_id)
    return render(request, 'portfolio/detail.html', {'person': person_detail})


def person_new(request):
    if request.method=="POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('detail', person.pk)
    else:
        form = PersonForm()
    return render(request, 'portfolio/new.html', {'form':form})

def person_edit(request,person_id):
    person=get_object_or_404(Person,pk=person_id)
    if request.method=='POST':
        form=PersonForm(request.POST,instance=person)
        if form.is_valid():
            person=form.save(commit=False)
            person.save()
            return redirect('new',person_id=person.pk)s
    else:
        form=PersonForm(instance=person)
        return render(request,'portfolio/edit.html',{'form':form})