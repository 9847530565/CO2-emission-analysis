import os
from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tkinter import messagebox
class CO2model:
    def __init__(self):
        #self.generate=False
        self.count=1
        self.df=pd.read_csv("Dataset/CO2 Emissions_Canada.csv")
        self.root=Tk()
        self.root.geometry("500x500")
        self.root.title("Car Quality classifier")
        self.icon=PhotoImage(file="Images/icon.png")
        self.root.iconphoto(True,self.icon)
        self.root.resizable(False,False)
        self.canvas=Canvas(self.root,width=500,height=500)
        self.canvas.pack()
        self.photo=PhotoImage(file="Images/background.png")
        self.canvas.create_image(0,0,anchor=NW,image=self.photo)
        Label(self.root,text="Car Quality Classifier",font=("Arieal",30),fg="Black",bg="Orange").place(relx=0.1,rely=0.05)
        #engine size
        self.enginecount=DoubleVar(self.root)
        Label(self.root,text="enter Engine Size(in L)",font=("Arieal",10),fg="Navy",bg="Teal").place(relx=0.05,rely=0.2)
        Entry(self.root,text=self.enginecount,fg="Pink",bg="Maroon",font=("Arieal",10)).place(relx=0.65,rely=0.2)
        #Citywise fuel consumption
        self.fuelcity=DoubleVar(self.root)
        Label(self.root,text="enter citywise fuel consumption(L/100km)",font=("Arieal",10),fg="Navy",bg="Teal").place(relx=0.05,rely=0.3)
        Entry(self.root,text=self.fuelcity,fg="Pink",bg="Maroon",font=("Arieal",10)).place(relx=0.65,rely=0.3)
        #Highway wise fuel consumption
        self.fuelhighway=DoubleVar(self.root)
        Label(self.root,text="enter highway fuel consumption(L/100km)",font=("Arieal",10),fg="Navy",bg="Teal").place(relx=0.05,rely=0.4)
        Entry(self.root,text=self.fuelhighway,fg="Pink",bg="Maroon",font=("Arieal",10)).place(relx=0.65,rely=0.4)
        #Comb fuel consumption
        self.fuelcomb=DoubleVar(self.root)
        Label(self.root,text="enter comb fuel consumption(L/100km)",font=("Arieal",10),fg="Navy",bg="Teal").place(relx=0.05,rely=0.5)
        Entry(self.root,text=self.fuelcomb,fg="Pink",bg="Maroon",font=("Arieal",10)).place(relx=0.65,rely=0.5)
        #no of cylinders
        Label(self.root,text="Select No of Cylinders",font=("Arieal",10),fg="Navy",bg="Teal").place(relx=0.05,rely=0.6)
        self.cylinder=IntVar(self.root)
        Entry(self.root,text=self.cylinder,fg="Pink",bg="Maroon",font=("Arieal",10)).place(relx=0.65,rely=0.6)
        #model generator
        Button(self.root,text="Generate Model",font=("Arieal",15),command=self.generate,bg="Black",fg="Orange").place(relx=0.1,rely=0.9)
        #Car classifier
        Button(self.root,text="apply model",font=("Arieal",15),command=self.apply,bg="Black",fg="Orange").place(relx=0.5,rely=0.9)
    def generate(self):
        X=self.df.loc[:,"Engine Size(L)":'Fuel Consumption Comb (mpg)']
        X=X.drop(['Transmission','Fuel Type','Fuel Consumption Comb (mpg)'],axis=1)
        Y=self.df.loc[:,'CO2 Emissions(g/km)']
        x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.8,random_state=0)
        self.lin_reg=LinearRegression()
        self.lin_reg.fit(x_train,y_train)
        messagebox.showinfo("information","model generated successfully")
    def apply(self):
        try:
            prediction=self.lin_reg.predict([[self.enginecount.get(),self.cylinder.get(),self.fuelcity.get(),self.fuelhighway.get(),self.fuelcomb.get()]])
            if prediction[0]<100:
                condition="Best"
            elif 100<=prediction[0]<200:
                condition="Good"
            elif 200<=prediction[0]<300:
                condition="Average"
            elif 300<=prediction[0]<400:
                condition="Bad"
            else:
                condition="Worst"
            messagebox.showinfo("Result",f"Your vehicle is in its {condition} condition with estimate CO2 emission of {prediction[0]} g/km")
        except:
            messagebox.showerror("Error","Model Not generated")
sample=CO2model()
