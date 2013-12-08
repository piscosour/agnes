from Tkinter import *

class Interface(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent, background='white')

		self.parent = parent
		self.parent.title("AgNES")
		self.pack(fill=BOTH, expand=1)

		self.centerWindow()
		self.initUI()

	def red_block(self, event):
		if event:
			self.canvas.create_rectangle(78, 100, 178, 200, outline='#f00', fill='#f00')
			self.canvas.create_text(128, 230, fill='#f00', text='CURIOSITY')

	def centerWindow(self):
		w = 1024
		h = 768

		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2

		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def initUI(self):
		self.canvas = Canvas(self, width=1024, height=300)

		self.canvas.create_text(78, 50, fill='#000', anchor='w', text='My name is AgNES. How can I help you?')

		# core indicators

		self.canvas.create_rectangle(78, 100, 178, 200, outline='#090', fill='#090')
		self.canvas.create_text(128, 230, fill='#090', text='CURIOSITY')

		self.canvas.create_rectangle(270, 100, 370, 200, outline='#090', fill='#090')
		self.canvas.create_text(320, 230, fill='#090', text='EMPATHY')

		self.canvas.create_rectangle(462, 100, 562, 200, outline='#090', fill='#090')
		self.canvas.create_text(512, 230, fill='#090', text='NEUROTICISM')

		self.canvas.create_rectangle(654, 100, 754, 200, outline='#090', fill='#090')
		self.canvas.create_text(704, 230, fill='#090', text='SOCIABILITY')

		self.canvas.create_rectangle(846, 100, 946, 200, outline='#090', fill='#090')
		self.canvas.create_text(896, 230, fill='#090', text='DISCIPLINE')

		# command buttons

		storyButton = self.canvas.create_rectangle(212, 300, 312, 350, outline='#03e', fill='#03e')
		storyButtonText = self.canvas.create_text(262, 325, fill='#fff', text='Story')

		tilButton = self.canvas.create_rectangle(462, 300, 562, 350, outline='#03e', fill='#03e')
		tilButtonText = self.canvas.create_text(512, 325, fill='#fff', text='TIL')

		poemButton = self.canvas.create_rectangle(712, 300, 812, 350, outline='#03e', fill='#03e')
		poemButtonText = self.canvas.create_text(762, 325, fill='#fff', text='Poem')

		confessbutton = self.canvas.create_rectangle(212, 400, 312, 450, outline='#03e', fill='#03e')
		confessButtonText = self.canvas.create_text(262, 425, fill='#fff', text='Confess')
		
		yoloButton = self.canvas.create_rectangle(462, 400, 562, 450, outline='#03e', fill='#03e')
		yoloButtonText = self.canvas.create_text(512, 425, fill='#fff', text='YOLO')

		whoisButton = self.canvas.create_rectangle(712, 400, 812, 450, outline='#03e', fill='#03e')
		whoisButtonText = self.canvas.create_text(762, 425, fill='#fff', text='WHOIS')

		openButton = self.canvas.create_rectangle(212, 500, 312, 550, outline='#03e', fill='#03e')
		openButtonText = self.canvas.create_text(262, 525, fill='#fff', text='Open')

		statusButton = self.canvas.create_rectangle(462, 500, 562, 550, outline='#03e', fill='#03e')
		statusButtonText = self.canvas.create_text(512, 525, fill='#fff', text='Status')

		aboutButton = self.canvas.create_rectangle(712, 500, 812, 550, outline='#03e', fill='#03e')
		aboutButtonText = self.canvas.create_text(762, 525, fill='#fff', text='About')

		fourthwallButton = self.canvas.create_rectangle(212, 600, 312, 650, outline='#fff', fill='#fff')
		self.canvas.tag_bind(fourthwallButton, '<ButtonPress-1>', self.clear_canvas)

		byeButton = self.canvas.create_rectangle(462, 600, 562, 650, outline='#03e', fill='#03e')
		byeButtonText = self.canvas.create_text(512, 625, fill='#fff', text='Bye!')
		self.canvas.tag_bind(byeButton, '<ButtonPress-1>', self.shut_down)
		self.canvas.tag_bind(byeButtonText, '<ButtonPress-1>', self.shut_down)

		self.canvas.pack(fill=BOTH, expand=1)


		# byeButton = Button(self, text="Bye!", command=self.quit)
		# byeButton.place(x=900, y=680)

	def clear_canvas(self, event):
		if event:
			self.canvas.get_tk_widget().delete("all")

	def shut_down(self, event):
		self.quit()



if __name__ == '__main__':
	root = Tk()
	agnes_app = Interface(root)
	root.mainloop()

