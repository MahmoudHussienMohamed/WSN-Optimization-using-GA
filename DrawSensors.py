from tkinter import *
class window:
    
    def __init__(self, GA):
        self.iter = 0
        self.gen_n = GA.iterationsNo
        self.areas = GA.coverage
        self.gen = GA.generations
        self.radius = GA.sensors_radius
        self.best_gen = GA.best_gen
        self.root = Tk()
        self.root.title("WSN Simulation")
        self.root.geometry("1080x720+0+0")
        self.ratio = 100 / (1080*720)
        self.cnvs = Canvas(self.root, width=1080, height=720, bg="white")
        self.cnvs.pack()
        self.lbl1 = Label(self.root, text=f"Generation 0")
        self.lbl1.place(x = 0, y = 0)
        self.lbl2 = Label(self.root, text=f"Coverage area = {self.areas[0]} m²\n({self.percentage(0)})")
        self.lbl2.place(x = 0, y = 20)
        self.next_butt = Button(self.root, text = "Next Generation", 
        command = self.next_gen)
        self.next_butt.place(x = 1250, y = 10)
        self.prev_butt = Button(self.root, text = "Prev Generation", 
        command = self.prev_gen)
        self.prev_butt.place(x = 1250, y = 50)
        self.best_gen_butt = Button(self.root, text = "Best Generation", 
        command = self.best_one)
        self.best_gen_butt.place(x = 1250, y = 90)
        self.update()
    
    def percentage(self, area_idx):
        return f'{self.ratio * self.areas[area_idx]:.2f}%'

    def update(self):
        self.cnvs.delete(ALL)
        self.lbl1.config(text=f"Generation {self.iter}")
        self.lbl2.config(text=f"Coverage area = {self.areas[self.iter]} m²\n({self.percentage(self.iter)})")
        self.draw_sensors(self.gen[self.iter], self.radius)

    
    def next_gen(self):
        if self.iter < self.gen_n - 1:
            self.iter += 1
            self.update()

    def prev_gen(self):
        if self.iter > 0:
            self.iter -= 1
            self.update()

    def draw_sensors(self, locations, radius):
        for x, y in locations:
            self.cnvs.create_oval(x-radius, y-radius, x+radius, y+radius)
            self.cnvs.create_oval(x-3, y-3, x+3, y+3, fill = 'red')
        self.cnvs.pack()
    
    def best_one(self):
        self.cnvs.delete(ALL)
        self.lbl1.config(text=f"Best Generation(#{self.best_gen})")
        self.lbl2.config(text=f"Coverage area = {self.areas[self.best_gen]} m²\n({self.percentage(self.best_gen)})")
        self.draw_sensors(self.gen[self.best_gen], self.radius)
        self.iter = self.best_gen
    
    def show(self):
        self.root.mainloop()