from django.shortcuts import render
import requests
import datetime 


def index(request):
    data=None
    a=None
    b=None 
    c=None 
    d=None 
    e=None 
    f=None 
    g=None 
    h=None
    i=None
    j=None
    now=None
    if request.method=='POST':
      city=(request.POST)
      #print(city.get('city'))
      city=str(city.get('city'))
      url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2dc38f73ffe4adb439c42a01b79e7aa1'
      data=requests.get(url).json()
      a=round((data['main']['temp'])-273,2)
      b=round((data['main']['feels_like'])-273,2)
      c=round((data['main']['temp_min'])-273,2)
      d=round((data['main']['temp_max'])-273,2)
      e=round((data['main']['pressure']))
      f=data['weather'][0]['description']
      g=round((((data['wind']['speed'])*18)/5),2)
      h=data['main']['humidity']
      i=data['name']
      j=data['weather'][0]['icon']
      now=datetime.datetime.now()
    context={'data':data,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'now':now}
    return render(request,'weatherapp/index.html',context)
