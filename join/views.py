from django.shortcuts import render, redirect
from django.views import View
import requests
import json
# Create your views here.


# 이용약관 동의 뷰
class AgreeView(View):
    def get(self, request):
        return render(request, 'join/agree.html')

    def post(self, request):
        pass

# 본인확인 뷰
class CheckmeView(View):
    def get(self, request):
        return render(request, 'join/checkme.html')

    def post(self, request):
        SECRET_KEY = '6Lfc8qYgAAAAADTeEg2dB6tlHI25bUH3WiVuz0p2'
        VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'
        form = request.POST.dict()

        params = {'secret': SECRET_KEY, 'response': form['g-recaptcha']}

        result = requests.get(VERIFY_URL, params=params).json

        if result['success']:
            tokens = {'name': form['name'], 'phone': form['phone']}

            tokens = json.dumps(tokens, ensure_ascii=True)
            print(tokens)

            res = redirect('/join/joinme')
            res.set_cookie('tokens',tokens, max_age=60*30)
            return res
        else:
            error='자동가입방지 인증이 실패했습니다'

        context = {'form': form, 'error': error}
        return render(request, 'join/checkme.html', context)

# 정보기입 뷰
class JoinmeView(View):
    def get(self, request):
        cookie = request.COOKIES.get('tokens')
        try:
            return render(request, 'join/joinme.html', eval(cookie))
        except:
            return redirect('/join/agree')

    def post(self, request):
        pass


# 가입완료 뷰
class JoinokView(View):
    def get(self, request):
        # return render(request, 'join/joinok.html')
        pass

    def post(self, request):
        pass

# 회원가입관련 뷰
class ZipcodeView(View):
    pass

class UseridView(View):
    pass