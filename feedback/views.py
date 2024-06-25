from django.shortcuts import render, redirect
from .forms import FeedbackForm


def contact(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts_success")
    else:
        form = FeedbackForm()

    return render(request, "contacts.html", {"form": form})


def contacts_success(request):
    return render(request, "contacts_success.html")
