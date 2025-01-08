from random import choice

def getWeather():
    weather = ['맑음', '비', '눈', '폭우', '돌풍', '따뜻']
    return choice(weather)