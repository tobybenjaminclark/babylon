from GameCanvas import *
from tkinter import *
import configparser

def move(master, canvas, object) -> None:
    canvas.move(object, 0.5, 0)
    master.after(1, lambda: move(master, canvas, object))
    

class Window(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Load settings from settings.ini
        self.load_settings()

        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.canvas:GameCanvas
        self.canvas = GameCanvas(self)
        self.canvas.pack()
        
        self.bind("<Escape>", self.quit_fullscreen)
        self.bind(self.fullscreen_key, self.toggle_fullscreen)


        self.update()

        self.canvas.render_map()

        self.x = 100
        self.y = 100
        self.tribe = self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill = "orange")
        
        self.after(1, lambda: move(self, self.canvas, self.tribe))

        self.mainloop()

    


    def load_settings(self) -> None:
        config: configparser.ConfigParser = configparser.ConfigParser()
        config.read('settings.ini') 

        fullscreen_setting = config.getboolean('Window', 'fullscreen', fallback=False)
        self.attributes('-fullscreen', fullscreen_setting)

        # Load control key from settings.ini (default to 'F' if not specified)
        self.fullscreen_key = config.get('Controls', 'fullscreen_key', fallback='<F>')

    def save_settings(self) -> None:
        config: configparser.ConfigParser = configparser.ConfigParser()
        config['Window'] = {'fullscreen': self.attributes('-fullscreen')}
        config['Controls'] = {'fullscreen_key': self.fullscreen_key}
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

    def quit_fullscreen(self, event) -> None:
        self.attributes('-fullscreen', False)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.save_settings()
        self.quit()

    def toggle_fullscreen(self, event) -> None:
        current_state = self.attributes('-fullscreen')
        if not current_state:
            self.attributes('-fullscreen', True)
            self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        else:
            self.attributes('-fullscreen', False)
            self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.save_settings()

if __name__ == "__main__":
    w = Window()