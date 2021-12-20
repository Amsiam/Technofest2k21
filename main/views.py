from django.shortcuts import redirect, render
from django.views import View
from .models import Question, Answer, Points
from django.contrib import messages
from django.contrib.auth import login, logout as authLogout, authenticate


class Index(View):
    def get(self, request):
        return render(request, "main/index.html")


class Problem(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
        problem = Question.objects.order_by('point').all()

        solvedlist = []

        for p in problem:
            try:
                ans = request.user.answer.filter(question=p).get()
                if ans:
                    solvedlist.append(ans.question)
            except:
                pass

        return render(request, "main/problems.html", context={"problem": problem, "solvedlist": solvedlist})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
        ans = request.POST.get('ans')
        pid = request.POST.get('pId')

        try:
            p = Question.objects.get(id=pid)
        except:
            messages.error(request, 'Problem Not Found')
            return redirect('/problems')

        if(p.question_answer == ans):
            messages.success(request, 'Congrats! You have right one.')
            ans = Answer.objects.create(user=request.user, question=p)
            ans.save()

            try:
                points = Points.objects.get(user=request.user)

            except:
                points = Points.objects.create(user=request.user)

            points.total_point += p.point
            points.save()
        else:
            messages.error(request, 'Try again')

        return redirect('/problems')


class Rank(View):
    def get(self, request):
        userrank = Points.objects.order_by("-total_point").all()
        return render(request, "main/rank.html", {"userrank": userrank})


class Login(View):
    def get(self, request):
        return render(request, "main/login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if(user):
            login(request, user)
            return redirect('/problems')
        else:
            messages.error(request, "Wrong username of password")
            return render(request, "main/login.html", {"username": username, "password": password})


def logout(request):
    authLogout(request)
    return redirect("/")
