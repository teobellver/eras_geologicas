import json, tkinter
from tkinter import ttk
from tkinter import *
app=tkinter.Tk()
app.config(width=300, height=300, cursor="cross")
app.title("Estructuras geologicas")
data='''{
    "Cenozoica cuartica": {
        "6":"Cuenca Del Chaco Paranaense",
        "8":"Cuenca Neuquina",
        "9":"Cuenca Del Colorado",
        "10":"Patagonia austral"
    },
    "Precambrica":{
        "1":"Puna",
        "7":"Sierras Pampeanas",
        "3":"Nesocraton Norpatagonico",
        "2":"Nesocraton Del Deseado",
        "5":"Tandilia",
        "20":"Meseta De Misiones"
    },
    "Mezosoica": {
        "11":"Cuenca del Golfo de San Jorge"
    },
    "Paleozoica":{
        "4":"Ventania",
        "15":"Cordillera oriental",
        "13":"Precordillera San Juan, Mendoza, La Rioja",
        "12":"Cordillera Frontal",
        "14":"Provincia Geologica de San Rafaelino Pampeana"
    },
    "Cenozoica terciaria":{
        "16":"Cordillera Principal",
        "17":"Andes Patagonicos Fueguiños",
        "18":"Sierra Sub Andinas",
        "19":"Sistema Famatina"
    }
}'''
## convierte string con formato object (json) a un dictionary de python
jsondata= json.loads(data)
num_era_geologica=0
for key, value in jsondata.items() :
    era=Label(text=str(num_era_geologica)+". "+ key)
    era.pack()
    era.place(x=10,y=((num_era_geologica+1)*20))
#    print (str(num_era_geologica)+". "+ key)
    num_era_geologica+=1
text= ttk.Entry()
text.pack()
text.place(x=20, y=200)
label=Label(text="Eras geologicas:")
label.pack()
label.place(x=10,y=5)
categoriatkinter=0

def estructuras(value2):
    num_era_geologica=0
    for key, value in value2.items():
        estructura=Label(text=value)
        estructura.pack
        estructura.place(x=10, y=240+num_era_geologica*30)
        num_era_geologica+=1

def activate():
    categoriatkinter=text.get()
    num_era_geologica=0
    for key, value in jsondata.items() :
        if int(categoriatkinter)==num_era_geologica:
            label=Label(text="Estructuras de la era "+ key + ":")
            label.pack()
            label.place(x=10, y=200)
            app.config(width=300,height=500)
            text.place(x=20, y=150)
            button.place(x=150, y=150)

            estructuras(value)
        num_era_geologica+=1
def destroy():
    app.destroy()
button=Button(app, text="Recover")
button.config(command=activate, cursor="man")
button.place(x=150, y= 200)
Button=Button(app, text="Quit", command=destroy)
Button.pack
Button.place(x=200, y=20)
app.mainloop()

#print(jsondata[categoria][id_estructura])

## convierte dictionary de python en json (cadena de caracteres), lo cual facilita su transmisión
##y=json.dumps(data)
## print(y)