from flask import g
import pyxel as px
from dataclasses import dataclass

FPS = 60


@dataclass
class Spirit:
    tile_x: int
    tile_y: int
    height: int
    width: int

    x: float
    y: float
    dx: float = 0
    dy: float = 0
    gravity_enabled: bool = True

    strenght: float = 180.0

    def is_under_ground(self, g_level: float, strict: bool):
        return self.y + self.height > g_level if strict else self.y + self.height >= g_level

    def update_position(self):
        self.handle_controls()
        self.apply_velocities()

    def apply_velocities(self):
        self.x += self.dx * 1/FPS
        self.y += self.dy * 1/FPS

    def set_dx(self, value):
        if 0 <= value:
            if value <= self.width/2*FPS:
                self.dx = value
            else:
                self.dx = self.width/2*FPS
        else:
            if value >= - self.width/2*FPS:
                self.dx = value
            else:
                self.dx = - self.width/2*FPS

    def set_dy(self, value):
        if 0 <= value:
            if value <= self.height/2*FPS:
                self.dy = value
            else:
                self.dy = self.height/2*FPS
        else:
            if value >= - self.height/2*FPS:
                self.dy = value
            else:
                self.dy = - self.height/2*FPS

    def handle_controls(self):
        if px.btn(px.KEY_LEFT):
            self.set_dx(self.dx - self.strenght/FPS)
        if px.btn(px.KEY_RIGHT):
            self.set_dx(self.dx + self.strenght/FPS)
        if px.btn(px.KEY_UP):
            self.set_dy(self.dy - self.strenght/FPS*2)

        if px.btnp(px.KEY_KP_PLUS):
            self.strenght += 20
        if px.btnp(px.KEY_KP_MINUS) and self.strenght > 20:
            self.strenght -= 20

    def draw(self):
        # px.blt(self.x, self.y, 0, self.tile_x, self.tile_y, self.width, self.height)
        px.rect(self.x, self.y, self.width, self.height, px.COLOR_PINK)
        px.text(
            5, 5, f"Strenght: {self.strenght}\n Dy: {int(self.dy)}", px.COLOR_WHITE)


class Jeu:
    def __init__(self):
        px.init(160, 120, fps=FPS)

        self.spirits: list[Spirit] = [
            Spirit(0, 0, height=5, width=5, x=50, y=50, dx=0, dy=0)
        ]
        self.mechanics = Mechanics_handeler(self)

        # px.load("PYXEL_RESSOURCE_FILE.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        self.mechanics.handle_gravity()
        self.mechanics.handle_floor_friction()
        self.mechanics.update_spirits_position()

    def draw(self):
        px.cls(0)
        for spirit in self.spirits:
            spirit.draw()


@dataclass
class Mechanics_handeler:
    jeu: Jeu
    GRAVITATIONAL_ACCELERATION = 9.8*20  # m/s^2 * px/m
    FLOOR_STRENGHT_ABSORTION = 3

    def handle_gravity(self):
        for spirit in self.jeu.spirits:
            if spirit.gravity_enabled:
                if spirit.is_under_ground(g_level=px.height, strict=True):
                    spirit.y = px.height - spirit.height
                    spirit.set_dy(-spirit.dy/self.FLOOR_STRENGHT_ABSORTION)
                else:
                    spirit.set_dy(
                        spirit.dy + self.GRAVITATIONAL_ACCELERATION * 1/FPS)

    def handle_floor_friction(self):
        for spirit in self.jeu.spirits:
            if spirit.is_under_ground(g_level=px.height, strict=False):
                spirit.set_dx(
                    spirit.dx*(1 - 1/FPS*self.FLOOR_STRENGHT_ABSORTION))

    def update_spirits_position(self):
        for spirit in self.jeu.spirits:
            spirit.update_position()


Jeu()
