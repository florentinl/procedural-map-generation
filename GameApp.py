from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
Config.set('modules', 'monitor', '')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture
from kivy.core.window import Window

from PixelMap import PixelMap
from MapBuffer import MapBuffer
from Player import Player


FPS = 120

class MapGame(Widget):

    def __init__(self, **kwargs):
        super(MapGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'z':
            self.player.reset_speed('up')
        elif keycode[1] == 's':
            self.player.reset_speed('down')
        elif keycode[1] == 'q':
            self.player.reset_speed('left')
        elif keycode[1] == 'd':
            self.player.reset_speed('right')

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'z':
            self.player.set_speed('up')
        elif keycode[1] == 's':
            self.player.set_speed('down')
        elif keycode[1] == 'q':
            self.player.set_speed('left')
        elif keycode[1] == 'd':
            self.player.set_speed('right')

    def init_game(self):
        self.world = PixelMap(3000, 300)
        self.player = Player(50, 0., 0.)
        self.view = MapBuffer(self.world, self.player.x, self.player.y)
        self.texture = Texture.create(size=(601, 601))

    def update(self, dt):
        self.player.update_position(dt)
        self.refresh_texture() 
        self.canvas.clear()
        with self.canvas:
            Rectangle(texture = self.texture, pos=(0,0), size = (601,601))

    def refresh_texture(self):
        data = self.view.get_view(self.player.y, self.player.x).tobytes()
        self.texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="luminance")


class MapApp(App):
    def build(self):  
        game = MapGame()
        game.init_game()
        Clock.schedule_interval(game.update, 1.0 / FPS)
        return game



MapApp().run()




# default_font = pygame.font.get_default_font()
# font_renderer = pygame.font.Font(default_font, 45)
# displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Procedural map generation")
# FramePerSec = pygame.time.Clock()

# world = PixelMap(3000, 300)
# player = Player(50, 0., 0.)
# view = MapBuffer(world, player.x, player.y)

# displaysurface.fill((255,255,255))
# displaysurface.blit(view.get_surface(player.x, player.y), (0, 0))

# mask = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
# mask.fill((0,0,0, 255))
# pygame.draw.circle(mask, (255,255,255, 0), (WIDTH//2, HEIGHT//2), min(HEIGHT,WIDTH)//2)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#                 running = False

#         if event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_z:
#                 player.set_speed('up')

#             if event.key == pygame.K_s:
#                 player.set_speed('down')

#             if event.key == pygame.K_q:
#                 player.set_speed('left')

#             if event.key == pygame.K_d:
#                 player.set_speed('right')
        
#         if event.type == pygame.KEYUP:
            
#             if event.key == pygame.K_z:
#                 player.reset_speed('up')

#             if event.key == pygame.K_s:
#                 player.reset_speed('down')

#             if event.key == pygame.K_q:
#                 player.reset_speed('left')

#             if event.key == pygame.K_d:
#                 player.reset_speed('right')

#     dT = FramePerSec.tick(FPS)
#     player.update_position(dT/1000)
#     label = font_renderer.render(str(round(FramePerSec.get_fps())), True, (255,255,255))

#     displaysurface.blit(view.get_surface(player.x, player.y), (0, 0))
#     displaysurface.blit(mask, (0,0))
#     displaysurface.blit(label, label.get_rect())
    
#     pygame.display.update()