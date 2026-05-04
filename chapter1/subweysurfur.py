import random
import sys

try:
    import pygame
except ImportError:
    print("Please install pygame first: python -m pip install pygame")
    sys.exit(1)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS = 60
GROUND_Y = 320
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

WHITE = (255, 255, 255)
SKY = (135, 206, 250)
TRACK = (40, 40, 40)
PLAYER_COLOR = (0, 120, 255)
OBSTACLE_COLOR = (220, 20, 60)
COIN_COLOR = (255, 215, 0)
TEXT_COLOR = (30, 30, 30)
ROAD_COLOR = (50, 50, 50)
LANE_COLOR = (200, 200, 200)
BACKGROUND_COLOR = (90, 170, 90)

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed_x = 5
        self.jump_speed = -14
        self.velocity_y = 0
        self.on_ground = True

    def move(self, dx):
        self.rect.x += dx * self.speed_x
        self.rect.x = max(40, min(self.rect.x, SCREEN_WIDTH - PLAYER_WIDTH - 40))

    def jump(self):
        if self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False

    def update(self):
        self.velocity_y += 0.8
        self.rect.y += self.velocity_y
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.velocity_y = 0
            self.on_ground = True

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect, border_radius=12)

class Obstacle:
    def __init__(self, x, width=30, height=50, speed=6):
        self.rect = pygame.Rect(x, GROUND_Y - height, width, height)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect, border_radius=8)

class Coin:
    def __init__(self, x, y, speed=6):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, COIN_COLOR, self.rect.center, 10)


def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, TEXT_COLOR)
    screen.blit(surface, (x, y))


def show_start_screen(screen):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, ROAD_COLOR, (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y))
    for lane_x in (SCREEN_WIDTH // 3, SCREEN_WIDTH * 2 // 3):
        pygame.draw.line(screen, LANE_COLOR, (lane_x, GROUND_Y), (lane_x, SCREEN_HEIGHT), 4)
    draw_text(screen, "SUBWAY SURFER STYLE RUNNER", 32, 40, 120)
    draw_text(screen, "Use LEFT/RIGHT to move", 28, 140, 190)
    draw_text(screen, "Use SPACE to jump", 28, 160, 230)
    draw_text(screen, "Press ENTER to start", 28, 140, 280)
    pygame.display.flip()


def draw_background(screen, offset):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, ROAD_COLOR, (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y))
    for lane_x in (SCREEN_WIDTH // 3, SCREEN_WIDTH * 2 // 3):
        pygame.draw.line(screen, LANE_COLOR, (lane_x, GROUND_Y), (lane_x, SCREEN_HEIGHT), 4)
    for x in range(-40, SCREEN_WIDTH + 40, 80):
        pygame.draw.rect(screen, LANE_COLOR, (x + offset, GROUND_Y + 150, 40, 8), border_radius=4)


def show_game_over(screen, score, high_score):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, ROAD_COLOR, (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y))
    draw_text(screen, "GAME OVER", 48, 180, 110)
    draw_text(screen, f"Score: {score}", 36, 220, 180)
    draw_text(screen, f"High Score: {high_score}", 28, 220, 230)
    draw_text(screen, "Press ENTER to play again", 28, 120, 280)
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Subway Surfer Style Game")
    clock = pygame.time.Clock()

    player = Player(280, GROUND_Y - PLAYER_HEIGHT)
    obstacles = []
    coins = []
    score = 0
    frames = 0
    scroll_offset = 0
    high_score = 0
    game_speed = 6
    running = True
    playing = False

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not playing and event.key == pygame.K_RETURN:
                    playing = True
                    obstacles.clear()
                    coins.clear()
                    score = 0
                    frames = 0
                    scroll_offset = 0
                    game_speed = 6
                    player.rect.x = 280
                    player.rect.y = GROUND_Y - PLAYER_HEIGHT
                    player.velocity_y = 0
                    player.on_ground = True
                if playing and event.key == pygame.K_SPACE:
                    player.jump()

        keys = pygame.key.get_pressed()
        if playing:
            dx = 0
            if keys[pygame.K_LEFT]:
                dx = -1
            elif keys[pygame.K_RIGHT]:
                dx = 1
            player.move(dx)
            player.update()

            frames += 1
            scroll_offset = (scroll_offset + game_speed) % 80
            if frames % 90 == 0:
                obstacles.append(Obstacle(SCREEN_WIDTH + 20, width=random.randint(30, 45), height=random.randint(40, 70), speed=game_speed))
            if frames % 120 == 0:
                coin_y = random.randint(180, GROUND_Y - 60)
                coins.append(Coin(SCREEN_WIDTH + 20, coin_y, speed=game_speed))

            for obstacle in obstacles[:]:
                obstacle.update()
                if obstacle.rect.right < 0:
                    obstacles.remove(obstacle)
                elif obstacle.rect.colliderect(player.rect):
                    playing = False

            for coin in coins[:]:
                coin.update()
                if coin.rect.right < 0:
                    coins.remove(coin)
                elif coin.rect.colliderect(player.rect):
                    coins.remove(coin)
                    score += 10

            score += 1
            game_speed = 6 + score // 300

        draw_background(screen, scroll_offset)

        if playing:
            for obstacle in obstacles:
                obstacle.draw(screen)
            for coin in coins:
                coin.draw(screen)
            player.draw(screen)
            draw_text(screen, f"Score: {score}", 28, 16, 16)
            draw_text(screen, f"Speed: {game_speed}", 28, 16, 44)
            draw_text(screen, f"High Score: {high_score}", 28, 16, 72)
        else:
            if frames == 0:
                show_start_screen(screen)
            else:
                high_score = max(high_score, score)
                show_game_over(screen, score, high_score)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
