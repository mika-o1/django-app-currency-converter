import json

import requests
from django.shortcuts import render


def get_currency(request):
    context = {}
    if request.method == "POST":
        currency = request.POST["currency"]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/77.0.3865.90 Safari/537.36"}
        if currency == "USD":
            url = f'https://www.google.ru/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0&newwindow=1&ei=17IwY7PtNo2HrwSyoZ3gAg&oq=%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzINCAAQRxDWBBCwAxDJAzIICAAQkgMQsAMyCggAEEcQ1gQQsAMyCggAEEcQ1gQQsAMyBwgAELADEEMyBwgAELADEEMyBwgAELADEEMyDQgAEOQCENYEELADGAEyDQgAEOQCENYEELADGAEyDQgAEOQCENYEELADGAEyEgguEMcBENEDEMgDELADEEMYAkoECEEYAEoECEYYAVAAWABgugloAXABeACAAQCIAQCSAQCYAQDIARDAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz'
            currency = "Доллар"
        elif currency == "EURO":
            url = f'https://www.google.ru/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0+%D0%B5%D0%B2%D1%80%D0%BE&newwindow=1&ei=3LIwY_uqOqXrrgTTvI-QDg&ved=0ahUKEwj7iPCp3bD6AhWltYsKHVPeA-IQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoNCAAQRxDWBBCwAxDJAzoICAAQkgMQsAM6CggAEEcQ1gQQsAM6BwgAELADEEM6BAgAEEM6BwgAEMkDEEM6BwgAEIAEEApKBAhBGABKBAhGGABQ9QVYwxZgxx9oAXABeACAAWyIAYsEkgEDMC41mAEAoAEByAEKwAEB&sclient=gws-wiz'
            currency = "Евро"
        else:
            url = f'https://www.google.ru/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&newwindow=1&ei=ObMwY5SnJ8rRqwGm-YfoDw&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0+%D1%80%D1%83&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoNCAAQRxDWBBCwAxDJAzoICAAQkgMQsAM6BwgAELADEEM6BggAEB4QFjoICAAQHhAWEAo6CQgAEB4QyQMQFkoECEEYAEoECEYYAFC1BVj8DWCPG2gCcAF4AIABgQGIAdsCkgEDMS4ymAEAoAEByAEKwAEB&sclient=gws-wiz'
            currency = "рубль"
        response = requests.get(url=url, headers=headers)

        data1 = response.text
        data2 = data1.split(sep='converter-container converter-container-in-grid')[0]
        data3 = data2.split(sep='class="converter-container__item-input-wrapper')[1]
        data4 = data3.split(sep='type="tel')[0]

        context["currency"] = f"Валюта в {currency}: {data4}"
    return render(request, 'app_heroku/pages/CurrencyPage.html', context)