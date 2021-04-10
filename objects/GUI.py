import tkinter as tk
import tkinter.ttk as ttk
from time import strftime, gmtime, sleep
from assets.utils.gui_constants import *
from objects.Chatbot import *
import threading as th
from PIL import Image, ImageTk, ImageFont, ImageDraw

class PizzabotInterface(tk.Tk):
    def __init__(self, lang='en'):
        tk.Tk.__init__(self)
        self.title(APP_TITLE)
        self.geometry(APP_GEOMETRY)
        self.iconbitmap(APP_ICON_PATH)
        self.resizable(width=False, height=False)
        self.configure(bg='white')
        self.elements={}
        self.lang=lang
        self.bot=Chatbot(lang)
        self.botThread=th.Thread()
        self.__create_splash_screen()
        

    def __create_splash_screen(self):
        self.elements['output_field']=tk.Label(self, text=SPLASH_OUTPUT_FIELD_TEXT,
                                               bg="white", fg="black", font=SPLASH_OUTPUT_FIELD_FONT, anchor=tk.CENTER)
        self.elements['output_field'].place(x=SPLASH_OUTPUT_FIELD_X, y=SPLASH_OUTPUT_FIELD_Y, height=SPLASH_OUTPUT_FIELD_HEIGHT)
        self.elements['input_field']=tk.Entry(self, width=SPLASH_INPUT_FIELD_WIDTH)
        self.elements['input_field'].place(x=SPLASH_INPUT_FIELD_X, y=SPLASH_INPUT_FIELD_Y, height=SPLASH_INPUT_FIELD_HEIGHT, width=SPLASH_INPUT_FIELD_WIDTH)
        self.elements['send_button']=ttk.Button(self, text=SPLASH_SEND_BUTTON_TEXT, command=self.__get_name)
        self.elements['send_button'].place(x=SPLASH_SEND_BUTTON_X, y=SPLASH_SEND_BUTTON_Y, height=SPLASH_SEND_BUTTON_HEIGHT, width=SPLASH_SEND_BUTTON_WIDTH)
        img=ImageTk.PhotoImage(Image.open(DELIVERY_IMG_PATH))
        img_label=tk.Label(self, image=img)
        img_label.image=img
        img_label.place(x=SPLASH_DELIVERY_IMG_X, y=SPLASH_DELIVERY_IMG_Y)
        

    def __get_name(self):
        if(self.elements['input_field'].get().strip() !=''):
            self.username=self.elements['input_field'].get().strip()
            self.elements['output_field'].destroy()
            self.elements['input_field'].destroy()
            self.elements['send_button'].destroy()
            self.__create_widgets()
            
            
            
    def __create_widgets(self):
        #add output field with its scroll
        self.title(APP_TITLE+" with "+self.username)
        self.elements['output_field']=tk.Text(self, wrap=tk.WORD, state=tk.DISABLED)
        self.elements['scroll'] = tk.Scrollbar(self, orient="vertical", command=self.elements['output_field'].yview)
        self.elements['output_field'].configure(yscrollcommand=self.elements['scroll'].set)
        self.elements['scroll'].place(x=SCROLL_X, y=SCROLL_Y, height=SCROLL_HEIGHT)
        self.elements['output_field'].place(x=OUTPUT_FIELD_X, y=OUTPUT_FIELD_Y, height=OUTPUT_FIELD_HEIGHT, width=OUTPUT_FIELD_WIDTH)

        #add entry field
        self.elements['input_field']=tk.Entry(self, width=INPUT_FIELD_WIDTH, font=INPUT_FIELD_FONT)
        self.elements['input_field'].place(x=INPUT_FIELD_X, y=INPUT_FIELD_Y, height=INPUT_FIELD_HEIGHT, width=INPUT_FIELD_WIDTH)

        #add send button
        img=ImageTk.PhotoImage(Image.open(SEND_BUTTON_IMG_PATH))
        self.elements['send_button']=ttk.Button(self, command=self.add_message_user, image=img)
        self.elements['send_button'].image=img
        self.elements['send_button'].place(x=SEND_BUTTON_X, y=SEND_BUTTON_Y, height=SEND_BUTTON_HEIGHT, width=SEND_BUTTON_WIDTH)
    
    def add_message_user(self):
        if(self.elements['input_field'].get().strip() !=''):
            #contruct message to display
            message = self.username + " @ " +strftime("%H:%M", gmtime()) + " =>  "
            message += self.elements['input_field'].get()
            #update output field with message
            self.elements['output_field'].configure(state=tk.NORMAL)
            self.elements['output_field'].insert(tk.END, '\n\n'+message)
            self.elements['output_field'].configure(state=tk.DISABLED)
            #get bot answer
            self.add_message_bot(self.elements['input_field'].get())#this must be a thread
            #remove what was written in the entry field
            self.elements['input_field'].delete(0,tk.END)

    def add_message_bot(self, received):
        #construct message to display
        message = "PizzaBot @ " +strftime("%H:%M", gmtime()) + " =>  "
        message += self.bot.answer(received)
        #update output field with message
        self.elements['output_field'].configure(state=tk.NORMAL)
        self.elements['output_field'].insert(tk.END, '\n\n'+message)
        self.elements['output_field'].configure(state=tk.DISABLED)

        if("card" in message or "wallet" in message):
            self.__pizza_ready_screen()
            
    def __pizza_ready_screen(self):
        window = tk.Toplevel(self, height=TOP_LEVEL_HEIGHT, width=TOP_LEVEL_WIDTH)
        window.resizable(height=False, width=False)
        window.title(TOP_LEVEL_TITLE)
        window.iconbitmap(APP_ICON_PATH)
        
        font = ImageFont.truetype(PIZZA_IMG_FONT, 34)
        img = Image.open(PIZZA_IMG_PATH)
        draw = ImageDraw.Draw(img)
        draw.text(PIZZA_IMG_TEXT_POS,PIZZA_IMG_TEXT+self.username,PIZZA_IMG_TEXT_COLOR,font=font)
        img=ImageTk.PhotoImage(img)
        label=tk.Label(window, image=img)
        label.image=img
        label.place(x=0, y=0)
    
    def close_app(self):
        self.elements={}
        self.destroy()
