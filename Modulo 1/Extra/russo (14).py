import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Naves com Upgrades")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 24)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nave_tipo = 1
        self.images = {
            1: self.create_image(40, 30, WHITE),
            2: self.create_image(45, 35, BLUE),
            3: self.create_image(50, 40, GREEN),
            4: self.create_image(55, 45, YELLOW),
            5: self.create_image(60, 50, PURPLE),
        }
        self.image = self.images[self.nave_tipo]
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        self.speed = 5
        self.last_shot = 0
        self.shoot_delay = 400
        self.shield = False

    def create_image(self, w, h, color):
        image = pygame.Surface((w, h))
        image.fill(color)
        return image

    def update(self, keys=None):
        if keys:
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullets = []
            if self.nave_tipo == 1:
                bullets.append(Bullet(self.rect.centerx, self.rect.top, -10, 0))
            elif self.nave_tipo == 2:
                bullets.append(Bullet(self.rect.centerx - 10, self.rect.top, -10, -1))
                bullets.append(Bullet(self.rect.centerx + 10, self.rect.top, -10, 1))
            elif self.nave_tipo == 3:
                bullets.append(Bullet(self.rect.centerx, self.rect.top, -10, 0))
                bullets.append(Bullet(self.rect.centerx - 15, self.rect.top, -10, -1))
                bullets.append(Bullet(self.rect.centerx + 15, self.rect.top, -10, 1))
            elif self.nave_tipo == 4:
                bullets.append(Bullet(self.rect.centerx, self.rect.top, -15, 0))
                bullets.append(Bullet(self.rect.centerx - 15, self.rect.top, -10, -1))
                bullets.append(Bullet(self.rect.centerx + 15, self.rect.top, -10, 1))
            elif self.nave_tipo == 5:
                bullets.append(Bullet(self.rect.centerx - 10, self.rect.top, -18, -1))
                bullets.append(Bullet(self.rect.centerx + 10, self.rect.top, -18, 1))
                bullets.append(Bullet(self.rect.centerx, self.rect.top, -18, 0))

            for b in bullets:
                all_sprites.add(b)
                bullets_group.add(b)

    def upgrade_nave(self):
        if self.nave_tipo < 5:
            self.nave_tipo += 1
            self.image = self.images[self.nave_tipo]
            self.rect = self.image.get_rect(center=self.rect.center)
            if self.nave_tipo == 2:
                self.speed = 7
            elif self.nave_tipo == 3:
                self.speed = 7
                self.shoot_delay = 350
            elif self.nave_tipo == 4:
                self.speed = 8
                self.shoot_delay = 300
                self.shield = True
            elif self.nave_tipo == 5:
                self.speed = 9
                self.shoot_delay = 250
                self.shield = True

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speedy, speedx):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(x, y))
        self.speedy = speedy
        self.speedx = speedx

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0 or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        size = random.randint(20, 40)
        self.image = pygame.Surface((size, size))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -40)
        self.speedy = random.randint(2, 5)
        self.hp = size // 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-150, -40)
            self.speedy = random.randint(2, 5)
            self.hp = self.rect.width // 10

all_sprites = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies_group.add(enemy)

score = 0
MAX_SCORE = 200000
next_upgrade_score = 50000

running = True
game_over = False

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        player.update(keys)
        if keys[pygame.K_SPACE]:
            player.shoot()

        all_sprites.update()  # OK, não precisa de keys aqui porque update de player aceita keys=None

        hits = pygame.sprite.groupcollide(enemies_group, bullets_group, False, True)
        for enemy, bullets_hit in hits.items():
            for _ in bullets_hit:
                enemy.hp -= 1
            if enemy.hp <= 0:
                enemy.kill()
                score += 1000
                new_enemy = Enemy()
                all_sprites.add(new_enemy)
                enemies_group.add(new_enemy)

        hits_player = pygame.sprite.spritecollide(player, enemies_group, True)
        if hits_player:
            if player.shield:
                for enemy in hits_player:
                    enemy.kill()
                    new_enemy = Enemy()
                    all_sprites.add(new_enemy)
                    enemies_group.add(new_enemy)
                player.shield = False
            else:
                game_over = True

        if score >= next_upgrade_score and player.nave_tipo < 5:
            player.upgrade_nave()
            next_upgrade_score += 50000

        if score >= MAX_SCORE:
            game_over = True

    screen.fill(BLACK)
    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    nave_text = font.render(f"Nave: {player.nave_tipo} / 5", True, WHITE)
    shield_text = font.render(f"Escudo: {'Ativo' if player.shield else 'Inativo'}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(nave_text, (10, 40))
    screen.blit(shield_text, (10, 70))

    if game_over:
        msg = "VOCÊ VENCEU!" if score >= MAX_SCORE else "GAME OVER! Aperte R para reiniciar."
        msg_surface = font.render(msg, True, RED)
        screen.blit(msg_surface, (WIDTH // 2 - msg_surface.get_width() // 2, HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Resetar o jogo
            score = 0
            next_upgrade_score = 50000
            game_over = False
            player = Player()
            all_sprites.empty()
            enemies_group.empty()
            bullets_group.empty()
            all_sprites.add(player)
            for _ in range(8):
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies_group.add(enemy)

    pygame.display.flip()

pygame.quit()
sys.exit()
