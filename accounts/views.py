from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
from accounts.forms import SignUpForm


class TopPageView(TemplateView):
    template_name = 'TopPage.html'


toppageview = TopPageView.as_view()


class IndexView(TemplateView):
    template_name = 'index.html'


indexview = IndexView.as_view()


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'signup.html', context)
