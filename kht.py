import pygame
import time
background = pygame.image.load("Background.png")
jumps = 0
pygame.font.init()
# A blocky, Zenithal-style font (from Grizzy and the Lemmings)
font = pygame.font.Font("Fonts/ZENITHAL.ttf", 52)
# A afterfont (made up word)
afterfont = pygame.font.Font("Fonts/zombiecontrol.ttf", 50)
def gravity(time, start_velocity=0, gravity=9.81):
    return start_velocity + gravity * time

def jump(time, start_velocity=0, gravity=9.81, max_jump_time=0.16):
    if pygame.time.get_ticks() > max_jump_time:
        time = max_jump_time
    return start_velocity - gravity * time

class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.last_time = time.time()

    def tick(self, fps):
        self.clock.tick(fps)
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time
        return delta_time
    def get_fps(self):
        return self.clock.get_fps()
    def get_time(self):
        return self.clock.get_time()
    def get_rawtime(self):
        return self.clock.get_rawtime()
    def get_ticks(self):
        return self.clock.get_ticks()
    def tick_busy_loop(self, fps):
        self.clock.tick_busy_loop(fps)
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time
        return delta_time
if __name__ == "__main__":
    pygame.init()
    clock = Clock()
    screen = pygame.display.set_mode((400, 400))
    # Make the character
    rect = pygame.Rect(20, 20, 50, 50)
    while True:
        t = pygame.time.get_ticks()
        delta_time = clock.tick_busy_loop(60)
        pygame.display.set_caption("KHT: How fast can you hypertap??,  FPS:    %.3f" % clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE:
                    rect.y -= jump(delta_time, start_velocity=200, gravity=200)
                    jumps += 1
        rect.y += gravity(delta_time, start_velocity=0, gravity=200)
        if rect.y >= 200:
            rect.y = 200
        if t >= 5000:
            pygame.quit()
            exit()
        rect.y = max(rect.y, 0)
        rect.y = int(rect.y)
        rect.x = int(rect.x)
        rect.x += 100 * delta_time
        screen.fill((215, 215, 225)) 
        screen.blit(background, (0, 0))
        score = font.render(F"{jumps}", (0, 0, 0), True)
        tt = afterfont.render("%.2f" % (t / 1000), (0, 0, 0), True)
        screen.blit(tt, (56, 100))
        screen.blit(score, (200, 100))
        pygame.draw.rect(screen, (255, 0, 0), rect)
        pygame.display.flip()
        clock.tick_busy_loop(60)
