from pico2d import *
import random as r


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = r.randint(100,700), 90
        self.frame = r.randint(0, 7)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        if self.x > 800: self.x = 0

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5
        if self.x > 800: self.x = 0

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                             self.x, self.y, frame_width // 2, frame_height // 2)

class Ball:
    def __init__(self):
        self.x, self.y = r.randint(50, 750), 599
        self.speed = r.randint(3, 10)
        self.image = load_image('ball21x21.png') if (r.randint(1,100)) % 2 == 0 else load_image('ball41x41.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y - self.image.h > 33:
            self.y -= self.speed
        else : self.y = 33 + self.image.h

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    running = True

    global world
    world = []

    grass = Grass() # Grass 도장을 이용해서 grass 객체 생성
    world.append(grass)

    team = [Boy() for _ in range (11)]
    world += team

    zombie = Zombie()
    world.append(zombie)

    ball = [Ball() for _ in range (20)]
    world += ball

def update_world():
    for game_object in world:
        game_object.update()

def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()


open_canvas()

reset_world()

while running:
    # 이벤트 확인
    handle_events()
    # 게임 로직
    update_world()
    # 렌더링
    render_world()
    delay(0.05)

close_canvas()
