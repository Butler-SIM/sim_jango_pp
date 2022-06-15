from datetime import datetime, timedelta
import random
from time import timezone

import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from etc.models import LottoNumber
from etc.serializers import LottoNumberSerializer
from bs4 import BeautifulSoup


def etcList(request):

    return render(request, 'main.html')


class LottoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = LottoNumber.objects.all()
    serializer_class = LottoNumberSerializer

    def get_lotto_numer(self, request):
        number_list = []
        for i in range(0,7):
            for j in range(0,7):
                my_number = random.sample(range(1, 46), 6)
                my_number.sort()
                print(f'{my_number}')
            number_list.append({f"number_dic{i}": my_number})
            print("======================")
            print(f'{my_number}')

            LottoNumber.objects.create(number_01=my_number[0], number_02=my_number[1], number_03=my_number[2],
                                       number_04=my_number[3], number_05=my_number[4], number_06=my_number[5])

        return JsonResponse({'number_list : ': number_list})


def get_week_lotto_check(request):
    # 매주 토요일 오후 11시 실행

    getWinNumbers(getMaxRoundNum()).get('win_nums')

    win_num = getWinNumbers(getMaxRoundNum()).get('win_nums')

    print(win_num)
    first_date = datetime(2022, 2, 20)
    last_date = datetime(2022, 7, 1)

    print("!!" , datetime.now())

    today = datetime.today().strftime("%Y%m%d")
    print("투데이1", today, "type :", type(today))
    today = datetime.strptime(today, "'%Y%m%d'").date()
    print("투데이1", today, "type :", type(today))

    print(LottoNumber.objects.filter(created_at__range=(first_date, last_date)).values())
    print(LottoNumber.objects.filter(created_at__range=datetime.now().strftime("%Y%m%d").date() - timedelta(days=1)).values())
    return JsonResponse({"ss": "ssss"})


def getMaxRoundNum() -> int:
    url = "https://dhlottery.co.kr/common.do?method=main"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find(name="strong", attrs={"id": "lottoDrwNo"})
    return int(tag.text)


def getWinNumbers(round_num: int):

    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={round_num}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    win_result_tag = soup.find(name="div", attrs={"class": "win_result"})

    # 회차 정보 읽기
    strong_tags = win_result_tag.find_all("strong")
    round_num_text = strong_tags[0].text.replace("회", '')
    round_num_query = int(round_num_text)
    # 추첨일 읽기
    p_tags = win_result_tag.find_all("p", "desc")
    draw_date = datetime.strptime(p_tags[0].text, "(%Y년 %m월 %d일 추첨)")
    # 당첨번호 6개 읽기
    num_win_tag = win_result_tag.find(name="div", attrs={"class": "num win"})
    p_tag = num_win_tag.find("p")
    win_nums = [int(x.text) for x in p_tag.find_all("span")]
    # 보너스 번호 읽기
    num_bonus_tag = win_result_tag.find(name="div", attrs={"class": "num bonus"})
    p_tag = num_bonus_tag.find("p")
    bonus_num = int(p_tag.find("span").text)

    return {
        "round_num": round_num_query,
        "draw_date": draw_date,
        "win_nums": win_nums,
        "bonus_num": bonus_num
    }