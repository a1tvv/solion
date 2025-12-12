import pygame
pygame.init()

WIN_W, WIN_H = 400, 700
win = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Платформер 2 игрока")

clock = pygame.time.Clock()

# параметры игрока
player_w, player_h = 40, 40
speed = 5
jump_power = -15
gravity = 1

# сброс
def reset_game():
    return {
        "p1_x": 100, "p1_y": 600,
        "p2_x": 250, "p2_y": 600,

        "p1_xvel": 0,
        "p1_yvel": 0,
        "p2_xvel": 0,
        "p2_yvel": 0,

        "p1_ground": False,
        "p2_ground": False
    }

state = reset_game()

# платформы
platforms = [
    pygame.Rect(40, 600, 300, 20),
    pygame.Rect(20, 500, 150, 20),
    pygame.Rect(230, 400, 150, 20),
    pygame.Rect(80, 300, 180, 20),
    pygame.Rect(140, 200, 120, 20)
]


# корректная коллизия
def move_and_collide(px, py, xvel, yvel):
    rect = pygame.Rect(px, py, player_w, player_h)

    # движение по X
    rect.x += xvel
    for pl in platforms:
        if rect.colliderect(pl):
            if xvel > 0:
                rect.right = pl.left
            elif xvel < 0:
                rect.left = pl.right

    # движение по Y
    rect.y += yvel
    on_ground = False
    for pl in platforms:
        if rect.colliderect(pl):
            if yvel > 0:  # упал сверху
                rect.bottom = pl.top
                yvel = 0
                on_ground = True
            elif yvel < 0:  # ударился головой снизу
                rect.top = pl.bottom
                yvel = 0

    return rect.x, rect.y, yvel, on_ground


run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                state = reset_game()

    keys = pygame.key.get_pressed()

    # --- игрок 1 ---
    state["p1_xvel"] = 0
    if keys[pygame.K_a]:
        state["p1_xvel"] = -speed
    if keys[pygame.K_d]:
        state["p1_xvel"] = speed
    if keys[pygame.K_w] and state["p1_ground"]:
        state["p1_yvel"] = jump_power

    state["p1_yvel"] += gravity

    state["p1_x"], state["p1_y"], state["p1_yvel"], state["p1_ground"] = move_and_collide(
        state["p1_x"], state["p1_y"], state["p1_xvel"], state["p1_yvel"]
    )

    # --- игрок 2 ---
    state["p2_xvel"] = 0
    if keys[pygame.K_LEFT]:
        state["p2_xvel"] = -speed
    if keys[pygame.K_RIGHT]:
        state["p2_xvel"] = speed
    if keys[pygame.K_UP] and state["p2_ground"]:
        state["p2_yvel"] = jump_power

    state["p2_yvel"] += gravity

    state["p2_x"], state["p2_y"], state["p2_yvel"], state["p2_ground"] = move_and_collide(
        state["p2_x"], state["p2_y"], state["p2_xvel"], state["p2_yvel"]
    )

    # --- отрисовка ---
    win.fill((20, 20, 20))

    for pl in platforms:
        pygame.draw.rect(win, (255, 170, 0), pl)

    pygame.draw.rect(win, (255, 0, 0), (state["p1_x"], state["p1_y"], player_w, player_h))
    pygame.draw.rect(win, (0, 120, 255), (state["p2_x"], state["p2_y"], player_w, player_h))

    font = pygame.font.SysFont(None, 24)
    txt = font.render("Press R to restart", True, (230, 230, 230))
    win.blit(txt, (120, 20))

    pygame.display.update()

    finish_rect = pygame.Rect(150, 100, 100, 20)
    if p1_rect.colliderect(finish_rect) or p2_rect.colliderect(finish_rect):
        game_finished = True
    if game_finished:
        win.blit(finish_frames[frame_index], (finish_rect.x, finish_rect.y))
        frame_index += 1
    if frame_index >= len(finish_frames):
        frame_index = 0

pygame.quit()