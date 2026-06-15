import pygame as pyg
import random

pyg.init()

# Screen
screen = pyg.display.set_mode((1000, 512))
clock = pyg.time.Clock()
pyg.display.set_caption("Space Defenders")

icon = pyg.image.load("ufo.png")
pyg.display.set_icon(icon)

# Font
font = pyg.font.SysFont(None, 36)

# Load High Score from file
try:
    with open("highscore.txt", "r") as f:
        Highest_score = int(f.read())
except:
    Highest_score = 0

score = 0

# Player
player_img = pyg.image.load("ufo (1).png")
player_rect = player_img.get_rect(topleft=(450, 480))
player_speed = 10
player_lives = 3

# Bullet
bullet_img = pyg.image.load("bullet.png")
bullet_speed = 10
bullets = []
shoot_delay = 100
last_shot = 0

# Enemy
enemy_img = pyg.image.load("monster.png")
enemy_speed = 3
enemies = []
spawn_delay = 1500
last_spawn = 0
min_distance = 150

game_over = False
running = True


def reset_game():
    global score, player_lives, bullets, enemies, game_over, last_spawn, last_shot
    score = 0
    player_lives = 3
    bullets.clear()
    enemies.clear()
    player_rect.topleft = (450, 480)
    last_spawn = 0
    last_shot = 0
    game_over = False


while running:
    dt = clock.tick(60)
    current_time = pyg.time.get_ticks()

    # Events
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

        if event.type == pyg.KEYDOWN:
            if game_over and event.key == pyg.K_r:
                reset_game()

    if not game_over:

        # Player movement
        keys = pyg.key.get_pressed()
        if keys[pyg.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pyg.K_RIGHT]:
            player_rect.x += player_speed

        player_rect.left = max(0, player_rect.left)
        player_rect.right = min(1000, player_rect.right)

        # Auto shooting
        if current_time - last_shot > shoot_delay:
            bullet_rect = bullet_img.get_rect(midbottom=player_rect.midtop)
            bullets.append(bullet_rect)
            last_shot = current_time

        # Move bullets
        for bullet in bullets:
            bullet.y -= bullet_speed

        bullets = [b for b in bullets if b.bottom > 0]

        # Spawn enemies
        if len(enemies) == 0 or enemies[-1].y > min_distance:
            if current_time - last_spawn > spawn_delay:
                x = random.randint(0, 950)
                rect = enemy_img.get_rect(topleft=(x, 0))
                enemies.append(rect)
                last_spawn = current_time

        # Move enemies
        for enemy in enemies:
            enemy.y += enemy_speed

        # Check enemies reaching bottom
        for enemy in enemies[:]:
            if enemy.bottom >= 512:
                enemies.remove(enemy)
                player_lives -= 1
                if player_lives <= 0:
                    game_over = True

                    # Save high score
                    if score > Highest_score:
                        Highest_score = score
                        with open("highscore.txt", "w") as f:
                            f.write(str(Highest_score))

        # Collision detection
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

    # ================= DRAWING =================
    screen.fill((0, 0, 0))
    screen.blit(player_img, player_rect)

    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    high_text = font.render(f"High Score: {Highest_score}", True, (255, 255, 255))
    screen.blit(high_text, (400, 10))

    lives_text = font.render(f"Lives: {player_lives}", True, (255, 0, 0))
    screen.blit(lives_text, (850, 10))

    # Game Over text
    if game_over:
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        screen.blit(game_over_text, (400, 230))
        screen.blit(restart_text, (360, 270))

    pyg.display.update()

pyg.quit()
