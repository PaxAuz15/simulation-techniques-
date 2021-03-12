import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import itertools
import math
from math import sqrt
from tkinter import ttk
from tkinter import messagebox
import webbrowser



#------------------------------------------------------------------------------------------------

def CuadradoMedio():

	win=tk.Toplevel()
	win.title("Método del Cuadrado Medio")
	win.configure(bg="#EBF5FB")


	def enablebotons(boton):
		if(bcalcularCM['state']==tk.NORMAL):
			bcalcularCM['state']=tk.DISABLED

	yy=[]
	def calculoCM():

		r=int(esemilla.get())
		iteraciones=int(eiteraciones.get())

		l=len(str(r)) # determinamos el número de dígitos
		lista = [] # almacenamos en una lista
		lista2 = []
		i=1
		#while len(lista) == len(set(lista)):
		while i <= iteraciones:
			x=str(r*r) 
			if l % 2 == 0:
				x = x.zfill(l*2)
			else:
				x = x.zfill(l)

			y=(len(x)-l)/2
			y=int(y)
			r=int(x[y:y+l])
			lista.append(r)
			lista2.append(x)
			i=i+1

		df = pd.DataFrame({'X2':lista2,'Xi':lista})
		dfrac = df["Xi"]/10**l
		df["ri"] = dfrac
		for i in dfrac:
			yy.append(i)
		
		root = tk.Toplevel()
		root.title("Tabla y gráfico del Método del Cuadrado Medio")
		root.configure(bg="#EBF5FB")
		frame=tk.Frame(root, height=400,width=350,bg="#EBF5FB")
		frame.pack(side=tk.LEFT)
		table = tk.Text(frame)
		table.insert(tk.INSERT, df.to_string())
		table.place( x=10, y=10, height=390, width=320)

		frame2=tk.Frame(root,bg="#EBF5FB")
		frame2.pack(side=tk.RIGHT)

		iteraciones=float(eiteraciones.get())

		#------------------------------CREAR GRAFICA---------------------------------
		fig = Figure(figsize=(5, 4), dpi=100)
		yyy=np.arange(0,iteraciones)
		fig.add_subplot(111).plot(yyy,yy)#AÑADIR "subbplot"

		canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		# -----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
		toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


		root.mainloop()



	ltitulovacio=tk.Label(win, width=20, height=2,bg="#EBF5FB")
	lvacio=tk.Label(win, width=25, height=1,bg="#EBF5FB")

	lsemilla=tk.Label(win, text="Semilla: ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")
	literaciones=tk.Label(win, text="Iteraciones: ",width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")
	

	esemilla=tk.Entry(win)
	eiteraciones=tk.Entry(win)

	#bsalir=tk.Button(win,text="Salir", width=17, height=1,command=win.destroy)
	bcalcularCM=tk.Button(win, text="Calcular", width=17, height=1,command=lambda:[enablebotons(bcalcularCM),calculoCM()],font="Arial 10 bold", bg="#2E86C1", activebackground="#5DADE2",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	bnuevocalculo=tk.Button(win,text="Nuevo cálculo", width=17, height=1, command=lambda:[win.destroy(),CuadradoMedio()],font="Arial 10 bold", bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
	

	ltitulovacio.grid(row=1,column=1)
	lvacio.grid(row=5,column=1)

	lsemilla.grid(row=1,column=0)
	literaciones.grid(row=2,column=0)

	esemilla.grid(row=1,column=1)
	eiteraciones.grid(row=2,column=1)
	
		
	bcalcularCM.grid(row=4,column=1)
	bnuevocalculo.grid(row=4,column=0)
	#bsalir.grid(row=7,column=1)
	win.mainloop()

#------------------------------------------------------------------------------------------------

def CongruencialAditivo():
	#ventana.deiconify()
	win=tk.Toplevel()
	#win.geometry('800x600')
	win.title("Método Congruencial Aditivo")
	win.configure(bg="#EBF5FB")

	def enablebotons():
		if(bcalcular['state']==tk.NORMAL):
			bcalcular['state']=tk.DISABLED
			
	yy2=[]
	yy=[]
	def calculoCA():

		m=int(emodulo.get())
		a=int(eiteraciones.get())
		x0=int(esemilla.get())
		c=int(eincremento.get())
		n1=int(eincre.get())


		x = [1] * n1
		r = [0.1] * n1
		for i in range(0, n1):
			x[i] = ((a*x0)+c) % m
			x0 = x[i]
			r[i] = x0 / m
		d = {'ri': r}
		dfrac=d["ri"]

		d = {'Xn': x, 'ri': r }
		dfrac=d["ri"]
		dfrac2=d["Xn"]
		df = pd.DataFrame(data=d)

		for i in dfrac:
			yy.append(i)
		for i in dfrac:
			yy2.append(i)

		root = tk.Toplevel()
		root.title("Tabla y gráfico del Método de Coungrencial Aditivo")
		root.configure(bg="#EBF5FB")
		frame=tk.Frame(root, height=400,width=200,bg="#EBF5FB")
		frame.pack(side=tk.LEFT)
		table = tk.Text(frame)
		table.insert(tk.INSERT, df.to_string())
		table.place( x=10, y=10, height=390, width=180)

		frame2=tk.Frame(root,bg="#EBF5FB")
		frame2.pack(side=tk.RIGHT)

		a=int(eincre.get())

		#------------------------------CREAR GRAFICA---------------------------------
		fig = Figure(figsize=(5, 4), dpi=100)
		yyy=np.arange(0,a)
		fig.add_subplot(111).plot(yyy,yy,marker='o')#AÑADIR "subbplot"

		canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
		toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		# -----------------------------BOTÓN "cerrar"----------------------------------
		
		root.mainloop()
	
	lmodulo=tk.Label(win, text="Módulo (m): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")	
	lsemilla=tk.Label(win, text="Semilla (X0): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")
	literaciones=tk.Label(win, text="Multiplicador (a): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")
	lincremento=tk.Label(win, text="Incremento (c): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")
	lincre=tk.Label(win, text="Iteraciones (n): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")

	#ltitulo=tk.Label(win, text="Variables a ingresar", width=20, height=2)
	#ltitulovacio=tk.Label(win, width=20, height=2)
	lvacio=tk.Label(win, width=25, height=1,bg="#EBF5FB")

	
	emodulo=tk.Entry(win)
	esemilla=tk.Entry(win)
	eiteraciones=tk.Entry(win)
	eincremento=tk.Entry(win)
	eincre=tk.Entry(win)


	bcalcular=tk.Button(win, text="Calcular",width=17, height=1, command=lambda:[enablebotons(),calculoCA()],font="Arial 10 bold",bg="#2E86C1", activebackground="#5DADE2",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	bnuevocalculo=tk.Button(win,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),CongruencialAditivo()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
	

	#ltitulo.grid(row=0,column=0)
	#ltitulovacio.grid(row=0,column=1)
	lvacio.grid(row=7,column=1)

	lmodulo.grid(row=1,column=0)
	lsemilla.grid(row=2,column=0)
	literaciones.grid(row=3,column=0)
	lincremento.grid(row=4,column=0)
	lincre.grid(row=5,column=0)

	emodulo.grid(row=1,column=1)
	esemilla.grid(row=2,column=1)
	eiteraciones.grid(row=3,column=1)
	eincremento.grid(row=4,column=1)
	eincre.grid(row=5,column=1)

	bcalcular.grid(row=6,column=1)
	bnuevocalculo.grid(row=6,column=0)	
	

	win.mainloop()

#------------------------------------------------------------------------------------------------

def CoungrecialMultiplicativo():
	#ventana.deiconify()
	win=tk.Toplevel()
	win.title("Método Congruencial Multiplicativo")
	#win.geometry('800x600')
	win.configure(bg="#EBF5FB")


	def enablebotons():
		if(bcalcular['state']==tk.NORMAL):
			bcalcular['state']=tk.DISABLED
		
	yy=[]
	def calculoCMul():

		m=int(emodulo.get())
		a=int(eiteraciones.get())
		x0=int(esemilla.get())
		n1=int(eincre.get())
		

		x = [1] * n1
		r = [0.1] * n1
		
		for i in range(0, n1):
 			x[i] = (a*x0) % m
 			x0 = x[i]
 			r[i] = x0 / m
		d = {'Xn': x, 'ri': r }
		df = pd.DataFrame(data=d)
		dfrac=d["ri"]
		for i in dfrac:
			yy.append(i)
	
		root = tk.Toplevel()
		root.title("Tabla y gráfico del Método de Coungrencial Multiplicativo")
		root.configure(bg="#EBF5FB")
		frame=tk.Frame(root, height=400,width=200,bg="#EBF5FB")
		frame.pack(side=tk.LEFT)
		table = tk.Text(frame)
		table.insert(tk.INSERT, df.to_string())
		table.place( x=10, y=10, height=390, width=180)

		frame2=tk.Frame(root,bg="#EBF5FB")
		frame2.pack(side=tk.RIGHT)
	
		a=int(eincre.get())
	
		#------------------------------CREAR GRAFICA---------------------------------
		fig = Figure(figsize=(5, 4), dpi=100)
		yyy=np.arange(0,a)
		fig.add_subplot(111).plot(yyy,yy,marker='o')#AÑADIR "subbplot"

		canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
		toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		# -----------------------------BOTÓN "cerrar"----------------------------------
		root.mainloop()
	
	lmodulo=tk.Label(win, text="Módulo (m): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")	
	lsemilla=tk.Label(win, text="Semilla (X0): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")
	literaciones=tk.Label(win, text="Multiplicativo (a): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")
	lincre=tk.Label(win, text="Iteraciones (n): ", width=20, height=2,bg="#EBF5FB",font="Arial 10 bold",fg="#1B4F72")

	#ltitulo=tk.Label(win, text="Variables a ingresar", width=20, height=2,bg="#EBF5FB")
	#ltitulovacio=tk.Label(win, width=20, height=2)
	lvacio=tk.Label(win, width=25, height=1,bg="#EBF5FB")
	
	emodulo=tk.Entry(win)
	esemilla=tk.Entry(win)
	eiteraciones=tk.Entry(win)
	eincre=tk.Entry(win)
	

	#bsalir=tk.Button(win,text="Salir",width=17, height=1,command=win.destroy)
	bcalcular=tk.Button(win, text="Calcular",width=17, height=1, command=lambda:[enablebotons(),calculoCMul()],font="Arial 10 bold",bg="#2E86C1", activebackground="#5DADE2",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	bnuevocalculo=tk.Button(win,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),CoungrecialMultiplicativo()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")

	#ltitulo.grid(row=0,column=0)
	#ltitulovacio.grid(row=0,column=1)
	lvacio.grid(row=6,column=1)
	
	lmodulo.grid(row=1,column=0)
	lsemilla.grid(row=2,column=0)
	literaciones.grid(row=3,column=0)
	lincre.grid(row=4, column=0)

	emodulo.grid(row=1,column=1)
	esemilla.grid(row=2,column=1)
	eiteraciones.grid(row=3,column=1)
	eincre.grid(row=4,column=1)
	
	bcalcular.grid(row=5,column=1)
	bnuevocalculo.grid(row=5,column=0)
	#bsalir.grid(row=7,column=1)

	win.mainloop()

#------------------------------------------------------------------------------------------------

def PromedioMovil():
	
	win=tk.Toplevel()
	win.title("Método de Promedio Móvil")
	win.configure(bg="#E8DAEF")

	def enableboton1():
		if(SizeofArray['state']==tk.NORMAL):
			SizeofArray['state'] = tk.DISABLED
			ApplytoLabel1['state']= tk.NORMAL



	def enableboton2():
		if(ApplytoLabel1['state']== tk.NORMAL):
			calclulo['state'] = tk.NORMAL
			ApplytoLabel1['state']=tk.DISABLED

		elif(calclulo['state'] == tk.NORMAL):
			calclulo['state'] = tk.DISABLED		

		
	lista= []
	def ApplytoLabel():
		
	    xx=size.get()
	    for i in range(xx):
	        element = box_list[round(i,2)].get() # Get value from corresponding Entry
	        #ArrayLabel=tk.Label(win,text=element)
	        lista.append(float(element))  
	        #ArrayLabel.pack()
	
	box_list = []   # Create list of Entrys
	def Boxes():


		def on_configure(event):
			canvas.configure(scrollregion=canvas.bbox('all'))

		canvas = tk.Canvas(win)
		canvas.configure(bg="#E8DAEF")
		canvas.pack(side=tk.LEFT)

		scrollbar = tk.Scrollbar(win, command=canvas.yview)
		scrollbar.pack(side=tk.LEFT, fill='y')
		canvas.configure(yscrollcommand
		 = scrollbar.set,width="170", height="285")
		canvas.bind('<Configure>', on_configure)

		frame = tk.Frame(canvas)
		canvas.create_window((0,0), window=frame, anchor='nw')	

		xx=size.get()
		for i in range(xx):
			valores=tk.Label(frame, text="# "+str(i+1)+": ",bg="#E8DAEF",fg="#4A235A")     
			box=tk.Entry(frame)
			valores.grid(row=i, column=0)
			box.grid(row=i,column=1)
			

			box_list.append(box)    # Append current Entry to list


	x1=[]
	pm3=[]
	pm4=[]
	def calculoPM():
		
		numelem=size.get()  
		matriz = {}
		matriz.update({'x' : lista})
		a = pd.DataFrame(matriz)
		x = a["x"]
		movil = pd.DataFrame(matriz)
		for i in range(0,movil.shape[0]-2):
				movil.loc[movil.index[i+2],'MMO_3'] = np.round(((movil.iloc[i,0]+movil.iloc[i+1,0]+movil.iloc[i+2,0])/3),0)

		for i in range(0,movil.shape[0]-3):
				movil.loc[movil.index[i+3],'MMO_4'] = np.round(((movil.iloc[i,0]+movil.iloc[i+1,0]+movil.iloc[i+2,0]+movil.iloc[i+3,0])/4),0)

		k=numelem-3    

		proyeccion = movil.iloc[k:,[0,1,2]]
		p1,p2,p3=proyeccion.mean()
		
		a = movil.append({'x':p1,'MMO_3':p2, 'MMO_4':p3},ignore_index=True)
		a['e_MM3'] = a['x']-a['MMO_3']
		a['e_MM4'] = a['x']-a['MMO_4']

		mmo3=a['MMO_3']
		mmo4=a['MMO_4']

		for i in x:
			x1.append(i)
		for i in mmo3:
			pm3.append(i)
		for i in mmo4:
			pm4.append(i)	
		

		root = tk.Toplevel()
		root.title("Tabla y gráfico del Método del Promedio Móvil")
		root.configure(bg="#E8DAEF")
		frame=tk.Frame(root, height=400,width=560,bg="#E8DAEF")
		frame.pack(side=tk.LEFT)
		table = tk.Text(frame)
		table.insert(tk.INSERT, a.to_string())
		table.place( x=10, y=10, height=390, width=540)

		frame2=tk.Frame(root,bg="#E8DAEF")
		frame2.pack(side=tk.RIGHT)


		#------------------------------CREAR GRAFICA---------------------------------
		fig = Figure(figsize=(5, 4), dpi=100)
		yyy=np.arange(0,numelem)
		yyyy=np.arange(0,numelem+1)
		fig.add_subplot(111).plot(yyy,x1,label='x',marker='o')#AÑADIR "subbplot"
		fig.add_subplot(111).plot(yyyy,pm3,label='3 años',marker='o')#AÑADIR "subbplot"
		fig.add_subplot(111).plot(yyyy,pm4,label='4 años',marker='o')#AÑADIR "subbplot"
		fig.add_subplot(111).legend(loc=2)

		canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
		toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		# -----------------------------BOTÓN "cerrar"----------------------------------

		root.mainloop()

	Array = tk.Frame(win)
	Array.configure(bg="#E8DAEF")
	Array.pack()

	#ltitulo=tk.Label(Array, text="Variables a ingresar", width=20, height=2,bg="#F4ECF7")
	#ltitulovacio=tk.Label(Array, width=20, height=2)
	lvacio=tk.Label(Array, width=25, height=1,bg="#E8DAEF")

	#ltitulo.grid(row=0,column=0)
	#ltitulovacio.grid(row=1,column=2)
	lvacio.grid(row=4,column=2)

	text1=tk.Label(Array,text="Cantidad de la muestra:",width=20, height=2,bg="#E8DAEF",font="Arial 10 bold",fg="#4A235A")#font="Arial 10 bold",fg="blue")
	text1.grid(row=1,column=0,sticky="w")

	size=tk.IntVar()

	ArraySize=tk.Entry(Array,textvariable=size,width=20)
	ArraySize.grid(row=1,column=1)

	bnuevocalculo=tk.Button(Array,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),PromedioMovil()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
	bnuevocalculo.grid(row=1,column=2)

	SizeofArray=tk.Button(Array,text="Generar muestra",width=17, height=1,command=lambda:[enableboton1(),Boxes()],font="Arial 10 bold",bg="#884EA0", activebackground="#AF7AC5",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	SizeofArray.grid(row=3,column=0)

	ApplytoLabel1=tk.Button(Array,text="Guardar valores",width=17, height=1,command=lambda:[enableboton2(),ApplytoLabel()],font="Arial 10 bold", state=tk.DISABLED,bg="#884EA0", activebackground="#AF7AC5",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	ApplytoLabel1.grid(row=3,column=1)

	calclulo=tk.Button(Array,text="Calcular",width=17, height=1,command=lambda:[enableboton2(),calculoPM()],font="Arial 10 bold", state=tk.DISABLED,bg="#884EA0", activebackground="#AF7AC5",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	calclulo.grid(row=3,column=2)

	win.mainloop()

#------------------------------------------------------------------------------------------------

def AlisamientoExponencial():

	win=tk.Toplevel()
	win.title("Método de Alisamiento Eponencial")
	win.configure(bg="#E8DAEF")

	def enableboton1():
		if(SizeofArray['state']==tk.NORMAL):
			SizeofArray['state'] = tk.DISABLED
			ApplytoLabel1['state']= tk.NORMAL


	def enableboton2():
		if(ApplytoLabel1['state']== tk.NORMAL):
			calclulo['state'] = tk.NORMAL
			ApplytoLabel1['state']=tk.DISABLED

		elif(calclulo['state'] == tk.NORMAL):
			calclulo['state'] = tk.DISABLED	

	lista= []
	def ApplytoLabel():
		
	    xx=size.get()
	    for i in range(xx):
	        element = box_list[i].get() # Get value from corresponding Entry
	        #ArrayLabel=tk.Label(win,text=element)
	        lista.append(float(element))  
	        #ArrayLabel.pack()
	
	box_list = []   # Create list of Entrys
	def Boxes():


		def on_configure(event):
			canvas.configure(scrollregion=canvas.bbox('all'))

		canvas = tk.Canvas(win)
		canvas.configure(bg="#E8DAEF")
		canvas.pack(side=tk.LEFT)
		scrollbar = tk.Scrollbar(win, command=canvas.yview)
		scrollbar.pack(side=tk.LEFT, fill='y')
		canvas.configure(yscrollcommand
		 = scrollbar.set,width="170", height="285")
		canvas.bind('<Configure>', on_configure)

		frame = tk.Frame(canvas)
		canvas.create_window((0,0), window=frame, anchor='nw')

		xx=size.get()
		for i in range(xx):        
			valores=tk.Label(frame, text="# "+str(i+1)+": ",bg="#E8DAEF",fg="#4A235A")     
			box=tk.Entry(frame)
			valores.grid(row=i, column=0)
			box.grid(row=i,column=1)
			

			box_list.append(box)    # Append current Entry to list


	sn=[]
	x1=[]
	def calculoAE():
		alfa=float(ealfa1.get())
		matriz = {}
		matriz.update({'x' : lista})
		movil = pd.DataFrame(matriz)

		unoalfa = 1. - alfa
		for i in range(0,movil.shape[0]-1):
		    movil.loc[movil.index[i+1],'SN'] = np.round(movil.iloc[i,0],0)
		for i in range(2,movil.shape[0]):
		    movil.loc[movil.index[i],'SN'] = (np.round(movil.iloc[i-1,0],0)*alfa) + (np.round(movil.iloc[i-1,1],0)*unoalfa)
		i=i+1
		p1=0
		p2=(np.round(movil.iloc[i-1,0],0)*alfa) + (np.round(movil.iloc[i-1,1],0)*unoalfa)
		a = movil.append({'x':p1, 'SN':p2},ignore_index=True)
		a['error'] = a['x']-a['SN']
		print(p2)
		# unoalfa = 1. - alfa
		# for i in range(0,movil.shape[0]-1):
		# 	movil.loc[movil.index[i+1],'SN'] = np.round(movil.iloc[i,0],0)
		# for i in range(2,movil.shape[0]):
		# 	movil.loc[movil.index[i],'SN'] = np.round(movil.iloc[i-1,0],0)*alfa + np.round(movil.iloc[i-1,1],0)*unoalfa
		# i=i+1
		# p1=0
		# p2=np.round(movil.iloc[i-1,0],0)*alfa + np.round(movil.iloc[i-1,1],0)*unoalfa
		# a = movil.append({'x':p1, 'SN':p2},ignore_index=True)
		# a['error'] = a['x']-a['SN']
		Sn=a['SN']
		x=a['x']
		for i in Sn:
			sn.append(i)
		for i in x:
			x1.append(i)
			
		
		root = tk.Toplevel()
		root.title("Tabla y gráfico del Método de Alisamiento Exponencial")
		root.configure(bg="#E8DAEF")
		frame=tk.Frame(root, height=400,width=300,bg="#E8DAEF")
		frame.pack(side=tk.LEFT)
		table = tk.Text(frame)
		table.insert(tk.INSERT, a.to_string())
		table.place( x=10, y=10, height=390, width=280)

		frame2=tk.Frame(root,bg="#E8DAEF")
		frame2.pack(side=tk.RIGHT)

		xx=size.get()
		yyy=np.arange(0,xx+1)
		

		#------------------------------CREAR GRAFICA---------------------------------
		fig = Figure(figsize=(5, 4), dpi=100)

		
		fig.add_subplot(111).plot(yyy,x1,label='x',marker='o')#AÑADIR "subbplot"
		fig.add_subplot(111).plot(yyy,sn,label='Alisamiento',marker='o')#AÑADIR "subbplot"
		fig.add_subplot(111).legend(loc=2)

		canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
		toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		# -----------------------------BOTÓN "cerrar"----------------------------------
		

		root.mainloop()

	Array = tk.Frame(win)
	Array.configure(bg="#E8DAEF")
	Array.pack()

	#ltitulo=tk.Label(Array, text="Variables a ingresar", width=20, height=2,bg="#E8DAEF")
	#ltitulovacio=tk.Label(Array, width=20, height=2)
	lvacio=tk.Label(Array, width=25, height=1,bg="#E8DAEF")

	#ltitulo.grid(row=0,column=0)
	#ltitulovacio.grid(row=1,column=2)
	lvacio.grid(row=4,column=2)

	text2=tk.Label(Array,text="Número de alfa:", width=20, height=2,bg="#E8DAEF",font="Arial 10 bold",fg="#4A235A")#font="Arial 10 bold",fg="blue")
	text2.grid(row=1,column=0,sticky="w")

	text1=tk.Label(Array,text="Cantidad de la muestra:",width=20, height=2,bg="#E8DAEF",font="Arial 10 bold",fg="#4A235A")
	text1.grid(row=2,column=0,sticky="w")

	alfa1=tk.IntVar()
	size=tk.IntVar()

	ealfa1=tk.Entry(Array,textvariable=alfa1)
	ealfa1.grid(row=1,column=1,sticky="w")

	ArraySize=tk.Entry(Array,textvariable=size)
	ArraySize.grid(row=2,column=1,sticky="w")

	bnuevocalculo=tk.Button(Array,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),AlisamientoExponencial()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
	bnuevocalculo.grid(row=1,column=2)

	SizeofArray=tk.Button(Array,text="Generar muestra",width=17, height=1,command=lambda:[Boxes(),enableboton1()],font="Arial 10 bold",bg="#884EA0", activebackground="#AF7AC5",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	SizeofArray.grid(row=3,column=0)

	ApplytoLabel1=tk.Button(Array,text="Guardar valores",width=17, height=1,command=lambda:[enableboton2(),ApplytoLabel()],font="Arial 10 bold", state=tk.DISABLED,bg="#884EA0", activebackground="#AF7AC5",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	ApplytoLabel1.grid(row=3,column=1)

	calclulo=tk.Button(Array,text="Calcular",width=17, height=1,command=lambda:[enableboton2(),calculoAE()],font="Arial 10 bold", state=tk.DISABLED,bg="#884EA0", activebackground="#AF7AC5",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	calclulo.grid(row=3,column=2)

	win.mainloop()

#------------------------------------------------------------------------------------------------

def RegresionLineal():
	
	win=tk.Toplevel()
	win.title("Método de Regresión Lineal")
	win.configure(bg="#D1F2EB")

	def enableboton1():
		if(SizeofArray['state']==tk.NORMAL):
			SizeofArray['state'] = tk.DISABLED
			ApplytoLabel1['state']= tk.NORMAL

		# if(ApplytoLabel1['state']== tk.NORMAL):
		# 	calclulo['state'] = tk.NORMAL
		# 	ApplytoLabel1['state']=tk.DISABLED

		# elif(calclulo['state'] == tk.NORMAL):
		# 	calclulo['state'] = tk.DISABLED

	def enableboton2():
		if(ApplytoLabel1['state']== tk.NORMAL):
			calclulo['state'] = tk.NORMAL
			ApplytoLabel1['state']=tk.DISABLED

		elif(calclulo['state'] == tk.NORMAL):
			calclulo['state'] = tk.DISABLED	

	lista1= []
	lista2= []

	def ApplytoLabel():
		xx=size.get()
		for i in range(xx):
			element1 = box_list1[i].get()
			lista1.append(float(element1))
		print(lista1)
	       
		for i in range(xx):
			element2 = box_list2[i].get()
			lista2.append(float(element2)) 
		print(lista2)

	   
	
	box_list1 = []  
	box_list2 = []

	def Boxes1():

		def on_configure(event):
			canvas.configure(scrollregion=canvas.bbox('all'))

		canvas = tk.Canvas(win)
		canvas.configure(bg="#D1F2EB")
		canvas.pack(side=tk.LEFT)
		scrollbar = tk.Scrollbar(win, command=canvas.yview)
		scrollbar.pack(side=tk.LEFT, fill='y')
		canvas.configure(yscrollcommand
		 = scrollbar.set,width="170", height="285")
		canvas.bind('<Configure>', on_configure)

		frame = tk.Frame(canvas)
		frame.configure(bg="#D1F2EB")
		canvas.create_window((0,0), window=frame, anchor='nw')

		lavaloresx=tk.Label(frame, text="Valores de X",bg="#D1F2EB",font="Arial 10 bold",fg="#0B5345")
		lavaloresx.grid(row=0,column=1)	

		xx=size.get()
		for i in range(xx):
			valores=tk.Label(frame, text="# "+str(i+1)+": ",bg="#D1F2EB",fg="#0B5345")     
			box1=tk.Entry(frame)
			valores.grid(row=i+1, column=0)
			box1.grid(row=i+1,column=1)
			box_list1.append(box1)

	def Boxes2():

		# def enableboton2():
		# 	if(ApplytoLabel1['state']== tk.NORMAL):
		# 		calclulo['state'] = tk.NORMAL
		# 		ApplytoLabel1['state']=tk.DISABLED
		# 	elif(calclulo['state']== tk.NORMAL):
		# 		calclulo['state']= tk.DISABLED

		def on_configure(event):
			canvas.configure(scrollregion=canvas.bbox('all'))

		canvas = tk.Canvas(win)
		canvas.configure(bg="#D1F2EB")
		canvas.pack(side=tk.LEFT)
		scrollbar = tk.Scrollbar(win, command=canvas.yview)
		scrollbar.pack(side=tk.LEFT, fill='y')
		canvas.configure(yscrollcommand
		 = scrollbar.set,width="170", height="285")
		canvas.bind('<Configure>', on_configure)

		frame = tk.Frame(canvas)
		frame.configure(bg="#D1F2EB")
		canvas.create_window((0,0), window=frame, anchor='nw')

		#-----------------------------------------------------
		lavaloresy=tk.Label(frame, text="Valores de Y",bg="#D1F2EB",font="Arial 10 bold",fg="#0B5345")
		lavaloresy.grid(row=0,column=1)

		xx=size.get()
		for i in range(xx):
			valores=tk.Label(frame,text="# "+str(i+1)+": ",bg="#D1F2EB",fg="#0B5345")     
			box2=tk.Entry(frame)
			valores.grid(row=i+1, column=0)
			box2.grid(row=i+1,column=1)
			box_list2.append(box2)

		
	y_ajuste=[]
	def calculoRL():
			
		predi=prediccion.get()
		
		x=lista1
		y=lista2
		x2=[]
		xy= np.multiply(x,y)
		y2=[]

		for i in x:
		    xcuadrado = (i**2)
		    x2.append(xcuadrado)
			    
		for i in y:
		    ycuadrado = (i**2)
		    y2.append(ycuadrado)

		sumax=sum(x)
		sumay=sum(y)
		sumax2=sum(x2)
		sumaxy=sum(xy)
		sumay2=sum(y2)

		df=pd.DataFrame({'X':x,'Y':y,'X^2':x2,'XY':xy,'Y^2':y2})
		df.loc[7]=[sumax,sumay,sumax2,sumaxy,sumay2]

		p = np.polyfit(x,y,1) 
		p0,p1 = p

		for i in x:
			y_a = p0*i + p1
			y_ajuste.append(round(y_a,2))
		print(y_ajuste)
		print(x)

		pronostico=p1+(p0*predi)

		lecuacion = "Ecuación Y = "+str(round(p1,2))+"+"+str(round(p0,2))+"(X) \n" 
		lpredi="Ecuación Y = "+ str(round(p1,2)) +"+"+str(round(p0,2))+"("+str(round(predi,2))+")"+"="+str(round(pronostico,2))

	
		root = tk.Toplevel()
		root.title("Tabla y gráfico del Método de Regresión lineal")
		root.configure(bg="#D1F2EB")
		frame=tk.Frame(root, height=350,width=420,bg="#D1F2EB")
		frame.pack(side=tk.LEFT)
		table = tk.Text(frame)

		table.insert(tk.INSERT, df.to_string())
		table.place( x=10, y=10, height=250, width=400)

		frame2=tk.Frame(root,bg="#D1F2EB")
		frame2.pack(side=tk.RIGHT)

		respuesta = tk.Text(frame)
		respuesta.insert(tk.INSERT, lecuacion)
		respuesta.insert(tk.INSERT, lpredi)
		respuesta.place( x=10, y=280, height=70, width=400)

		x=lista1
		y=lista2

		#------------------------------CREAR GRAFICA---------------------------------
		fig = Figure(figsize=(5, 4), dpi=100)
		fig.add_subplot(111).plot(x, y,"o")#AÑADIR "subbplot"
		fig.add_subplot(111).plot(x,y_ajuste)
		canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
		toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		root.mainloop()

	Array = tk.Frame(win)
	Array.configure(bg="#D1F2EB")
	Array.pack()

	#ltitulo=tk.Label(Array, text="Variables a ingresar", width=20, height=2)
	#ltitulovacio=tk.Label(Array, width=20, height=2)
	lvacio=tk.Label(Array, width=25, height=1,bg="#D1F2EB")

	#ltitulo.grid(row=0,column=0)
	#ltitulovacio.grid(row=1,column=2)
	lvacio.grid(row=4,column=2)

	text2=tk.Label(Array,text="Predicción:",width=20, height=2,bg="#D1F2EB",font="Arial 10 bold",fg="#0B5345")
	text2.grid(row=1,column=0,sticky="w")

	text1=tk.Label(Array,text="Cantidad de la muestra:",width=20, height=2,bg="#D1F2EB",font="Arial 10 bold",fg="#0B5345")
	text1.grid(row=2,column=0,sticky="w")

	size=tk.IntVar()
	prediccion=tk.IntVar()

	eprediccion=tk.Entry(Array,textvariable=prediccion)
	eprediccion.grid(row=1,column=1,sticky="w")

	ArraySize=tk.Entry(Array,textvariable=size)
	ArraySize.grid(row=2,column=1,sticky="w")

	bnuevocalculo=tk.Button(Array,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),RegresionLineal()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
	bnuevocalculo.grid(row=1,column=2)

	SizeofArray=tk.Button(Array,text="Generar muestra",width=17, height=1,command=lambda:[Boxes1(),Boxes2(),enableboton1()],font="Arial 10 bold",bg="#17A589", activebackground="#48C9B0",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	SizeofArray.grid(row=3,column=0)

	ApplytoLabel1=tk.Button(Array,text="Guardar valores (X,Y)",width=17, height=1,command=lambda:[enableboton2(),ApplytoLabel()],font="Arial 10 bold", state=tk.DISABLED,bg="#17A589", activebackground="#48C9B0",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	ApplytoLabel1.grid(row=3,column=1)

	calclulo=tk.Button(Array,text="Calcular",width=17, height=1,command=lambda:[enableboton2(),calculoRL()],font="Arial 10 bold", state=tk.DISABLED,bg="#17A589", activebackground="#48C9B0",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	calclulo.grid(row=3,column=2)


	win.mainloop()

#------------------------------------------------------------------------------------------------

def RegresionCuadratica():
	
	win=tk.Toplevel()
	win.title("Método de Regresión No Lineal")
	win.configure(bg="#D1F2EB")


	def enableboton1():
		if(SizeofArray['state']==tk.NORMAL):
			SizeofArray['state'] = tk.DISABLED
			ApplytoLabel1['state']= tk.NORMAL


	def enableboton2():
		if(ApplytoLabel1['state']== tk.NORMAL):
			calclulo['state'] = tk.NORMAL
			ApplytoLabel1['state']=tk.DISABLED

		elif(calclulo['state'] == tk.NORMAL):
			calclulo['state'] = tk.DISABLED	



	lista1= []
	lista2= []

	def ApplytoLabel():
		xx=size.get()
		for i in range(xx):
			element1 = box_list1[i].get()
			lista1.append(float(element1))
		print(lista1)
	       
		for i in range(xx):
			element2 = box_list2[i].get()
			lista2.append(float(element2)) 
		print(lista2)

	   
	
	box_list1 = []  
	box_list2 = []

	def Boxes1():
		def on_configure(event):
			canvas.configure(scrollregion=canvas.bbox('all'))

		canvas = tk.Canvas(win)
		canvas.configure(bg="#D1F2EB")
		canvas.pack(side=tk.LEFT)
		scrollbar = tk.Scrollbar(win, command=canvas.yview)
		scrollbar.pack(side=tk.LEFT, fill='y')
		canvas.configure(yscrollcommand
		 = scrollbar.set,width="170", height="285")
		canvas.bind('<Configure>', on_configure)

		frame = tk.Frame(canvas)
		frame.configure(bg="#D1F2EB")
		canvas.create_window((0,0), window=frame, anchor='nw')

		lavaloresx=tk.Label(frame, text="Valores de X",bg="#D1F2EB",font="Arial 10 bold",fg="#0B5345")
		lavaloresx.grid(row=0,column=1)	

		xx=size.get()
		for i in range(xx):
			valores=tk.Label(frame, text="# "+str(i+1)+": ",bg="#D1F2EB",fg="#0B5345")     
			box1=tk.Entry(frame)
			valores.grid(row=i+1, column=0)
			box1.grid(row=i+1,column=1)
			box_list1.append(box1)

  	

	def Boxes2():

		def enableboton2():
			if(ApplytoLabel1['state']== tk.NORMAL):
				calclulo['state'] = tk.NORMAL
				ApplytoLabel1['state']=tk.DISABLED
			elif(calclulo['state']== tk.NORMAL):
				calclulo['state']= tk.DISABLED

		def on_configure(event):
			canvas.configure(scrollregion=canvas.bbox('all'))

		canvas = tk.Canvas(win)
		canvas.configure(bg="#D1F2EB")
		canvas.pack(side=tk.LEFT)
		scrollbar = tk.Scrollbar(win, command=canvas.yview)
		scrollbar.pack(side=tk.LEFT, fill='y')
		canvas.configure(yscrollcommand
		 = scrollbar.set,width="170", height="285")
		canvas.bind('<Configure>', on_configure)

		frame = tk.Frame(canvas)
		frame.configure(bg="#D1F2EB")
		canvas.create_window((0,0), window=frame, anchor='nw')

		#-----------------------------------------------------
		lavaloresy=tk.Label(frame, text="Valores de Y",bg="#D1F2EB",font="Arial 10 bold",fg="#0B5345")
		lavaloresy.grid(row=0,column=1)

		xx=size.get()
		for i in range(xx):
			valores=tk.Label(frame,text="# "+str(i+1)+": ",bg="#D1F2EB",fg="#0B5345")     
			box2=tk.Entry(frame)
			valores.grid(row=i+1, column=0)
			box2.grid(row=i+1,column=1)
			box_list2.append(box2)	





	y_ajuste2=[]

	def calculoRC():
			
		predi=prediccion.get()

		x=lista1
		y=lista2
		x2=[]
		x3=[]
		x4=[]
		xy= np.multiply(x,y)

		for i in x:
		    xcuadrado = (i**2)
		    x2.append(xcuadrado)
		    xcubo = (i**3)
		    x3.append(xcubo)
		    xcuatro = (i**4)
		    x4.append(xcuatro)

		x2y= np.multiply(x2,y)

		sumax1=sum(x)
		sumay=sum(y)
		sumax2=sum(x2)
		sumax3=sum(x3)
		sumax4=sum(x4)
		sumaxy=sum(xy)
		sumax2y=sum(x2y)

		df=pd.DataFrame({'X':x,'Y':y,'X^2':x2,'X^3':x3,'X^4':x4,'XY':xy,'(x^2)y':x2y})
		df.loc[11]=[sumax1,sumay,sumax2,sumax3,sumax4,sumaxy,sumax2y]

		k = np.polyfit(x,y,2)
		k1,k2,k3 = k
		cuadrado=(predi**2)
		pronostico=k3+(k2*predi)+(k1*(cuadrado))

		for i in x:
			y_a = ((k1*i)*i) + (k2*i) + k3
			y_ajuste2.append(round(y_a,2))
		print(y_ajuste2)
		print(x)

		lecuacion="Ecuación Y = "+str(round(k3,2))+"+"+str(round(k2,2))+"(X)"+"+"+str(round(k1,2))+"(X)^2 \n"
		lpredi="Ecuación Y = "+ str(round(k3,2)) +"+"+str(round(k2,2))+"("+str(round(predi,2))+")"+"+"+str(round(k1,2))+"("+str(round(cuadrado,2))+")"+"="+str(round(pronostico,2))
		#messagebox.showinfo(message=lpredi, title="Título")	
		

		root = tk.Toplevel()
		root.title("Tabla y gráfico del Método de Regresión No lineal")
		root.configure(bg="#D1F2EB")
		frame=tk.Frame(root, height=350,width=700,bg="#D1F2EB")
		frame.pack(side=tk.LEFT)
		table = tk.Text(frame)

		table.insert(tk.INSERT, df.to_string())
		table.place( x=10, y=10, height=250, width=680)

		frame2=tk.Frame(root)
		frame2.pack(side=tk.RIGHT)

		respuesta = tk.Text(frame)
		respuesta.insert(tk.INSERT, lecuacion)
		respuesta.insert(tk.INSERT, lpredi)
		respuesta.place( x=10, y=280, height=70, width=680)
	
		x=lista1
		y=lista2

		#------------------------------CREAR GRAFICA---------------------------------
		fig = Figure(figsize=(5, 4), dpi=100)
		fig.add_subplot(111).plot(x, y,"o")#AÑADIR "subbplot"
		fig.add_subplot(111).plot(x,y_ajuste2)
		canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
		toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


		root.mainloop()
		

	Array = tk.Frame(win)
	Array.configure(bg="#D1F2EB")
	Array.pack()

	#ltitulo=tk.Label(Array, text="Variables a ingresar", width=20, height=2,bg="#D1F2EB")
	#ltitulovacio=tk.Label(Array, width=20, height=2)
	lvacio=tk.Label(Array, width=25, height=1,bg="#D1F2EB")

	#ltitulo.grid(row=0,column=0)
	#ltitulovacio.grid(row=1,column=2)
	lvacio.grid(row=4,column=2)

	text2=tk.Label(Array,text="Predicción:",width=20, height=2,bg="#D1F2EB",font="Arial 10 bold",fg="#0B5345")
	text2.grid(row=1,column=0)

	text1=tk.Label(Array,text="Cantidad de la muestra:",width=20, height=2,bg="#D1F2EB",font="Arial 10 bold",fg="#0B5345")
	text1.grid(row=2,column=0)



	size=tk.IntVar()
	prediccion=tk.IntVar()

	eprediccion=tk.Entry(Array,textvariable=prediccion)
	eprediccion.grid(row=1,column=1,sticky="w")

	ArraySize=tk.Entry(Array,textvariable=size)
	ArraySize.grid(row=2,column=1,sticky="w")

	bnuevocalculo=tk.Button(Array,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),RegresionCuadratica()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
	bnuevocalculo.grid(row=1,column=2)

	SizeofArray=tk.Button(Array,text="Generar muestra",width=17, height=1,command=lambda:[Boxes1(),Boxes2(),enableboton1()],font="Arial 10 bold",bg="#17A589", activebackground="#48C9B0",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	SizeofArray.grid(row=3,column=0)

	ApplytoLabel1=tk.Button(Array,text="Guardar valores (X,Y)",width=17, height=1,command=lambda:[enableboton2(),ApplytoLabel()],font="Arial 10 bold", state=tk.DISABLED,bg="#17A589", activebackground="#48C9B0",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	ApplytoLabel1.grid(row=3,column=1)

	calclulo=tk.Button(Array,text="Calcular",width=17, height=1,command=lambda:[enableboton2(),calculoRC()],font="Arial 10 bold", state=tk.DISABLED,bg="#17A589", activebackground="#48C9B0",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	calclulo.grid(row=3,column=2)

	win.mainloop()

#------------------------------------------------------------------------------------------------

def Montecarlo():

	win=tk.Toplevel()
	win.title("Método de Montecarlo")
	win.configure(bg="#FCF3CF")
	#win.geometry('800x600')

	def quitar():
		if(SizeofArray['state']==tk.NORMAL):
			SizeofArray['state']=tk.DISABLED
			ApplytoLabel1['state']= tk.NORMAL


	def enableboton2():
		if(ApplytoLabel1['state']== tk.NORMAL):
			calclulo['state'] = tk.NORMAL
			ApplytoLabel1['state']=tk.DISABLED

		elif(calclulo['state'] == tk.NORMAL):
			calclulo['state'] = tk.DISABLED	


	lista= []
	def ApplytoLabel():
		
		xx=size.get()
		for i in range(xx):
			element = box_list[i].get() # Get value from corresponding Entry
	        #ArrayLabel=tk.Label(win,text=element)
			lista.append(float(element))  
	        #ArrayLabel.pack()
	
	box_list = []   # Create list of Entrys
	def Boxes():
		def enableboton2():
			if(ApplytoLabel1['state']== tk.NORMAL):
				calclulo['state'] = tk.NORMAL
				ApplytoLabel1['state']=tk.DISABLED
			elif(calclulo['state']== tk.NORMAL):
				calclulo['state']= tk.DISABLED

		def on_configure(event):
			canvas.configure(scrollregion=canvas.bbox('all'))

		canvas = tk.Canvas(win)
		canvas.configure(bg="#FCF3CF")
		canvas.pack(side=tk.LEFT)
		scrollbar = tk.Scrollbar(win, command=canvas.yview)
		scrollbar.pack(side=tk.LEFT, fill='y')
		canvas.configure(yscrollcommand
		 = scrollbar.set,width="170", height="285")
		canvas.bind('<Configure>', on_configure)

		frame = tk.Frame(canvas)
		
		canvas.create_window((0,0), window=frame, anchor='nw')	

		xx=size.get()
		for i in range(xx):
			valores=tk.Label(frame, text="# "+str(i+1),bg="#FCF3CF",fg="#784212")     
			box=tk.Entry(frame)
			valores.grid(row=i, column=0)
			box.grid(row=i,column=1)

			box_list.append(box)

	
	yy=[]

	def calculoCA():

		m=int(emodulo.get())
		a=int(eiteraciones.get())
		x0=int(esemilla.get())
		c=int(eincremento.get())
		n1=int(elespera1.get())


		x = [1] * n1
		r = [0.1] * n1
		for i in range(0, n1):
			x[i] = ((a*x0)+c) % m
			x0 = x[i]
			r[i] = x0 / m
		d = {'ri': r}
		dfrac=d["ri"]
		
		for i in dfrac:
			yy.append(i)

		
		f = {'ri': r}
		df = pd.DataFrame(data=f) #tabla ri
		n=len(lista)
		w=range(1,n+1)
		x = {'#':w,'Muestra': lista}
		dfc = pd.DataFrame(data=x)
		
		print(d)

		suma = dfc['Muestra'].sum()
		
		x1 = dfc.assign(Probabilidad=lambda  y:y['Muestra'] / suma)
		a=x1['Probabilidad']
		a1= np.cumsum(a) #Cálculo la suma acumulativa de las probabilidades
		x1['FPA'] =a1

		x1['Min'] = x1['FPA']
		x1['Max'] = x1['FPA']

		lis = x1["Min"].values
		lis2 = x1['Max'].values
		lis[0]= 0
		for i in range(1,n):
			lis[i] = lis2[i-1]
		x1['Min'] = lis

		max = x1 ['Max'].values
		min = x1 ['Min'].values

		def busqueda(arrmin, arrmax, valor):
			 #print(valor)
			for i in range (len(arrmin)):
			 # print(arrmin[i],arrmax[i])
				if valor >= arrmin[i] and valor <= arrmax[i]:
					return i
			return -1
		posi = [0] * n

		xpos = df['ri']
		for j in range(n):
			val = xpos[j]
			pos = busqueda(min,max,val)
			posi[j] = pos


		simula = []
		for j in range(n):
			for i in range(n):
				sim = x1.loc[x1["#"] == posi[i]+1]
				simu = sim.filter(['Muestra']).values
				iterator = itertools.chain(*simu)
				for item in iterator:
					a=item
				simula.append(round(a,2))


		df["SIMULACION"] = pd.DataFrame(simula)
		print(posi)
		# print(x1)

		root = tk.Toplevel()
		root.title("Tabla y gráfico del Método de Montecarlo")
		root.configure(bg="#FCF3CF")
		frame1=tk.Frame(root, height=320,width=580,bg="#FCF3CF")
		frame1.pack(side="left")
		frame2=tk.Frame(root, height=320,width=220,bg="#FCF3CF")
		frame2.pack(side="left")

		table1 = tk.Text(frame1)
		table2 = tk.Text(frame2)
		table1.insert(tk.INSERT, x1.to_string())
		table2.insert(tk.INSERT, df.to_string())
		table1.place( x='10',y='10', height=300, width=560)
		table2.place( x='10',y='10', height=300, width=200)
		root.mainloop()

	Array = tk.Frame(win)
	Array.configure(bg="#FCF3CF")
	Array.pack()

	lmodulo=tk.Label(Array, text="Módulo (m): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")	
	lsemilla=tk.Label(Array, text="Semilla (X0): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
	literaciones=tk.Label(Array, text="Multiplicador (a): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
	lincremento=tk.Label(Array, text="Incremento (c): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
	lespera1=tk.Label(Array, text="Iteraciones (n): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
	text1=tk.Label(Array,text="Cantidad de la muestra:",width=20,height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")


	#ltitulo=tk.Label(Array, text="Variables a ingresar", width=20, height=2)
	#ltitulovacio=tk.Label(Array, width=20, height=2)
	lvacio=tk.Label(Array, width=25, height=1,bg="#FCF3CF")

	#ltitulo.grid(row=0,column=0)
	#ltitulovacio.grid(row=1,column=2)
	lvacio.grid(row=8,column=2)
	

	emodulo=tk.Entry(Array)
	esemilla=tk.Entry(Array)
	eiteraciones=tk.Entry(Array)
	eincremento=tk.Entry(Array)
	elespera1=tk.Entry(Array)


	lmodulo.grid(row=1,column=0)
	lsemilla.grid(row=2,column=0)
	literaciones.grid(row=3,column=0)
	lincremento.grid(row=4,column=0)
	lespera1.grid(row=5,column=0)
	text1.grid(row=6,column=0,sticky="w")
	

	emodulo.grid(row=1,column=1)
	esemilla.grid(row=2,column=1)
	eiteraciones.grid(row=3,column=1)
	eincremento.grid(row=4,column=1)
	elespera1.grid(row=5,column=1)


	size=tk.IntVar()

	ArraySize=tk.Entry(Array,textvariable=size)
	ArraySize.grid(row=6,column=1,sticky="w")

	bnuevocalculo=tk.Button(Array,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),Montecarlo()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
	bnuevocalculo.grid(row=1,column=2)

	SizeofArray=tk.Button(Array,text="Generar muestra",width=17, height=1,command=lambda:[quitar(),Boxes()],font="Arial 10 bold",bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	SizeofArray.grid(row=7,column=0)


	ApplytoLabel1=tk.Button(Array,text="Guardar valores",width=17, height=1,command=lambda:[enableboton2(),ApplytoLabel()],font="Arial 10 bold", state=tk.DISABLED,bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	ApplytoLabel1.grid(row=7,column=1)

	calclulo=tk.Button(Array,text="Calcular",width=17, height=1,command=lambda:[enableboton2(),calculoCA()],font="Arial 10 bold", state=tk.DISABLED,bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
	calclulo.grid(row=7,column=2)


	win.mainloop()

#------------------------------------------------------------------------------------------------

def TransformadaInversa():

	win1=tk.Toplevel()
	win1.title("Transformada Inversa")
	#win.geometry('800x600')
	win1.configure(bg="#FCF3CF")
	
	
	def TransformadaInversageneraladitivo():
		def enablebotons():
			if(bcalcular['state']==tk.NORMAL):
				bcalcular['state']=tk.DISABLED
		win1.withdraw()
		win=tk.Toplevel()
		win.title("Método de la Transformada Inversa")
		win.configure(bg="#FCF3CF")

		yy=[]
		ti = []
		def calculoCA():
			m=int(emodulo.get())
			a=int(eiteraciones.get())
			x0=int(esemilla.get())
			c=int(eincremento.get())
			n1=int(eincre.get())
			inver=float(elanda.get())

			x = [1] * n1 
			r = [0.1] *n1

			for i in range(0, n1):
	    			x[i] = ((a*x0)+c) % m
	    			x0 = x[i]
	    			r[i] = x0 / m
			d = {'ri': r}
			dfrac=d["ri"]
			
			for i in dfrac:
				yy.append(i)
			 #Array donde se guardan los 15 valores generados de la transformada inversa
			for v in yy:
				
				x2=v**math.exp(inver)#Calculo de la transformada inversa
				ti.append(x2)
			f = {'Xn': x, 'ri': r, 'inversa':ti }
			print(ti)
			df = pd.DataFrame(data=f)
		
			root = tk.Toplevel()
			root.title("Tabla y gráfico del Método de Transformada Inversa (MCA)")
			root.configure(bg="#FCF3CF")
			frame=tk.Frame(root, height=400,width=250,bg="#FCF3CF")
			frame.pack(side=tk.LEFT)
			table = tk.Text(frame)

			table.insert(tk.INSERT, df.to_string())
			table.place( x=10, y=10, height=390, width=230)

			frame2=tk.Frame(root)
			frame2.pack(side=tk.RIGHT)

			x=yy
			y=ti

		
			fx=range(len(y))

			#------------------------------CREAR GRAFICA---------------------------------
			fig = Figure(figsize=(5, 4), dpi=100)
			fig.add_subplot(111).plot(fx, x,marker='o')#AÑADIR "subbplot"
			fig.add_subplot(111).plot(fx, y,marker='o')#AÑADIR "subbplot"

			canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
			canvas.draw()
			canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

			#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
			toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
			toolbar.update()
			canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

			#-----------------------------BOTÓN "cerrar"----------------------------------
			

			root.mainloop()

		lmodulo=tk.Label(win, text="Módulo (m): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")	
		lsemilla=tk.Label(win, text="Semilla (X0): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
		literaciones=tk.Label(win, text="Multiplicativo (a): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
		lincremento=tk.Label(win, text="Incremento (c): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
		lincreo=tk.Label(win, text="Iteraciones (n): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
		linversa=tk.Label(win, text="Landa (λ): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")

		#ltitulo=tk.Label(win, text="Variables a ingresar", width=20, height=2)
		#ltitulovacio=tk.Label(win, width=20, height=2)
		lvacio=tk.Label(win, width=25, height=1,bg="#FCF3CF")

		
		emodulo=tk.Entry(win)
		esemilla=tk.Entry(win)
		eiteraciones=tk.Entry(win)
		eincremento=tk.Entry(win)
		eincre=tk.Entry(win)
		elanda=tk.Entry(win)

  
		bcalcular=tk.Button(win, text="Calcular",width=17, height=1, command=lambda:[enablebotons(),calculoCA()],font="Arial 10 bold",bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
		
		bnuevocalculo=tk.Button(win,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),TransformadaInversa()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
		
		#ltitulo.grid(row=0,column=0)
		#ltitulovacio.grid(row=0,column=1)
		lvacio.grid(row=8,column=1)

		lmodulo.grid(row=1,column=0)
		lsemilla.grid(row=2,column=0)
		literaciones.grid(row=3,column=0)
		lincremento.grid(row=4,column=0)
		lincreo.grid(row=5,column=0)
		linversa.grid(row=6,column=0)

		emodulo.grid(row=1,column=1)
		esemilla.grid(row=2,column=1)
		eiteraciones.grid(row=3,column=1)
		eincremento.grid(row=4,column=1)
		eincre.grid(row=5,column=1)
		elanda.grid(row=6,column=1)
		
		bcalcular.grid(row=7,column=1)
		
		bnuevocalculo.grid(row=7,column=0)


	def TransformadaInversageneralmulti():
		win1.withdraw()
		win=tk.Toplevel()
		win.title("Método Congruencial Multiplicativo")
		#win.geometry('800x600')
		win.configure(bg="#FCF3CF")

		def enablebotons():
			if(bcalcular['state']==tk.NORMAL):
				bcalcular['state']=tk.DISABLED
		yy1=[]
		ti1 = []
		def calculoCMul():
			yy=[]
			ti = []
			m=int(emodulo.get())
			a=int(eiteraciones.get())
			x0=int(esemilla.get())
			n1=int(eincre.get())
			inver=float(elanda.get())

			x = [1] * n1
			r = [0.1] * n1
			
			for i in range(0, n1):
	 			x[i] = (a*x0) % m
	 			x0 = x[i]
	 			r[i] = x0 / m
		
			d = {'ri': r}
			dfrac=d["ri"]
			
			for i in dfrac:
				yy1.append(i)
			 #Array donde se guardan los 15 valores generados de la transformada inversa
			for v in yy1:
				
				x2=v**math.exp(inver)#Calculo de la transformada inversa
				ti1.append(x2)
			f = {'Xn': x, 'ri': r, 'inversa':ti1 }
			print(ti)
			df = pd.DataFrame(data=f)

			root = tk.Toplevel()
			root.title("Tabla y gráfico del Método de Transformada Inversa (MCM)")
			root.configure(bg="#FCF3CF")
			frame=tk.Frame(root, height=400,width=250,bg="#FCF3CF")
			frame.pack(side=tk.LEFT)
			table = tk.Text(frame)

			table.insert(tk.INSERT, df.to_string())
			table.place( x=10, y=10, height=390, width=230)

			frame2=tk.Frame(root)
			frame2.pack(side=tk.RIGHT)
			x1=yy1
			y1=ti1
			fx1=range(len(y1))

			#------------------------------CREAR GRAFICA---------------------------------
			fig = Figure(figsize=(5, 4), dpi=100)
			fig.add_subplot(111).plot(fx1, x1,marker='o')#AÑADIR "subbplot"
			fig.add_subplot(111).plot(fx1, y1,marker='o')#AÑADIR "subbplot"

			canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
			canvas.draw()
			canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

			#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
			toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
			toolbar.update()
			canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


			root.mainloop()

		lmodulo=tk.Label(win, text="Módulo (m): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")	
		lsemilla=tk.Label(win, text="Semilla (X0): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
		literaciones=tk.Label(win, text="Multiplicativo (a): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
		lincre=tk.Label(win, text="Iteraciones (n): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
		linversa=tk.Label(win, text="Landa (λ): ", width=20, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")

		#ltitulo=tk.Label(win, text="Variables a ingresar", width=20, height=2)
		#ltitulovacio=tk.Label(win, width=20, height=2)
		lvacio=tk.Label(win, width=25, height=1,bg="#FCF3CF")
		
		emodulo=tk.Entry(win)
		esemilla=tk.Entry(win)
		eiteraciones=tk.Entry(win)
		eincre=tk.Entry(win)
		elanda=tk.Entry(win)

		bcalcular=tk.Button(win, text="Calcular",width=17, height=1, command=lambda:[enablebotons(),calculoCMul()],font="Arial 10 bold",bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",disabledforeground="",cursor="hand2")
		bnuevocalculo=tk.Button(win,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),TransformadaInversa()],font="Arial 10 bold",bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",cursor="hand2")
		
		#ltitulo.grid(row=0,column=0)
		#ltitulovacio.grid(row=0,column=1)
		lvacio.grid(row=8,column=1)

		lmodulo.grid(row=1,column=0)
		lsemilla.grid(row=2,column=0)
		literaciones.grid(row=3,column=0)
		lincre.grid(row=4,column=0)
		linversa.grid(row=5,column=0)

		emodulo.grid(row=1,column=1)
		esemilla.grid(row=2,column=1)
		eiteraciones.grid(row=3,column=1)
		eincre.grid(row=4,column=1)
		elanda.grid(row=5,column=1)
		
		bcalcular.grid(row=6,column=1)
		bnuevocalculo.grid(row=6,column=0)


	Array = tk.Frame(win1)
	Array.configure(bg="#FCF3CF")
	Array.pack()

	texto=tk.Label(Array,text="Selecione el método para ingresar variables aleatorias",width=60, height=2,bg="#FCF3CF",font="Arial 10 bold",fg="#784212")
	#textovacio=tk.Label(Array,width=40, height=1)
	bconAditivo=tk.Button(Array,text="M. Congruencial Aditivo",width=30, height=1,command=TransformadaInversageneraladitivo,font="Arial 10 bold",bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",cursor="hand2")
	bconmultio=tk.Button(Array,text="M. Congruencial Multiplicativo",width=30, height=1,command=TransformadaInversageneralmulti,font="Arial 10 bold",bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",cursor="hand2")

	texto.pack(side='top')
	bconAditivo.pack(side='left',padx=10, pady=10, expand=True,fill='x')
	bconmultio.pack(side='left',padx=10, pady=10, expand=True,fill='x')

	# texto.grid(row=0,column=0)
	# bconAditivo.grid(row=1,column=0)
	# bconmultio.grid(row=2,column=0)
	# textovacio.grid(row=3,column=0)

	win1.mainloop()

#-------------------------------------------------------------------------------------------------

def Linea_espera():

	win1=tk.Toplevel()
	win1.title("Sistema de línea de espera")
	win1.configure(bg="#AEB6BF")
	#win.geometry('800x600')

	lista1=[]
	lista2=[]
	def TransformadaRandom():
		win1.withdraw()
		win=tk.Toplevel()
		win.configure(bg="#AEB6BF")
		win.title("Metodo congruncial aditivo para linea de espera")
		
		def calculoLineaE1():

			landa=float(elespera1.get())
			nu=float(elespera2.get())
			muestra=int(size.get())

			p=landa/nu
			Po = 1.0 - (landa/nu)
			Lq = landa*landa / (nu * (nu - landa))
			L = landa /(nu - landa)
			W = 1 / (nu - landa)
			Wq = W - (1.0 / nu)
			nl=1
			Pn = (landa/nu)*nl*Po

			jhg="Probabilidad ocupación sistema P: "+str(round(p,2))+"\n"+"probabilidad no unidades Po: "+str(round(Po,2))+"\n"+"Longitud de la cola Lq: "+str(round(Lq,2))+"\n"+"Longitud unidades sistema L: "+str(round(L,2))+"\n"+"Tiempo espera medio sistema W: "+str(round(W,2))+"\n"+"Tiempo espera medio en cola Wq: "+str(round(Wq,2))+"\n"+"Probabilidad clientes en cola Pn: "+str(round(Pn,2))+"\n"

			i = 0
			indice = ['ALL','ASE','TILL','TISE','TIRLL','TIISE','TIFSE','TIESP','TIESA']
			Clientes = np.arange(muestra)
			dfLE = pd.DataFrame(index=Clientes, columns=indice).fillna(0.000)

			for i in Clientes:
				if i == 0:
					dfLE['ALL'][i] = lista1[i]
					dfLE['ASE'][i] = lista2[i]
					dfLE['TILL'][i] = -landa*np.log(dfLE['ALL'][i])
					dfLE['TISE'][i] = -nu*np.log(dfLE['ASE'][i])
					dfLE['TIRLL'][i] = dfLE['TILL'][i]
					dfLE['TIISE'][i] = dfLE['TIRLL'][i]
					dfLE['TIFSE'][i] = dfLE['TIISE'][i] + dfLE['TISE'][i]
					dfLE['TIESA'][i] = dfLE['TIESP'][i] + dfLE['TISE'][i]
				else:
					dfLE['ALL'][i] = lista1[i]
					dfLE['ASE'][i] = lista2[i]
					dfLE['TILL'][i] = -landa*np.log(dfLE['ALL'][i])
					dfLE['TISE'][i] = -nu*np.log(dfLE['ASE'][i])
					dfLE['TIRLL'][i] = dfLE['TILL'][i] + dfLE['TIRLL'][i-1]
					dfLE['TIISE'][i] = max(dfLE['TIRLL'][i],dfLE['TIFSE'][i-1])
					dfLE['TIFSE'][i] = dfLE['TIISE'][i] + dfLE['TISE'][i]
					dfLE['TIESP'][i] = dfLE['TIISE'][i] - dfLE['TIRLL'][i]
					dfLE['TIESA'][i] = dfLE['TIESP'][i] + dfLE['TISE'][i]
			nuevas_columnas = pd.core.indexes.base.Index(["A_LLEGADA","A_SERVICIO","TIE_LLEGADA","TIE_SERVICIO","TIE_EXACTO_LLEGADA","TIE_INI_SERVICIO","TIE_FIN_SERVICIO","TIE_ESPERA","TIE_EN_SISTEMA"])
			dfLE.columns = nuevas_columnas
			kl=dfLE["TIE_ESPERA"]
			jl=dfLE["TIE_EN_SISTEMA"]
			ll=dfLE["A_LLEGADA"]
			pl=dfLE["A_SERVICIO"]
			ml=dfLE["TIE_INI_SERVICIO"]
			nl=dfLE["TIE_FIN_SERVICIO"]

			klsuma=sum(kl)
			klpro=(klsuma/muestra)
			jlsuma=sum(jl)
			jlpro=jlsuma/muestra
			dfLE.loc[muestra]=['-','-','-','-','-','-','SUMA',klsuma,jlsuma]
			dfLE.loc[(muestra+1)]=['-','-','-','-','-','-','PROMEDIO',klpro,jlpro]


			root = tk.Toplevel()
			root.title("Tabla y gráfico del Sistema de Línea de Espera (Metodo Congruencial Aditivo)")
			root.configure(bg="#AEB6BF")
			
			frame=tk.Frame(root, height=230,width=1100,bg="#AEB6BF")
			#frame.configure(bg="#AEB6BF")
			frame.pack(side="top")

			table = tk.Text(frame)

			table.insert(tk.INSERT, dfLE.to_string())
			table.place( x=10, y=10, height=210, width=1080)

			frame3=tk.Frame(root,height=400,width=600,bg="#AEB6BF")
			frame3.pack(side="left")
			#frame.configure(bg="#AEB6BF")
			tablita = tk.Text(frame3)
			tablita.insert(tk.INSERT, jhg)
			tablita.place( x=10, y=10, height=380, width=580)


			frame2=tk.Frame(root)
			frame2.pack(side="right")

			iteraciones=float(eiteraciones.get())

			#------------------------------CREAR GRAFICA---------------------------------
			fig = Figure(figsize=(5, 4), dpi=100)
			yyy=np.arange(0,muestra)

			fig.add_subplot(111).plot(yyy,kl,label='T.Espera',marker="o")#AÑADIR "subbplot"
			fig.add_subplot(111).plot(yyy,jl,label='T.Sistema',marker="o")
			fig.add_subplot(111).plot(yyy,ll,label='T.Llegada',marker='o')#AÑADIR "subbplot"
			fig.add_subplot(111).plot(yyy,pl,label='T.Servicio',marker='o')
			fig.add_subplot(111).plot(yyy,ml,label='Ini.Servicio',marker='o')#AÑADIR "subbplot"
			fig.add_subplot(111).plot(yyy,nl,label='Fin.Servicio',marker='o')
			fig.add_subplot(111).legend(loc=2)



			canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
			canvas.draw()
			canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

			# -----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
			toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
			toolbar.update()
			canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
			root.mainloop()

			
		# metodoCA1 = tk.Frame(win)
		# metodoCA1.pack(side="left")
		def enableboton2():
			if(ApplytoLabel1['state']== tk.NORMAL):
				calclulo['state'] = tk.NORMAL
				ApplytoLabel1['state']=tk.DISABLED
			elif(calclulo['state']== tk.NORMAL):
				# calclulo1['state']	= tk.NORMAL
				calclulo['state']= tk.DISABLED
			# elif(calclulo1['state']== tk.NORMAL):
			# 	calclulo1['state']	= tk.DISABLED

		lista1=[]
		def calculoCA1():
			m=int(emodulo.get())
			a=int(eiteraciones.get())
			x0=int(esemilla.get())
			c=int(eincremento.get())
			landa=float(elespera1.get())
			n1=int(size.get())


			x = [1] * n1
			r = [0.1] * n1
			for i in range(0, n1):
				x[i] = ((a*x0)+c) % m
				x0 = x[i]
				r[i] = x0 / m
			d = {'ri': r}
			dfrac=d["ri"]
			
			for i in dfrac:
				lista1.append(i)

		ltitulo=tk.Label(win, text="Generar valores de llegada", width=25, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
		lmodulo=tk.Label(win, text="Módulo (m): ", width=17, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")	
		lsemilla=tk.Label(win, text="Semilla (X0): ", width=17, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
		literaciones=tk.Label(win, text="Multiplicativo (a): ", width=17, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
		lincremento=tk.Label(win, text="Incremento (c): ", width=17, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
		lincre=tk.Label(win, text=" Iteraciones (=) (n) : ", width=17, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
		lespera1=tk.Label(win, text=" Landa (λ): ", width=17, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
		lvacio1=tk.Label(win,width=25, height=1,bg="#AEB6BF")
		
		emodulo=tk.Entry(win)
		esemilla=tk.Entry(win)
		eiteraciones=tk.Entry(win)
		eincremento=tk.Entry(win)
		size=tk.Entry(win)
		elespera1=tk.Entry(win)
		# bcalcular=tk.Button(metodoCA1, text="Ingresar datos de Llegada", command=calculoCA)
		
		ltitulo.grid(row=0,column=1)
		lmodulo.grid(row=1,column=0)
		lsemilla.grid(row=2,column=0)
		literaciones.grid(row=3,column=0)
		lincremento.grid(row=4,column=0)
		lincre.grid(row=5,column=0)
		lespera1.grid(row=6,column=0)
		lvacio1.grid(row=9,column=1)

		emodulo.grid(row=1,column=1)
		esemilla.grid(row=2,column=1)
		eiteraciones.grid(row=3,column=1)
		eincremento.grid(row=4,column=1)
		size.grid(row=5,column=1)
		elespera1.grid(row=6,column=1)

		#-----------------------------------------------

		# metodoCA2 = tk.Frame(win)
		# metodoCA2.pack(side="left")
		lista2=[]
		def calculoCA2():
			m2=int(emodulo2.get())
			a2=int(eiteraciones2.get())
			x02=int(esemilla2.get())
			c2=int(eincremento2.get())
			n12=int(eincre2.get())
			miu2=float(elespera2.get())

			x2 = [1] * n12
			r2 = [0.1] *n12

			for i in range(0, n12):
	    			x2[i] = ((a2*x02)+c2) % m2
	    			x02 = x2[i]
	    			r2[i] = x02 / m2
			d2 = {'ri': r2}
			dfrac2=d2["ri"]
			
			for i in dfrac2:
				lista2.append(i)

		ltitulo2=tk.Label(win, text="Generar valores de Servicio", width=25, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
		# lmodulo2=tk.Label(win, text="Módulo m: ", width=30, height=1,bg="#AEB6BF")	
		# lsemilla2=tk.Label(win, text="Semilla X0: ", width=30, height=1,bg="#AEB6BF")
		# literaciones2=tk.Label(win, text="Multiplicativo a: ", width=30, height=1,bg="#AEB6BF")
		# lincremento2=tk.Label(win, text="Incremento c: ", width=30, height=1,bg="#AEB6BF")
		# lincre2=tk.Label(win, text="Iteraciones n: ", width=30, height=1,bg="#AEB6BF")
		lespera2=tk.Label(win, text="Nu (μ): ", width=25, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
		lvacio2=tk.Label(win,width=25, height=1,bg="#AEB6BF")
		
		emodulo2=tk.Entry(win)
		esemilla2=tk.Entry(win)
		eiteraciones2=tk.Entry(win)
		eincremento2=tk.Entry(win)
		eincre2=tk.Entry(win)
		elespera2=tk.Entry(win)
		# bsalir=tk.Button(metodoCA2,text="Salir", width=15, height=1,command=metodoCA2.destroy)    
		# bcalcular=tk.Button(metodoCA2, text="Ingresar datos de Servicio", command=calculoCA)

		ltitulo2.grid(row=0,column=2)
		# lmodulo2.grid(row=1,column=1)
		# lsemilla2.grid(row=3,column=1)
		# literaciones2.grid(row=5,column=1)
		# lincremento2.grid(row=7,column=1)
		# lincre2.grid(row=9,column=1)
		lespera2.grid(row=7,column=0)
		lvacio2.grid(row=9,column=2)

		emodulo2.grid(row=1,column=2)
		esemilla2.grid(row=2,column=2)
		eiteraciones2.grid(row=3,column=2)
		eincremento2.grid(row=4,column=2)
		eincre2.grid(row=5,column=2)
		elespera2.grid(row=7,column=1)
		
		# bcalcular.grid(row=6,column=1)

		# bsalir.grid(row=7,column=1)

		# botones = tk.Frame(win)
		# botones.pack(side="left")

		ApplytoLabel1=tk.Button(win,text="Generar y guardar aleatorios",width=30, height=1,command=lambda:[enableboton2(),calculoCA2(),calculoCA1()],bg="#2E4053", activebackground="#5D6D7E",fg="White",font="Arial 10 bold", overrelief="flat",cursor="hand2")
		ApplytoLabel1.grid(row=8,column=1)
		calclulo=tk.Button(win,text="Calcular",width=17, height=1,command=lambda:[enableboton2(),calculoLineaE1()],state=tk.DISABLED,bg="#2E4053", activebackground="#5D6D7E",fg="White",font="Arial 10 bold", overrelief="flat",cursor="hand2")
		calclulo.grid(row=8,column=2)
		# calclulo1=tk.Button(botones,text="Graficar",width=17, height=1,command=lambda:[enableboton2(),Grafico()],state=tk.DISABLED)
		# calclulo1.pack()
		bnuevocalculo=tk.Button(win,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),Linea_espera()], bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		bnuevocalculo.grid(row=8,column=0)


		for i in lista1:
			lista1.append(i)
		for i in lista2:
			lista2.append(i)

	def metodoManual():
		win1.withdraw()
		win=tk.Toplevel()
		win.configure(bg="#AEB6BF")
		win.title("Ingreso de datos manuales para Linea de Espera")

		def enablebotons():
			if(SizeofArray['state']==tk.NORMAL):
				SizeofArray['state']=tk.DISABLED
				ApplytoLabel1['state']= tk.NORMAL

		def enableboton2():
			if(ApplytoLabel1['state']== tk.NORMAL):
				calclulo['state'] = tk.NORMAL
				ApplytoLabel1['state']=tk.DISABLED
			elif(calclulo['state']== tk.NORMAL):
				calclulo['state']= tk.DISABLED


		lista1= []
		lista2= []

		def ApplytoLabel():
			xx=size.get()
			for i in range(xx):
				element1 = box_list1[i].get()
				lista1.append(float(element1))
			print(lista1)
		       
			for i in range(xx):
				element2 = box_list2[i].get()
				lista2.append(float(element2)) 
			print(lista2)
		box_list1 = []  
		box_list2 = []

		def Boxes1():
			def on_configure(event):
				canvas.configure(scrollregion=canvas.bbox('all'))

			canvas = tk.Canvas(win)
			canvas.configure(bg="#AEB6BF")
			canvas.pack(side=tk.LEFT)
			scrollbar = tk.Scrollbar(win, command=canvas.yview)
			scrollbar.pack(side=tk.LEFT, fill='y')
			canvas.configure(yscrollcommand
			 = scrollbar.set,width="170", height="285")
			canvas.bind('<Configure>', on_configure)

			frame = tk.Frame(canvas)
			frame.configure(bg="#AEB6BF")
			canvas.create_window((0,0), window=frame, anchor='nw')

			lavaloresx=tk.Label(frame, text="T. LLegada",bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
			lavaloresx.grid(row=0,column=1)	

			xx=size.get()
			for i in range(xx):
				valores=tk.Label(frame, text="# "+str(i+1)+": ",bg="#AEB6BF",fg="#1B2631")     
				box1=tk.Entry(frame)
				valores.grid(row=i+1, column=0)
				box1.grid(row=i+1,column=1)
				box_list1.append(box1)    
		

		def Boxes2():


			def on_configure(event):
				canvas.configure(scrollregion=canvas.bbox('all'))

			canvas = tk.Canvas(win)
			canvas.pack(side=tk.LEFT)
			canvas.configure(bg="#AEB6BF")
			scrollbar = tk.Scrollbar(win, command=canvas.yview)
			scrollbar.pack(side=tk.LEFT, fill='y')
			canvas.configure(yscrollcommand
			 = scrollbar.set,width="170", height="285")
			canvas.bind('<Configure>', on_configure)

			frame = tk.Frame(canvas)
			frame.configure(bg="#AEB6BF")
			canvas.create_window((0,0), window=frame, anchor='nw')

			#-----------------------------------------------------
			lavaloresy=tk.Label(frame, text="T. Servicio",bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
			lavaloresy.grid(row=0,column=1)

			xx=size.get()
			for i in range(xx):
				valores=tk.Label(frame,text="# "+str(i+1)+": ",bg="#AEB6BF",fg="#1B2631")  
				valores.configure(bg="#AEB6BF")   
				box2=tk.Entry(frame)
				valores.grid(row=i+1, column=0)
				box2.grid(row=i+1,column=1)
				box_list2.append(box2)

			# ApplytoLabel1=tk.Button(win,text="Guardar valores (X,Y)",width=17, height=1,command=lambda:[enableboton2(),ApplytoLabel()])
			# ApplytoLabel1.pack()
			# calclulo=tk.Button(win,text="Calcular",width=17, height=1,command=lambda:[enableboton2(),calculoLineaE()],state=tk.DISABLED)
			# calclulo.pack()
			# bnuevocalculo=tk.Button(win,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),metodoManual()])
			# bnuevocalculo.pack()


		Array = tk.Frame(win)
		Array.configure(bg="#AEB6BF")
		Array.pack()

		text1=tk.Label(Array,text="Cantidad de la muestra:",height=2,width=20,
		               font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
		text1.grid(row=2,column=0)

		text2=tk.Label(Array,text="Landa (λ):",height=2,width=20,
		               font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
		text2.grid(row=0,column=0)

		text3=tk.Label(Array,text="Nu (μ):",height=2,width=20,
		               font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
		text3.grid(row=1,column=0)

		lvacio=tk.Label(Array,fg="#1B2631",height=1,width=25,bg="#AEB6BF")
		lvacio.grid(row=5,column=2)

		size=tk.IntVar()
		lespera1=tk.IntVar()
		lespera2=tk.IntVar()


		elespera1=tk.Entry(Array,textvariable=lespera1)
		elespera1.grid(row=0,column=1)

		elespera2=tk.Entry(Array,textvariable=lespera2)
		elespera2.grid(row=1,column=1)

		ArraySize=tk.Entry(Array,textvariable=size)
		ArraySize.grid(row=2,column=1)

		SizeofArray=tk.Button(Array,text="Generar muestra",command=lambda:[enablebotons(),Boxes1(), Boxes2()],bg="#2E4053", activebackground="#5D6D7E",fg="White",font="Arial 10 bold", overrelief="flat",cursor="hand2")
		SizeofArray.grid(row=4,column=0)


		ApplytoLabel1=tk.Button(Array,text="Guardar (Lle.,Ser.)",width=17, height=1,command=lambda:[enableboton2(),ApplytoLabel()],state=tk.DISABLED,bg="#2E4053", activebackground="#5D6D7E",fg="White",font="Arial 10 bold", overrelief="flat",cursor="hand2")
		ApplytoLabel1.grid(row=4,column=1)
		calclulo=tk.Button(Array,text="Calcular",width=17, height=1,command=lambda:[enableboton2(),calculoLineaE()],state=tk.DISABLED,bg="#2E4053", activebackground="#5D6D7E",fg="White",font="Arial 10 bold", overrelief="flat",cursor="hand2")
		calclulo.grid(row=4,column=2)
		bnuevocalculo=tk.Button(Array,text="Nuevo cálculo",width=17, height=1,command=lambda:[win.destroy(),Linea_espera()], bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		bnuevocalculo.grid(row=0,column=2)

		def calculoLineaE():

			landa=float(elespera1.get())
			nu=float(elespera2.get())
			muestra=int(size.get())

			p =landa/nu
			Po = 1.0 - (landa/nu)
			Lq = landa*landa / (nu * (nu - landa))
			L = landa /(nu - landa)
			W = 1 / (nu - landa)
			Wq = W - (1.0 / nu)
			nl=1
			Pn = (landa/nu)*nl*Po

			jhg="Probabilidad ocupación sistema P: "+str(round(p,2))+"\n"+"probabilidad no unidades Po: "+str(round(Po,2))+"\n"+"Longitud de la cola Lq: "+str(round(Lq,2))+"\n"+"Longitud unidades sistema L: "+str(round(L,2))+"\n"+"Tiempo espera medio sistema W: "+str(round(W,2))+"\n"+"Tiempo espera medio en cola Wq: "+str(round(Wq,2))+"\n"+"Probabilidad clientes en cola Pn: "+str(round(Pn,2))+"\n"

			i = 0
			indice = ['ALL','ASE','TILL','TISE','TIRLL','TIISE','TIFSE','TIESP','TIESA']
			Clientes = np.arange(muestra)
			dfLE = pd.DataFrame(index=Clientes, columns=indice).fillna(0.000)

			for i in Clientes:
				if i == 0:
					dfLE['ALL'][i] = lista1[i]
					dfLE['ASE'][i] = lista2[i]
					dfLE['TILL'][i] = -landa*np.log(dfLE['ALL'][i])
					dfLE['TISE'][i] = -nu*np.log(dfLE['ASE'][i])
					dfLE['TIRLL'][i] = dfLE['TILL'][i]
					dfLE['TIISE'][i] = dfLE['TIRLL'][i]
					dfLE['TIFSE'][i] = dfLE['TIISE'][i] + dfLE['TISE'][i]
					dfLE['TIESA'][i] = dfLE['TIESP'][i] + dfLE['TISE'][i]
				else:
					dfLE['ALL'][i] = lista1[i]
					dfLE['ASE'][i] = lista2[i]
					dfLE['TILL'][i] = -landa*np.log(dfLE['ALL'][i])
					dfLE['TISE'][i] = -nu*np.log(dfLE['ASE'][i])
					dfLE['TIRLL'][i] = dfLE['TILL'][i] + dfLE['TIRLL'][i-1]
					dfLE['TIISE'][i] = max(dfLE['TIRLL'][i],dfLE['TIFSE'][i-1])
					dfLE['TIFSE'][i] = dfLE['TIISE'][i] + dfLE['TISE'][i]
					dfLE['TIESP'][i] = dfLE['TIISE'][i] - dfLE['TIRLL'][i]
					dfLE['TIESA'][i] = dfLE['TIESP'][i] + dfLE['TISE'][i]
			nuevas_columnas = pd.core.indexes.base.Index(["A_LLEGADA","A_SERVICIO","TIE_LLEGADA","TIE_SERVICIO","TIE_EXACTO_LLEGADA","TIE_INI_SERVICIO","TIE_FIN_SERVICIO","TIE_ESPERA","TIE_EN_SISTEMA"])
			dfLE.columns = nuevas_columnas
			kl=dfLE["TIE_ESPERA"]
			jl=dfLE["TIE_EN_SISTEMA"]
			ll=dfLE["A_LLEGADA"]
			pl=dfLE["A_SERVICIO"]
			ml=dfLE["TIE_INI_SERVICIO"]
			nl=dfLE["TIE_FIN_SERVICIO"]

			klsuma=sum(kl)
			klpro=(klsuma/muestra)
			jlsuma=sum(jl)
			jlpro=jlsuma/muestra
			dfLE.loc[muestra]=['-','-','-','-','-','-','SUMA',klsuma,jlsuma]
			dfLE.loc[(muestra+1)]=['-','-','-','-','-','-','PROMEDIO',klpro,jlpro]


			root = tk.Toplevel()
			root.title("Tabla y gráfico del Sistema de Línea de Espera (Ingreso Manual)")
			root.configure(bg="#AEB6BF")
			frame=tk.Frame(root, height=230,width=1100,bg="#AEB6BF")
			frame.pack(side="top")

			table = tk.Text(frame)
			table.insert(tk.INSERT, dfLE.to_string())
			table.place( x=10, y=10, height=210, width=1080)

			frame3=tk.Frame(root,height=400,width=600,bg="#AEB6BF")
			frame3.pack(side="left")
			tablita = tk.Text(frame3)
			tablita.insert(tk.INSERT, jhg)
			tablita.place( x=10, y=10, height=380, width=580)

			frame2=tk.Frame(root)
			frame2.pack(side="left")

			#------------------------------CREAR GRAFICA---------------------------------
			fig = Figure(figsize=(5, 4), dpi=100)
			yyy=np.arange(0,muestra)

			fig.add_subplot(111).plot(yyy,kl,label='T.Espera',marker="o")#AÑADIR "subbplot"
			fig.add_subplot(111).plot(yyy,jl,label='T.Sistema',marker="o")
			fig.add_subplot(111).plot(yyy,ll,label='T.Llegada',marker='o')#AÑADIR "subbplot"
			fig.add_subplot(111).plot(yyy,pl,label='T.Servicio',marker='o')
			fig.add_subplot(111).plot(yyy,ml,label='Ini.Servicio',marker='o')#AÑADIR "subbplot"
			fig.add_subplot(111).plot(yyy,nl,label='Fin.Servicio',marker='o')
			fig.add_subplot(111).legend(loc=2)



			canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
			canvas.draw()
			canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

			# -----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
			toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
			toolbar.update()
			canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

			root.mainloop()


	Array = tk.Frame(win1)
	Array.configure(bg="#AEB6BF")
	Array.pack()
		
	texto=tk.Label(Array,text="Selecione el método para ingresar variables aleatorias",width=60, height=2,bg="#AEB6BF",font="Arial 10 bold",fg="#1B2631")
	#textovacio=tk.Label(Array,width=40, height=1,bg="#AEB6BF")
	bconAditivo=tk.Button(Array,text="M. Congruencial Aditivo",command=lambda:[TransformadaRandom()],width=30,bg="#2E4053", activebackground="#5D6D7E",fg="White",font="Arial 10 bold", overrelief="flat",cursor="hand2")
	bconmultio=tk.Button(Array,text="Datos manuales",command=metodoManual,width=30, height=1,bg="#2E4053", activebackground="#5D6D7E",fg="White",font="Arial 10 bold", overrelief="flat",cursor="hand2")

	texto.pack(side='top')
	bconAditivo.pack(side='left',padx=10, pady=10, expand=True,fill='x')
	bconmultio.pack(side='left',padx=10, pady=10, expand=True,fill='x')
	win1.mainloop()


#------------------------------------------------------------------------------------------------

def Inventario():
	
	win=tk.Toplevel()
	win.title("Modelo de Inventario")
	win.configure(bg="#AEB6BF")

	def enablebotons():
		if(bcalcularCM['state']==tk.NORMAL):
			bcalcularCM['state']=tk.DISABLED

	def MetodoInventario():
		D = float(edemanda.get())
		Co = float(ecostordenar.get())
		Ch = float(ecostomantenimiento.get())
		P = float(epedido.get())
		Tespera = float(etiempoespera.get())
		DiasAno = float(ediasano.get())
		n_iteraciones = int(eiteraciones.get())

		# D = 12000.00
		# Co = 25.00
		# Ch = 0.50
		# P = 2.50
		# Tespera = 5
		# DiasAno = 250

		Q = round(sqrt(((2*Co*D)/Ch)),2)
		N = round(D/Q,2)
		R = round((D/DiasAno) * Tespera,2)
		T = round(DiasAno/N,2)
		CoT= N*Co
		ChT= round(Q/2 * Ch,2)
		MOQ = round(CoT + ChT,2)
		CTT=round(P*D+MOQ,2)

		mostrarQ="Cantidad Optima de Pedido Q= "+str(Q)+" \n"
		mostrarCoT="Costo total de Ordenar CoT= " +str(CoT)+" \n"
		mostrarChT="Costo total de Mantener Inventario ChT= " +str(ChT)+" \n"
		mostrarMOQ="Costo Total de Ordenar y Mantener Inventario MoQ= " +str(MOQ)+" \n"
		MostrarCTT="Costo Total del Sistema de Inventario CTT= " +str(CTT)+" \n"
		mostrarN="Número total de pedidos N=" +str(N)+" \n"
		mostrarR="Punto de reorden R="  +str(R)+" \n"
		mostrarT="Tiempo de Pedido T= " +str(T)

		indice = ['Q','Costo_ordenar','Costo_Mantenimiento','Costo_total','Diferencia_Costo_Total']

		periodo = np.arange(1,n_iteraciones)
		def genera_lista(Q):
			n=(n_iteraciones-1)
			Q_Lista = []
			i=1
			Qi = Q
			Q_Lista.append(Qi)
			for i in range(1,9):
				Qi = Qi - 60
				Q_Lista.append(Qi)

			Qi = Q
			for i in range(9, n):
				Qi = Qi + 60
				Q_Lista.append(Qi)

			return Q_Lista
		Lista= genera_lista(Q)
		Lista.sort()
		dfQ = pd.DataFrame(index=periodo, columns=indice).fillna(0)
		dfQ['Q'] = Lista

		for period in periodo:
			dfQ['Costo_ordenar'][period] = D * Co / dfQ['Q'][period]
			dfQ['Costo_Mantenimiento'][period] = dfQ['Q'][period] * Ch / 2
			dfQ['Costo_total'][period] = dfQ['Costo_ordenar'][period] + dfQ['Costo_Mantenimiento'][period]
			dfQ['Diferencia_Costo_Total'][period] = dfQ['Costo_total'][period] - MOQ

		CostoOrdena=dfQ['Costo_ordenar']
		CotoMantenimiento=dfQ['Costo_Mantenimiento']
		CostoTotal=dfQ['Costo_total']
		Diferencia=dfQ['Diferencia_Costo_Total']

		root = tk.Toplevel()
		root.title("Tabla y gráfico del Modelo de inventario Costos")
		root.configure(bg="#AEB6BF")
		
		frame=tk.Frame(root, height=440,width=700,bg="#AEB6BF")
		#frame.configure(bg="#AEB6BF")
		frame.pack(side="left")

		table = tk.Text(frame)

		table.insert(tk.INSERT, dfQ.to_string())
		table.place( x=10, y=10, height=260, width=680)

		respuesta = tk.Text(frame)
		respuesta.insert(tk.INSERT, mostrarQ)
		respuesta.insert(tk.INSERT, mostrarCoT)
		respuesta.insert(tk.INSERT, mostrarChT)
		respuesta.insert(tk.INSERT, mostrarMOQ)
		respuesta.insert(tk.INSERT, MostrarCTT)
		respuesta.insert(tk.INSERT, mostrarN)
		respuesta.insert(tk.INSERT, mostrarR)
		respuesta.insert(tk.INSERT, mostrarT)
		respuesta.place( x=10, y=280, height=140, width=680)

		frame2=tk.Frame(root)
		frame2.pack(side="right")



		#------------------------------CREAR GRAFICA---------------------------------
		fig = Figure(figsize=(5, 4), dpi=100)
		yyy=np.arange(0,(n_iteraciones-1))

		fig.add_subplot(111).plot(yyy,CostoOrdena,label='Costo ordenar',marker="o")#AÑADIR "subbplot"
		fig.add_subplot(111).plot(yyy,CotoMantenimiento,label='Costo Mantenimiento',marker="o")
		fig.add_subplot(111).plot(yyy,CostoTotal,label='Costo total',marker='o')#AÑADIR "subbplot"
		fig.add_subplot(111).plot(yyy,Diferencia,label='DiferenciaCT',marker='o')
		fig.add_subplot(111).legend(loc=2)



		canvas = FigureCanvasTkAgg(fig, master=frame2)  # CREAR AREA DE DIBUJO DE TKINTER.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		# -----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
		toolbar = NavigationToolbar2Tk(canvas, frame2)# barra de iconos
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
		root.mainloop()

	
	ldemanda=tk.Label(win, text="Demanda: ", width=20, height=2,font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
	lcostordenar=tk.Label(win, text="Costo ordenar: ",width=20, height=2,font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
	lcostomantenimiento=tk.Label(win,text="Costo Mantenimiento:", width=20, height=2,font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
	lpedido=tk.Label(win,text="Pedido:", width=20, height=2,font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
	ltiempoespera=tk.Label(win, text="Tiempo espera:",width=20, height=2,font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
	ldiasano=tk.Label(win, text="Dias del año:",width=20, height=2,font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
	literaciones=tk.Label(win, text="Iteraciones:",width=20, height=2,font="Arial 10 bold",bg="#AEB6BF",fg="#1B2631")
	lvacio=tk.Label(win,width=25, height=1,bg="#AEB6BF")

	edemanda=tk.Entry(win)
	ecostordenar=tk.Entry(win)
	ecostomantenimiento=tk.Entry(win)
	epedido=tk.Entry(win)
	etiempoespera=tk.Entry(win)
	ediasano=tk.Entry(win)
	eiteraciones=tk.Entry(win)

	bcalcularCM=tk.Button(win, text="Calcular", width=17, height=1, command=lambda:[enablebotons(),MetodoInventario()],bg="#2E4053", activebackground="#5D6D7E",fg="White",font="Arial 10 bold", overrelief="flat",cursor="hand2")
	bnuevocalculo=tk.Button(win,text="Nuevo cálculo", width=17, height=1,command=lambda:[win.destroy(),Inventario()], bg="#CD6155", activebackground="#E6B0AA",fg="white", overrelief="flat",font="Arial 10 bold",cursor="hand2")

	ldemanda.grid(row=0,column=0)
	lcostordenar.grid(row=1,column=0)
	lcostomantenimiento.grid(row=2,column=0)
	lpedido.grid(row=3,column=0)
	ltiempoespera.grid(row=4,column=0)
	ldiasano.grid(row=5,column=0)
	literaciones.grid(row=6,column=0)
	lvacio.grid(row=8,column=1)

	edemanda.grid(row=0,column=1)
	ecostordenar.grid(row=1,column=1)
	ecostomantenimiento.grid(row=2,column=1)
	epedido.grid(row=3,column=1)
	etiempoespera.grid(row=4,column=1)
	ediasano.grid(row=5,column=1)
	eiteraciones.grid(row=6,column=1)
	
		
	bcalcularCM.grid(row=7,column=1)
	
	bnuevocalculo.grid(row=7,column=0)

	win.mainloop()


#------------------------------------------------------------------------------------------------

def AcercaDe():
	messagebox.showinfo(message="Autor:\nBarreno Robles Kevin \n \nDocente: \nIng. Jorge Moya Delgado \n \nMateria: \nTécnicas de Simulación \n \nCurso: \nOctavo 'A' \n \nVersión 1.0 Beta  \n \nCopyright (c) 2021 ", title="Acerca de la aplicación")

#------------------------------------------------------------------------------------------------

def link_clicked():
	# Aqui va el manual de usuario
	webbrowser.open("https://drive.google.com/file/d/1Uq0kdmFSVwh0Prhng8ZT5sGxs9Gy-_gr/view?usp=sharing")

#------------------------------------------------------------------------------------------------


class MRandoms(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame1=tk.Frame(self,bg="#D4E6F1")
		self.frame1.pack(side="right",padx=0, pady=0, expand=True,fill='both')

		self.greet_button = tk.Button(self.frame1, text="M. Cuadrado Medio" ,command=CuadradoMedio, bg="#2E86C1", activebackground="#5DADE2",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.greet_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')
       
		self.greet_button = tk.Button(self.frame1, text="M. Congruencial Aditivo", command=CongruencialAditivo, bg="#2E86C1", activebackground="#5DADE2",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2" )
		self.greet_button.pack(side='left',padx=20, pady=20,expand=True,fill='x')

		self.greet_button = tk.Button(self.frame1, text="M. Congruencial Multiplicativo", command=CoungrecialMultiplicativo,bg="#2E86C1", activebackground="#5DADE2",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.greet_button.pack(side='left',padx=20, pady=20,expand=True,fill='x')

class MProbabilisticos(ttk.Frame):
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame1=tk.Frame(self,bg="#E8DAEF")
		self.frame1.pack(side="right",padx=0, pady=0, expand=True,fill='both')

		self.web_button = tk.Button(self.frame1, text="Promedio Móvil", command=PromedioMovil,bg="#884EA0", activebackground="#AF7AC5",fg="White", overrelief="flat" ,font="Arial 10 bold",cursor="hand2")
		self.web_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

		self.forum_button = tk.Button(self.frame1, text="Alisamiento Exponencial", command=AlisamientoExponencial,bg="#884EA0", activebackground="#AF7AC5",fg="White", overrelief="flat" ,font="Arial 10 bold",cursor="hand2")
		self.forum_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

class MRegresion(ttk.Frame):
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame1=tk.Frame(self,bg="#D1F2EB")
		self.frame1.pack(side="right",padx=0, pady=0, expand=True,fill='both')

		self.web_button = tk.Button(self.frame1, text="Regresión Lineal", command=RegresionLineal,bg="#17A589", activebackground="#48C9B0",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.web_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

		self.forum_button = tk.Button(self.frame1, text="Regresión No Lineal (Cuadrática)",command=RegresionCuadratica,bg="#17A589", activebackground="#48C9B0",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.forum_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

class MSimulacion(ttk.Frame):
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame1=tk.Frame(self,bg="#FCF3CF")
		self.frame1.pack(side="right",padx=0, pady=0, expand=True,fill='both')

		self.web_button = tk.Button(self.frame1, text="Montecarlo", command=Montecarlo,bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.web_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

		self.forum_button = tk.Button(self.frame1, text="Transformada Inversa",command=TransformadaInversa,bg="#D68910", activebackground="#F5B041",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.forum_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

class MoSimulacion(ttk.Frame):
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame1=tk.Frame(self,bg="#AEB6BF")
		self.frame1.pack(side="right",padx=0, pady=0, expand=True,fill='both')

		self.web_button = tk.Button(self.frame1, text="Linea de espera", command=Linea_espera,bg="#2E4053", activebackground="#5D6D7E",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.web_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

		self.forum_button = tk.Button(self.frame1, text="Modelo de Inventario" ,command=Inventario,bg="#2E4053", activebackground="#5D6D7E",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.forum_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

class Informacion(ttk.Frame):
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame1=tk.Frame(self,bg="#FADBD8")
		self.frame1.pack(side="right",padx=0, pady=0, expand=True,fill='both')

		self.web_button = tk.Button( self.frame1, text="Manual en línea",command=link_clicked,bg="#E74C3C", activebackground="#EC7063",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.web_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

		self.forum_button = tk.Button(self.frame1, text="Acerca de", command=AcercaDe,bg="#E74C3C", activebackground="#EC7063",fg="White", overrelief="flat",font="Arial 10 bold",cursor="hand2")
		self.forum_button.pack(side='left',padx=20, pady=20, expand=True,fill='x')

class Application(ttk.Frame):

	def __init__(self, main_window):
		super().__init__(main_window)
		main_window.title("Aplicación de Técnicas de Simulación")

		def on_tab(event):
			global tab_styles
			global style
			self.notebook = event.widget
			tab = self.notebook.tab(self.notebook.select(), "text")
			st = tab_styles[tab]
			style.map('TNotebook.Tab', **st)


		self.frame0=tk.Frame(self,bg="#FDFEFE")
		self.frame0.pack(padx=0, pady=0, expand=True,fill='both')
		self.notebook = ttk.Notebook(self.frame0)
		self.notebook.pressed_index = None

		self.mrandoms = MRandoms(self.notebook)
		self.notebook.add(self.mrandoms, text="  M. Randoms  ", padding=0)
		tab_styles["  M. Randoms  "] = {"background": [("selected", "#D4E6F1"),("active", "#D7DBDD")],"foreground": [("selected", "#1B4F72")]}

		self.mprobabilisticos = MProbabilisticos(self.notebook)
		self.notebook.add(self.mprobabilisticos, text="  M. Probabilísticos  ", padding=0)
		tab_styles["  M. Probabilísticos  "] = {"background": [("selected", "#E8DAEF"),("active", "#D7DBDD")],"foreground": [("selected", "#4A235A")]}

		self.mregresion = MRegresion(self.notebook)
		self.notebook.add(self.mregresion, text="  M. de Regresión  ", padding=0)
		tab_styles["  M. de Regresión  "] = {"background": [("selected", "#D1F2EB"),("active", "#D7DBDD")],"foreground": [("selected", "#0B5345")]}

		self.msimulacion = MSimulacion(self.notebook)
		self.notebook.add(self.msimulacion, text="  M. de Simulación  ", padding=0)
		tab_styles["  M. de Simulación  "] = {"background": [("selected", "#FCF3CF"),("active", "#D7DBDD")],"foreground": [("selected", "#784212")]}

		self.mosimulacion = MoSimulacion(self.notebook)
		self.notebook.add(self.mosimulacion, text="  Modelos de Simulación  ", padding=0)
		tab_styles["  Modelos de Simulación  "] = {"background": [("selected", "#AEB6BF"),("active", "#D7DBDD")],"foreground": [("selected", "#1B2631")]}

		self.informacion = Informacion(self.notebook)
		self.notebook.add(self.informacion, text="  Información  ", padding=0)
		tab_styles["  Información  "] = {"background": [("selected","#FADBD8"),("active", "#D7DBDD")],"foreground": [("selected", "#78281F")]}


		self.notebook.pack(padx=0, pady=0)

		self.notebook.bind("<<NotebookTabChanged>>", on_tab)

		self.pack()


main_window = tk.Tk()
main_window.configure(bg="#F7F9F9")

style = ttk.Style()

settings = {"TNotebook.Tab": {"configure": {"padding": [15, 8],"font":"arial 10 bold","background":"#F4F6F7"}}}  
style.theme_create("mi_estilo", parent="alt",settings=settings)
style.theme_use("mi_estilo")

tab_styles = {}




app = Application(main_window)
app.mainloop()