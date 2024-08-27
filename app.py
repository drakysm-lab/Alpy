import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self, master=None):
        '''The base of the project: Tk main class.

        Vars:
        self.style = config window style -> tk.ttk.Style()
        (a coulpe of pre-initialized values used in other methods)

        Methods:
        (init) self.widgets() = screen objects management -> def(self)
        self.download() = call yt-dlp back-end -> def(self)
        self.options_drawing() = show/hide a dropdown menu -> def(self, *args)

        That's it. =)'''

        # TK SETTINGS
        tk.Tk.__init__(self, master)
        self.style = ttk.Style()
        self.style.theme_use("alt")

        # SUPPORTIVE VARIABLES
        self.download_format = tk.IntVar()
        self.show_options = tk.Button(self, text=">", font="JuliaMono 10", command=lambda: self.options_drawing())
        self.sop_switch = False

        # METHOD INITIALIZATION
        self.widgets()

    # FUNC METHODS
    def download(self):
        '''Match options and run yt-dlp script in back-end.

        Vars:
        (local) format = recives the current state of self.select_mode (tk.Radiobutton) -> int
        self.download_format = bridge from self.select_mode and (local) format; send and get data -> IntVar()'''

        format = self.download_format.get()

        match format:
            case 0:
                print("Downloading audio...")
            case 1:
                print("Downloading video...")
            case _:
                print("Could not fetch the video.")
    
    # GUI METHODS
    def options_drawing(self):
        '''Draw (or undraw) an dropdown menu on screen.
        
        Vars:
        self.sop_switch = func trigger -> bool
        self.show_options = menu button instance -> tk.Button
        self.enter_output = output option title -> tk.Label
        self.output_path = user option for save files -> tk.Entry
        self.browse_path = find for path by browsing filesystem -> tk.Button'''

        # TRIIGER FOR OPTIONS BUTTON
        self.sop_switch = not self.sop_switch
        if self.sop_switch:
            self.show_options['text'] = "V"

            # WIDGETS
            self.enter_output = tk.Label(self, text="Enter the output:", font="JuliaMono 12")
            self.output_path = tk.Entry(self, font="JuliaMono 12", width=24)
            self.browse_path = tk.Button(self, text="browse...", font="JuliaMono 10")

            # DRAW
            base_pos_y = WINDOW_SIZE[1] - int(self.display['height']) + 30
            self.enter_output.place(x=50, y=base_pos_y)
            self.output_path.place(x=50, y=base_pos_y + 35)
            self.browse_path.place(x=300, y=base_pos_y + 32)
        else:
            self.show_options['text'] = ">"
            self.enter_output.destroy()
            self.output_path.destroy()
            self.browse_path.destroy()

    def widgets(self):
        '''Create and draw widgets on the main screen.
        
        Vars:
        self.display = field where thumbnail will appears -> tk.Canvas
        self.insert_field = url entry field -> tk.Entry
        self.select_mode = choose between audio or video donwload -> tk.Radiobutton
        self.go_button = run back-end script -> tk.Button'''

        # WIDGETS
        self.display = tk.Canvas(self, width=480, height=270, background="gray75")
        self.insert_field = tk.Entry(self, font="JuliaMono 14", width=48)
        self.select_mode = (tk.Radiobutton(self, text="Audio", font="JuliaMono 16", width=18, value=0, variable=self.download_format),
                            tk.Radiobutton(self, text="Video", font="JuliaMono 16", width=18, value=1, variable=self.download_format))

        self.go_button = tk.Button(self, text="GO!", font="JuliaMono 16", width=12, command=lambda: self.download())

        # DRAW ON SCREEN
        self.display.place(x=0, y=0)
        self.insert_field.place(x=0, y=self.display['height'])
        self.select_mode[0].place(x=0, y=int(self.display['height']) + (int(self.insert_field['font'].replace("JuliaMono ", "")) + 2) * 2)
        self.select_mode[1].place(x=240, y=int(self.display['height']) + (int(self.insert_field['font'].replace("JuliaMono ", "")) + 2) * 2)
        self.show_options.place(x=0, y=WINDOW_SIZE[1] - int(self.display['height']))
        self.go_button.place(x=300, y=580)

def main():
    '''The lead of the program.

    Consts:
    global WINDOW_SIZE -> (tuple) int

    Vars:
    app = Application class object -> Application()'''

    # GLOBAL VALUES
    global WINDOW_SIZE
    WINDOW_SIZE = (480, 640)

    # SOURCE
    app = Application()

    # WINDOW SETUP
    app.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
    app.resizable(width=False, height=False)
    app.title("yt-dlp Python front-end!")

    # RUNNING...
    app.mainloop()

if __name__ == '__main__':
    main()

