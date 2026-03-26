import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="My Pyxel Game")
        self.x = 72
        self.y = 52
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(40, 4, "Move: Arrow Keys  Quit: Q", 7)
        pyxel.rect(self.x, self.y, 16, 16, 11)


App()
