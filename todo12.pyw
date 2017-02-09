import Tkinter as tk
import datetime

class Todo:
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.filename = "2017g2.txt"
		
		#self.buffer1 = tk.Frame(parent, width=5)
		#self.buffer1.pack(side=tk.LEFT, fill=tk.Y)
		
		self.main_frame = tk.Frame(parent, bg="black")
		self.main_frame.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
		
		#self.buffer2 = tk.Frame(parent, width=5)
		#self.buffer2.pack(side=tk.LEFT, fill=tk.Y)
		
		#self.b1 = tk.Button(self.main_frame,text="test", command=lambda:self.button_text(self.b1))
		#self.b1.pack(fill=tk.X)
		
		#self.mf_ = tk.Frame(self.main_frame, height=5)
		#self.mf_.pack(fill=tk.X)
		
		self.mf = tk.Frame(self.main_frame, bg="black")
		self.mf.pack(expand=0, fill=tk.X)
		
		self.mf_1 = tk.Frame(self.main_frame, height=1)
		self.mf_1.pack(fill=tk.X)
		
		self.mf1 = tk.Frame(self.main_frame, bg="black")
		self.mf1.pack(expand=0, fill=tk.X)
		
		self.mf2 = tk.Frame(self.main_frame)
		self.mf2.pack(expand=1, fill=tk.BOTH)
		
		#self.mf_2 = tk.Frame(self.main_frame, height=5)
		#self.mf_2.pack(fill=tk.X)
		
		self.mf_week = tk.Button(self.mf, text="Week", command=lambda:self.button_text(self.mf_week), width=17, pady=5, relief=tk.FLAT, bg="black", fg="white", font="Tahoma 12", anchor=tk.W,padx=9)
		#self.mf_month = tk.Button(self.mf, text="Month", command=lambda:self.button_text(self.mf_month), anchor=tk.W, width=7, relief=tk.FLAT, bg="black", fg="white", font="Tahoma 12")
		#self.mf_year = tk.Button(self.mf, text="Year", command=lambda:self.button_text(self.mf_year))
		#self.mf_buffer = tk.Label(self.mf, width=5)
		self.mf_time = tk.Button(self.mf, text="Time", command=lambda:self.button_text(self.mf_time), width=10, relief=tk.FLAT, bg="black", fg="white", font="Tahoma 12")
		self.mf_hide = tk.Button(self.mf, text="V", command=self.show_hide, width=3, relief=tk.FLAT, bg="black", fg="white", font="Tahoma 12")
		
		self.mf_week.pack(side=tk.LEFT, expand=0, fill=tk.BOTH)
		#self.mf_month.pack(side=tk.LEFT, expand=0, fill=tk.BOTH)
		#self.mf_buffer.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
		#self.mf_year.pack(side=tk.LEFT, expand=1, fill=tk.X)
		self.mf_hide.pack(side=tk.RIGHT, expand=0, fill=tk.BOTH)
		self.mf_time.pack(side=tk.RIGHT, expand=0, fill=tk.BOTH)
		
		
		self.mf1_txt1 = tk.Button(self.mf1, text="[]", command=lambda:self.button_text(self.mf1_txt1), width=3, relief=tk.FLAT, bg="black", fg="white", font="Tahoma 10")
		self.mf1_txt2 = tk.Button(self.mf1, text="Completed", command=lambda:self.button_text(self.mf1_txt2), width=12, relief=tk.FLAT, bg="black", fg="white", font="Tahoma 10")
		self.mf1_edit = tk.Button(self.mf1, text="Edit", command=self.edit, width=5, relief=tk.FLAT, bg="black", fg="white", font="Tahoma 10")
		self.mf1_save = tk.Button(self.mf1, text="Save", command=self.save, width=5, relief=tk.FLAT, bg="black", fg="white", font="Tahoma 10")
		
		self.mf1_txt1.pack(side=tk.LEFT, expand=0, fill=tk.X)
		self.mf1_txt2.pack(side=tk.LEFT, expand=0, fill=tk.X)
		
		self.mf1_save.pack(side=tk.RIGHT, expand=0, fill=tk.X)
		self.mf1_edit.pack(side=tk.RIGHT, expand=0, fill=tk.X)
		
		self.text1 = tk.Text(self.mf2, wrap=tk.WORD, height=15, width=25, font="Tahoma 12")
		self.text1.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
		self.scroll1 = tk.Scrollbar(self.mf2)
		self.scroll1.pack(side=tk.LEFT, expand=0, fill=tk.Y)
		
		self.text1.config(yscrollcommand=self.scroll1.set)
		self.scroll1.config(command=self.text1.yview)
		
		self.load_file()
		self.show_hide()
		self.show_time()
	
	def load_file(self):
		print "loading file"
		try:
			with open(self.filename, "r") as txtr:
				file_txt = txtr.read()
			self.text1.delete(1.0, tk.END)
			self.text1.insert(tk.END, file_txt)
			self.text1.mark_set(tk.INSERT, 1.0)
		except:
			f1 = open(self.filename, "w")
			f1.close()
				
		
		
	
	def button_text(self, button):
		#self.text1.insert(tk.END, button["text"])
		self.text1.insert(tk.INSERT, button["text"])
	
	def show_hide(self):
		if self.mf_hide["text"]=="V":
			self.mf_1.forget()
			self.mf1.forget()
			self.mf_hide.config(text="^")
		elif self.mf_hide["text"]=="^":
			self.mf2.forget()
			self.mf_1.pack(fill=tk.X)
			self.mf1.pack(expand=0, fill=tk.X)
			self.mf2.pack(expand=1, fill=tk.BOTH)
			self.text1.pack()
			self.mf_hide.config(text="V")
	
	def show_time(self):
		months = [
			"Jan", "Feb", "Mar", "Apr", "May", "June",
			"July", "August", "September", "October", "November", "December"
		]
		weekdays = [
			"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
			"Sunday"
		]
		weekday= datetime.datetime.now().weekday()
		month = datetime.datetime.now().month 
		day = datetime.datetime.now().day
		year = datetime.datetime.now().year
		if self.mf_week["text"]=="Week":
			self.mf_week.config(text=weekdays[weekday]+", "+months[month-1]+". "+str(day))
			#self.mf_month.config(text=months[month-1]+". "+str(day))
			#self.mf_year.config(text=str(year)) 
			self.parent.title("Todo "+str(year))
		
		hour = datetime.datetime.now().hour
		am_pm="AM"
		if hour >= 12:
			if hour >12:
				hour-=12
			am_pm="PM"
		minute = datetime.datetime.now().minute
		second = datetime.datetime.now().second
		time_now = "{:01d}:{:02d}:{:02d}".format(hour, minute, second)
		self.mf_time.configure(text=time_now+" "+am_pm)
		time_show = self.parent.after(100, self.show_time)
	
	def edit(self):
		print "editing"
		if self.mf1_edit["text"]=="Edit":
			self.mf1_edit.configure(text="Cancel")
			self.parent.after(1000,lambda:self.mf1_edit.configure(text="Edit"))
		else:
			self.mf1_edit.configure(text="Edit")
			self.show_hide()
			self.load_file()
	
	def save(self):
		print "saving"
		if self.mf1_save["text"]=="Save":
			self.mf1_save.configure(text="Cnfrm")
			self.parent.after(1000,lambda:self.mf1_save.configure(text="save"))
		else:
			file_txt = self.text1.get("1.0",tk.END)
			with open(self.filename, "w") as txtw:
				txtw.write(file_txt)
			self.show_hide()	
			self.load_file()
			self.mf1_save.configure(text="Save")		

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y-45))
			
if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("375x325")
	root.wm_attributes("-topmost", True)
	center(root)
	app = Todo(root)
	root.mainloop()