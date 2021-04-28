import tkinter as tk
from no_gui_gui import TransparentWin
import asyncio
import os
from PIL import ImageTk
dir_path = os.path.dirname(__file__)
loop = asyncio.get_event_loop()

class HintWidget(TransparentWin):
    def __init__(self, loop):
        super().__init__()
        self.pictures = []
        self.buttons = []
        asyncio.ensure_future(self.foo(), loop=loop)
        asyncio.ensure_future(self.independent_refresh_loop(), loop=loop)

    def load_image(self, image):
        l = ImageTk.PhotoImage(file=f".\imgs\{image}")
        self.pictures.append(l)


    def create_buttons(self):
        for photo in self.pictures:
            print(type(photo))
            btn = tk.Button(
                self,
                width=100,
                height=100,
                image=photo
            )
            self.buttons.append(btn)
            print(type(btn))
            btn.pack(side=tk.LEFT)


    async def foo(self):
        while True:
            for x in self.buttons:
                for y in [z for z in self.buttons if x != z]:
                    y.configure(width=50)
                x.configure(width=100)
                await asyncio.sleep(12)


    async def independent_refresh_loop(self):
        while True:
            await asyncio.sleep(0.01)
            self.update()

window = HintWidget(loop)
window.load_image("Spawn_larva.png")
window.load_image("Overlord.png")
window.load_image("Spend_larva.png")
window.load_image("Creep.png")
window.load_image("Check_upgrades.png")
window.create_buttons()
loop.run_forever()