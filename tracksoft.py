from math import log
from time import sleep
import tkinter 
import tkinter as Tkinter  
from tkinter import Frame,Label, Menubutton
from tkinter.constants import E, N, NW, X
from tkinter.ttk import Notebook
from PIL import ImageTk, Image
from tkinter import OptionMenu, StringVar, font as tkFont
# from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.messagebox import showinfo,showerror
master = tkinter.Tk()
import os,shutil,requests,pyautogui
from datetime import *
import os
import os.path
import random
from datetime import date
# import schedule
counter = 66600
mcounter = 66600
running = False
meeting = False
status=0
master.geometry("390x350")

def login():
	# Connect to database
	username = lblusername.get()
	password = lblpassword.get()
	url="http://localhost/track-soft/api/Authentication/login"
	data={'email':username,'password':password}
	headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	result=requests.post(url,data=data,headers=headers)
	res=result.json()
	def logged(id,c_id):
		master.withdraw()
		def counter_label(label):
			def count():  
				if running:
					global counter  
					# To manage the intial delay.  
					tt = datetime.fromtimestamp(counter) 
					string = tt.strftime("%H:%M:%S") 
					s = tt.strftime("%M") 
					display=string  
			
					label['text']=display    
					label.after(1000, count)   
					counter += 1
					x = random.randint(1,300)
					if x==149:
						def upload(file,fname):
							path=os.getcwd()
							url="http://localhost/track-soft/Screenshot/upload"
							image_metadata={'screenshot',fname}
							data = {'id':id,'cid':c_id}
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
							files = {'file': (fname,open(path+'/'+file+"/"+fname, 'rb'), 'image/png', {'Expires': '0'})}
							
							requests.post(url,files=files,data=data,headers=headers)
						def screenshot(fname):
							name="screenshot"
							now=datetime.now()
							now_str=now.strftime("%d_%m_%Y_%H_%M_%S")
							# process image
							pyautogui.screenshot(fname+"/"+"1_"+name+"_{}.png".format(now_str))
							img1="1_"+name+"_{}.png".format(now_str)
							upload(fname,img1)
						# now=date.today
						# currentmonth=now().month

						# folder="upload"
						# screenshot(folder)
						now= date.today
						# get current month
						currentmonth=now().month
						#make name for current month
						folder="Month_"+str(currentmonth)
						basepath=os.getcwd()
						listdirs=os.listdir(basepath)
						for fname in os.listdir(basepath):
							path = os.path.join(basepath,fname)
							if os.path.isdir(path):
								if fname==folder:
								# call screenshot function
									screenshot(folder)
								else:
									# Delete previous month screenshot
									shutil.rmtree(fname)
									# make folder if not existing in directory
									f=os.mkdir("Month_"+str(currentmonth))
									# call screenshot function
									screenshot(f)
				
			count() 
		def mcount(label):
			def mcounts():
				if meeting:
					global mcounter 
					mcounter +=1
					label.after(1000,mcounts)
					x = random.randint(1,300)
					if x==149:
						def upload(file,fname):
							path=os.getcwd()
							url="http://localhost/track-soft/Screenshot/upload"
							image_metadata={'screenshot',fname}
							data = {'id':id,'cid':c_id}
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
							files = {'file': (fname,open(path+'/'+file+"/"+fname, 'rb'), 'image/png', {'Expires': '0'})}
							
							requests.post(url,files=files,data=data,headers=headers)
						def screenshot(fname):
							name="screenshot"
							now=datetime.now()
							now_str=now.strftime("%d_%m_%Y_%H_%M_%S")
							# process image
							pyautogui.screenshot(fname+"/"+"1_"+name+"_{}.png".format(now_str))
							img1="1_"+name+"_{}.png".format(now_str)
							upload(fname,img1)
						# now=date.today
						# currentmonth=now().month

						# folder="upload"
						# screenshot(folder)
						now= date.today
						# get current month
						currentmonth=now().month
						#make name for current month
						folder="Month_"+str(currentmonth)
						basepath=os.getcwd()
						listdirs=os.listdir(basepath)
						for fname in os.listdir(basepath):
							path = os.path.join(basepath,fname)
							if os.path.isdir(path):
								if fname==folder:
								# call screenshot function
									screenshot(folder)
								else:
									# Delete previous month screenshot
									shutil.rmtree(fname)
									# make folder if not existing in directory
									f=os.mkdir("Month_"+str(currentmonth))
									# call screenshot function
									screenshot(f)
			mcounts()
		def attendance():
			url="http://localhost/track-soft/Screenshot/intime"
			data={'id':id,'cid':c_id}
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			requests.post(url,data=data,headers=headers)
		def tog(label): 
			global running
			global meeting

			global status
			if(toggle['text']=='Start'):
				if(variable.get()=='Office'):
					toggle['text']='Stop'
					if status==0:
						pass
					else:
						url="http://localhost/track-soft/Screenshot/breakouttime"
						data={'id':id,'cid':c_id,'bstatus':status}
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
						requests.post(url,data=data,headers=headers)
						status=0

					running=True
					counter_label(label)
					attendance()
					# start['state']='disabled'
					toggle['state']='normal'
				else:
					if(variable.get()=='Break'):
						showerror(title = "warning", message = "You are in "+variable.get())
						toggle['text']='Start'
						running=False
						meeting=False
					else:
						meeting=True
						toggle['text']='Start'
						running=False
						mcount(label)

			else:
				meeting=True
				toggle['text']='Start'
				toggle['state']='normal'
				# start['state']='disabled'
				running = False
				if(variable.get()=='Meeting'):
					mcount(label)
				
		def uploadtime(times):
			url="http://localhost/track-soft/Screenshot/working"
			data={'id':id,'time':times,'cid':c_id}
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			requests.post(url,data=data,headers=headers)
		def on_closing():
			if messagebox.askokcancel("Quit", "Do you want to quit?"):
				text1=label['text']
				if not text1:
					pass
				else:
					uploadtime(label['text'])
				master.destroy()
				tkWindow.destroy()
		# watch window start here 
		def appraisalData():
			def tasksubmit():
				attend=attdn.get()
				gits=git.get()
				jiras=jira.get()
				overtimes=overtime.get()
				code_reviews=code_review.get()
				error_free_deployments=error_free_deployment.get()
				module_kts=module_kt.get()

				url="http://localhost/track-soft/Screenshot/appraisal"
				data={'id':id,'cid':c_id,'atten':attend,'gits':gits,'jira':jiras,'overtime':overtimes,'code_review':code_reviews,'error_free_d':error_free_deployments,'module_kts':module_kts}
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
				result=requests.post(url,data=data,headers=headers)
				window.destroy()

			window =Tkinter.Tk()
			window.title('My Window')
			window.resizable(False,False)
			window.geometry('300x250+400+300')
			
			
			attdn = Tkinter.IntVar()
			git = Tkinter.IntVar()
			jira = Tkinter.IntVar()
			overtime = Tkinter.IntVar()
			code_review = Tkinter.IntVar()
			error_free_deployment = Tkinter.IntVar()
			module_kt = Tkinter.IntVar()

			c1 = Tkinter.Checkbutton(window, text='Attendance',variable=attdn, onvalue=1, offvalue=0)
			c1.grid(row= 1, sticky='W', padx=90)
			c2 = Tkinter.Checkbutton(window, text='Git',variable=git, onvalue=1, offvalue=0)
			c2.grid(row= 2, sticky='W', padx=90)
			c3 = Tkinter.Checkbutton(window, text='Jira',variable=jira, onvalue=1, offvalue=0)
			c3.grid(row= 3, sticky='W', padx=90)
			c4 = Tkinter.Checkbutton(window, text='Overtime',variable=overtime, onvalue=1, offvalue=0)
			c4.grid(row= 4, sticky='W', padx=90)
			c5 = Tkinter.Checkbutton(window, text='Code Review',variable=code_review, onvalue=1, offvalue=0)
			c5.grid(row= 5, sticky='W', padx=90)
			c6 = Tkinter.Checkbutton(window, text='Error Free Deployment',variable=error_free_deployment, onvalue=1, offvalue=0)
			c6.grid(row= 6, sticky='W', padx=90)
			c7 = Tkinter.Checkbutton(window, text="On Module creation KT's",variable=module_kt, onvalue=1, offvalue=0)
			c7.grid(row= 7, sticky='W', padx=90)
			submit = Tkinter.Button(window, text="Submit", command=lambda:tasksubmit())
			submit.grid(row= 10, sticky='W', padx=125)
			window.mainloop()
		def logout():
			text1=label['text']
			if not text1:
				pass
			else:
				uploadtime(label['text'])
			master.destroy()
			tkWindow.destroy()
			appraisalData()

		tkWindow = Tkinter.Tk()
		tkWindow.geometry('500x350') 

		myFont = tkFont.Font(family='Helvetica', size=13, weight='bold') 
		tkWindow.title('Stopwatch')
		logb=Tkinter.Button(tkWindow,text='Log Out',width=10,command=lambda:logout(),fg="black",activebackground='#867979')
		logb.pack(anchor="ne", padx=5, pady=5)
		label = Tkinter.Label(tkWindow, fg="black", font=("Verdana 30 bold",70))  
		label.pack()
		f = Tkinter.Frame(tkWindow) 
		toggle = Tkinter.Button(f, text='Start', width=5 , command=lambda:tog(label), fg="black",activebackground='#867979')
		toggle['font'] = myFont 
		f.pack(anchor = 'center',pady=5) 
		toggle.pack() 
		my_list = ["Office","Break","Meeting"]
		variable = StringVar(tkWindow)
		variable.set(my_list[0]) #default value
		w=OptionMenu(tkWindow, variable,*my_list)
		w.pack()
		
		def my_show(*args):
			if(variable.get()=="Office"):
				pass
			else:
				text2=label['text']
				if not text2:
					pass
				else:
					global status
					if(variable.get()=="Break"):
						status=1
					else:
						status=2
					url="http://localhost/track-soft/Screenshot/breaktime"
					data={'id':id,'cid':c_id,'bstatus':variable.get()}
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
					requests.post(url,data=data,headers=headers)
					tog(label)

		variable.trace('w',my_show)
		# tkWindow.protocol("WM_DELETE_WINDOW", on_closing)
		tkWindow.mainloop()
		

	if res['status']==True:
		logged(res['data']['id'],res['data']['company_id'])
	else:
		showerror(title = "warning", message = "incorrect username or password")
		


bg_color = "DeepSkyBlue2"
fg_color = "#383a39"
master.configure(background= bg_color)
master.title("Welcome")
#---heading image
photo = ImageTk.PhotoImage(Image.open("logo-dark.png"))
tkinter.Label(master, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
# -------username
tkinter.Label(master,  text="Username:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=8, padx=(50, 0), pady=(20, 10))
lblusername = tkinter.Entry(master)
lblusername.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))

# ----password
tkinter.Label(master,  text="Password:",fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0), pady=(20, 10))
lblpassword = tkinter.Entry(master,show="*")
lblpassword.grid(row=9, column=1, padx=(10, 10),pady=(20, 10))

# --------button
tkinter.Button(master, text="Login",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = login).grid(row = 10,  padx=(50, 0), pady=(20, 10))

master.mainloop()