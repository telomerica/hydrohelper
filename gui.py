import tkinter as tt
import elems as el
import nutrients as nt
import os
import json

class GUI:
    def __init__(self):
        self.gui = tt.Tk()
        self.gui.title("HydroHelper")
        self.gui.geometry("370x400")
        self.gui.resizable(0,0)
        self.dir = f'{os.getcwd()}/'
        self.dir_saved = f'{os.getcwd()}/saved'
        #self.gui.iconbitmap(f'{self.dir}icon.ico')
        self.on_screen = []
        self.new_screen(0)
    
    def new_screen(self,x):
        
        for i in self.on_screen:
            i.grid_forget()
        self.on_screen.clear()
        
        if x==0:
            self.gui.geometry("370x400")

            introductory_text = tt.Label(text="Welcome to HydroHelper, from here you can choose an \naction, such as defining a new nutrient or making \ncalculations based on pre-defined nutrients")
            introductory_text.grid(row=0,column=0,columnspan=4)
            self.on_screen.append(introductory_text)

            btn_to_scr1  = tt.Button(bg="darkgrey",width=20,borderwidth=3,text="Define a new nutrient",command = lambda: self.new_screen(1))
            btn_to_scr1.grid(row=1,column=1,columnspan=2)
            self.on_screen.append(btn_to_scr1)

            btn_to_scr3 = tt.Button(bg="darkgrey",width=20,borderwidth=3,text="Run calculations",command = lambda: self.new_screen(3))
            btn_to_scr3.grid(row=2,column=1,columnspan=2)
            self.on_screen.append(btn_to_scr3)
        
        elif x==1:
            self.el_ls_nutrient=[]
            for i in el.elements_ls:
                i.v = tt.StringVar()
                i.btn = tt.Checkbutton(the_gui.gui,text=i.name,width=5,height=2,borderwidth=3,variable=i.v)
                i.lbl = tt.Label(the_gui.gui,text=i.name,width=5)
                i.ent = tt.Entry(the_gui.gui,borderwidth=2)
                
                i.btn.grid(row=int(el.elements_ls.index(i)/5),column=int(el.elements_ls.index(i)%5))
                i.btn.deselect()
                self.on_screen.append(i.btn)
            
            btn_submit_nut = tt.Button(bg="darkgrey",width=20,borderwidth=3, text = "Submit this", command = lambda:self.yeyo())
            btn_submit_nut.grid(row=(int(el.elements_ls.index(i)/5))+1,column=1,columnspan=3)
            self.on_screen.append(btn_submit_nut)
        
        elif x==2:
            self.nut_name = tt.Label(the_gui.gui,text="Name of the nutrient:")
            self.nut_name.grid(row=0,column=0)
            self.on_screen.append(self.nut_name)
            self.nut_name_ent=tt.Entry(the_gui.gui,borderwidth=2)
            self.nut_name_ent.grid(row=0,column=1)
            self.on_screen.append(self.nut_name_ent)
            
            for i in (self.el_ls_nutrient):
                i.lbl.grid(row=self.el_ls_nutrient.index(i)+1,column=0)
                self.on_screen.append(i.lbl)
                i.ent.grid(row=self.el_ls_nutrient.index(i)+1,column=1)
                self.on_screen.append(i.ent)
                
            self.set_button = tt.Button(bg="darkgrey",width=20,borderwidth=3,text= "Save this nutrient",command=lambda:self.save())
            self.set_button.grid(row=self.el_ls_nutrient.index(i)+2,column=1)  
            self.on_screen.append(self.set_button)
            self.return_scr1 = tt.Button(bg="darkgrey",width=20,borderwidth=3,text="Return to previous screen",command=lambda:self.new_screen(1))  
            self.return_scr1.grid(row=self.el_ls_nutrient.index(i)+2,column=0)
            self.on_screen.append(self.return_scr1)
        
        elif x==3: 
            k=-1
            
            for i in os.listdir(f"{os.getcwd()}/saved"):
                k+=1
                with open(f"{os.getcwd()}/saved/{i}","r") as file:
                    data = file.read()
                    data1 = json.loads(data)

                self.define_button(name=i[:-5],data1=data1,k=k)
                
            self.rtn = tt.Button(text="Return to previous screen",bg="darkgrey",width=20,borderwidth=3,command=lambda: self.new_screen(0))
            self.rtn.grid(column=3,row=int(k/3)+1)
            self.on_screen.append(self.rtn)
            
            self.gui.geometry(f"580x{(int(k/3)*20)+400}")

  
    def yeyo(self):
        for i in el.elements_ls:
            if (i.v.get())=="1":
                self.el_ls_nutrient.append(i)
        self.new_screen(2)
    
    def save(self):

        saved_nut = {}

        for i in self.el_ls_nutrient:
            saved_nut[i.name]=i.ent.get()

        dirc = (f"{self.dir_saved}/{self.nut_name_ent.get()}.json")
        didi = open(dirc,"w+")
        json.dump(saved_nut,didi)
        
        self.new_screen(0)

    def define_button(self,name,data1,k):
        print("yea")
        n= nt.Nutrient(name=name,lcomposition=data1)
        n.btn = tt.Button(text=f'+{name}',bg="darkgrey",width=20,borderwidth=3, command = lambda: self.add(n))
        n.btn.grid(column=int(k%3),row=int(k/3))
        self.on_screen.append(n.btn)
    
    def add(self,n):
        for i in nt.nutrients_list:
            i.btn.configure(bg="darkgrey")
        print(n.name)
        n.btn.config(bg="lightblue")

the_gui = GUI()
the_gui.gui.mainloop()