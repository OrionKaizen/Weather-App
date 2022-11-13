from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title('Weather App')
root.geometry('900x500+300+200')
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
    
        geolocator= Nominatim(user_agent='geoapiExercises')
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime('%I:%M %p')
        clock.config(text=current_time)
        name.config(text='CURRENT WEATHER')
    
        #weather
        api='https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1feabdf94659cf3c56f3ba6f101251c8'
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']*1.8-459.67)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,'°'))
        c.config(text=(condition, '|', 'FEELS', 'LIKE',temp,'°'))
    
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!")

#search box
Search_image=PhotoImage(file='SearchBar.png')
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'), bg='#000000', border=0, fg='white')
textfield.place(x=90,y=85)
textfield.focus()

Search_icon=PhotoImage(file="SearchIcon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0,cursor="hand2", bg='#000000',command=getWeather)
myimage_icon.place(x=360,y=92)

#logo
Logo_image=PhotoImage(file='LogoImage.png')
logo=Label(image=Logo_image, borderwidth=0, bg='#999999')
logo.place(x=150,y=135)

#Bottom box
Frame_image=PhotoImage(file='RedBox.png')
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font= ('arial', 15,'bold'),bg='#999999')
name.place(x=30,y=180)
clock=Label(root,font=('Helvetica',20),bg='#999999')
clock.place(x=30,y=210)

#label
label1=Label(root,text='WIND',font=('Helvetica',15,'bold'),fg='white',bg='#eb4a5a')
label1.place(x=180,y=400)

label2=Label(root,text='HUMIDITY',font=('Helvetica',15,'bold'),fg='white',bg='#eb4a5a')
label2.place(x=290,y=400)

label3=Label(root,text='DESCRIPTION',font=('Helvetica',15,'bold'),fg='white',bg='#eb4a5a')
label3.place(x=447,y=400)

label4=Label(root,text='PRESSURE',font=('Helvetica',15,'bold'),fg='white',bg='#eb4a5a')
label4.place(x=650,y=400)

t=Label(font=('arial', 70,'bold'),fg='#ee666d')
t.place(x=550,y=150)
c=Label(font=('arial',15,'bold'))
c.place(x=550,y=250)

w=Label(text='...',font=('arial',20,'bold'),bg='#eb4a5a')
w.place(x=170,y=430)
h=Label(text='...',font=('arial',20,'bold'),bg='#eb4a5a')
h.place(x=315,y=430)
d=Label(text='...',font=('arial',20,'bold'),bg='#eb4a5a')
d.place(x=380,y=430)
p=Label(text='...',font=('arial',20,'bold'),bg='#eb4a5a')
p.place(x=650,y=430)




root.mainloop()
