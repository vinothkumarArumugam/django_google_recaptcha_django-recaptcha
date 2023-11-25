from django.shortcuts import render,HttpResponse
from contact.forms import ContactForm
def contact_view(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("yeah !,you are a human")
        else:
            return HttpResponse("oops! bot suspected")
    else :
        form=ContactForm()
    return render(request,"contact/contact.html",{"form":form})        

# Create your views here.
