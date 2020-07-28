import tkinter as tk
import requests
from PIL import Image, ImageTk
app = tk.Tk()
app.iconphoto(False, tk.PhotoImage(file='icona.png'))
app.title('Počasí')
vyska = 720
sirka = 1080


#{'coord': {'lon': 14.74, 'lat':  49.68}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 24.21, 'feels_like': 25.86, 'temp_min': 23.33, 'temp_max': 25.56, 'pressure': 1012, 'humidity': 60}, 'visibility': 10000, 'wind': {'speed': 0.45, 'deg': 214, 'gust': 2.68}, 'clouds': {'all': 66}, 'dt': 1595695245, 'sys': {'type': 3, 'id': 2030980, 'country': 'CZ', 'sunrise': 1595647342, 'sunset': 1595703148}, 'timezone': 7200, 'id': 3079508, 'name': 'Pičín', 'cod': 200}

# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}


#nastavení asi
def format1(weather_json): 
	try:
            mesto = weather_json['name']
            desc = weather_json['weather'][0]['description']
            teplota_max = round(weather_json['main']['temp_max'])
            teplota_min = round(weather_json['main']['temp_min'])
            #překlad
            en_1 = "clear sky"
            if desc == en_1:
               desc = ("Jasno")
        
            en_2 = "few clouds"
            if desc == en_2:
               desc = ("Polojasno")
            
            en_3 = "scattered clouds"
            if desc == en_3:
               desc = ("Zataženo")
            
            en_4 = "broken clouds"
            if desc == en_4:
               desc = ("Zataženo")
            
            en_5 = "shower rain"
            if desc == en_5:
               desc = ("Déšť")
            
            en_6 = "rain"
            if desc == en_6:
               desc = ("Déšť")
            
            en_7 = "thunderstorm"
            if desc == en_7:
               desc = ("Bouřka")
            
            en_8 = "snow"
            if desc == en_8:
               desc = ("Sněží")
            
            en_9 = "mist"
            if desc == en_9:
               desc = ("Mlha")
            
            en_10 = "Prague"
            if mesto == en_10:
               mesto = ("Praha")
         
            vysledek = 'Podmínky: %s \nMax. teplota: %s°c \nMin. teplota: %s°c' % (desc, teplota_max, teplota_min)
	except:
		vysledek = ''
	return vysledek

def format2(weather_json): 
	try:
            mesto = weather_json['name']  
            teplota = round(weather_json ['main']['temp'])
            vysledek = '%s\n %s°c' % (mesto, teplota) 
	except:
		vysledek = 'Došlo k potížím!'
	return vysledek

def format3(weather_json): 
	try:
            rychlos_vetru = weather_json['wind']['speed']
            tlak= weather_json['main']['pressure']
            vysledek = '%sm/s \nTlak: %s hPa \n' % (rychlos_vetru, tlak)
	except:
		vysledek = ''
	return vysledek



   


def pocasi(city):
   pocasi_key = '9f7913914b03b001c0cca319edf16901'
   url = 'https://api.openweathermap.org/data/2.5/weather'
   params = {'APPID': pocasi_key, 'q': city, 'units': 'Metric'}
   response = requests.get(url, params=params)
   weather_json = response.json()



   label['text'] = format2(response.json())
   label2['text'] = format1(response.json())
   label3['text'] = format3(response.json())

   icon_name = weather_json['weather'][0]['icon']
   open_image(icon_name)

def open_image(icon):
   size = int(spodní_frame.winfo_height()*0.25)
   img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
   weather_icon.delete("all")
   weather_icon.create_image(0,0, anchor='nw', image=img)
   weather_icon.image = img





#obrázek
C = tk.Canvas(app, height=vyska, width=sirka)
zadni_obrazek= tk.PhotoImage(file='Weather2.png')
zadni_label = tk.Label(app, image=zadni_obrazek)
zadni_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

frame = tk.Frame(app, bg='#ffc766', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth= 0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('calibri', 20, 'bold'))
entry.place(relwidth=0.65, relheight=1)

tlačítko = tk.Button(frame, borderwidth= 0, bg='#6bff6e',activebackground='#60f063',  text="Počasí", font=('calibri',25, 'bold') ,command=lambda: pocasi (entry.get()))
tlačítko.place(relx=0.7, relheight=1, relwidth=0.3)


#spodni_frame
spodní_frame= tk.Frame(app, bg='#ffc766', bd=10 )   
spodní_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#teplota + mesto(format2)
label = tk.Label(spodní_frame, font=('Andale Mono', 45, 'bold'),bg='#243755' ,anchor='center',justify= 'left', foreground="white")
label.place(relwidth=1, relheight=0.5)

#temp_min + temp_max + desc (format1)
label2 = tk.Label(spodní_frame, font=('Andale Mono', 15, 'bold'),bg='#243755' ,anchor='center',justify= 'left', foreground="white")
label2.place(rely= 0.5,relwidth=0.5, relheight=0.5 )

#rychlos_vetru + tlak (format3)
label3 = tk.Label(spodní_frame, font=('Andale Mono', 15, 'bold'),bg='#243755' ,anchor='center',justify= 'left', foreground="white")
label3.place(rely= 0.5,relwidth=0.5, relheight=0.5, relx= 0.5 )




#icona_pocasi
weather_icon = tk.Canvas(label, bg='#243755', bd=0, highlightthickness=0)
weather_icon.place(relx=0.75, rely=0.25, relwidth=1, relheight=0.5)



app.mainloop()
#243755 - barva

