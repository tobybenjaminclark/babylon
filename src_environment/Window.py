from GameCanvas import *
from tkinter import *
import configparser
import random

def move(master, canvas, object):
    canvas.move(object, 0.5, 0)
    master.after(1, lambda: move(master, canvas, object))

def move_tribe(master, canvas, tribe_object, target_x, target_y, speed=1):
    current_x, current_y, _, _ = canvas.coords(tribe_object)

    dx = target_x - current_x
    dy = target_y - current_y

    distance = (dx**2 + dy**2)**0.5

    if distance > speed:
        distance_ratio = speed / distance
        new_x = current_x + dx * distance_ratio
        new_y = current_y + dy * distance_ratio

        canvas.coords(tribe_object, new_x, new_y, new_x + 5, new_y + 5)

        master.after(10, lambda: move_tribe(master, canvas, tribe_object, target_x, target_y, speed))
    else:
        # If distance is less than speed, the tribe has reached the target
        canvas.coords(tribe_object, target_x, target_y, target_x + 10, target_y + 10)

        # Schedule a new random target after a short delay
        master.after(2000, lambda: move_tribe(master, canvas, tribe_object, random.randint(0, canvas.winfo_width() - 10), random.randint(0, canvas.winfo_height() - 10), speed))

class Window(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Load settings from settings.ini
        self.load_settings()

        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.canvas:GameCanvas
        self.canvas = GameCanvas(self)
        self.canvas.pack(side="top", pady = 20)

        # Create the second canvas and pack it to the bottom
        canvas2 = Canvas(self, width = 1200, height = 200, bg='white')
        canvas2.pack(side="top")
        
        self.bind("<Escape>", self.quit_fullscreen)
        self.bind(self.fullscreen_key, self.toggle_fullscreen)


        self.update()

        self.canvas.render_map()

        # Create a list to store tribe objects
        self.tribes = []

        for _ in range(300):
            x = random.randint(0, self.winfo_screenwidth() - 10)
            y = random.randint(0, self.winfo_screenheight() - 10)
            tribe = self.canvas.create_oval(x, y, x + 5, y + 5, fill="aqua", outline = "black", width=2)
            self.tribes.append(tribe)

            # Start the movement of each tribe towards a random location
            random_x = random.randint(0, self.winfo_screenwidth() - 10)
            random_y = random.randint(0, self.winfo_screenheight() - 10)
            move_tribe(self, self.canvas, tribe, random_x, random_y)

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