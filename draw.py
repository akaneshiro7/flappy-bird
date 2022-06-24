# this module has all the draw functions
def draw_background(window, background):
    """
    Draws the background
    :param window: pygame window to draw the background on
    :param background: background image
    :return: None
    """
    window.blit(background, (0, 0))


def draw_ground(window, ground, ground_coordinate):
    """
    Draws background
    :param window: pygame window to draw ground on
    :param ground: ground image
    :param ground_coordinate: int, x coordinate for ground
    :return: None
    """
    window.blit(ground, (ground_coordinate, 768))


# create images from text and draw on screen
def draw_text(window, color, text, font, x, y):
    """
    Renders Image from Text and draws it at x and y coordinate
    :param window: pygame window
    :param color: RGB Color (R, G, B)
    :param text: string, text to draw on screen
    :param font: string, font loaded from pygame.SysFont
    :param x: int, x coordinate
    :param y: int, y coordinate
    :return: None
    """
    img = font.render(text, True, color)
    window.blit(img, (x, y))


def draw_mode(window, antigravity, antigravity_button_img, normal_button_img, x, y):
    """
    Draw antigravity or normal button image
    :param window: pygame window
    :param antigravity: Boolean, whether antigravity mode is on
    :param antigravity_button_img: pygame image
    :param normal_button_img: pygame image
    :param x: int, x coordinate
    :param y: int, y coordinate
    :return:
    """
    if antigravity is True:
        window.blit(antigravity_button_img, (x, y))
    if antigravity is False:
        window.blit(normal_button_img, (x, y))


# draw the score using the images
def draw_score(window, score, images, x, y):
    """
    Finds score and draws it at x and y
    :param window: pygame window
    :param score: int, game score
    :param images: list, pygame images of numbers
    :param x: x coordinate to draw first digit
    :param y: y coordinate to draw first digit
    :return: None
    """
    s = str(score)
    # draws at i * 25 to prevent number overlap if there are multiple digits
    for i in range(len(s)):
        if s[i] == '0':
            window.blit(images[0], (x + i*25, y))
        if s[i] == '1':
            window.blit(images[1], (x + i*25, y))
        if s[i] == '2':
            window.blit(images[2], (x + i*25, y))
        if s[i] == '3':
            window.blit(images[3], (x + i*25, y))
        if s[i] == '4':
            window.blit(images[4], (x + i*25, y))
        if s[i] == '5':
            window.blit(images[5], (x + i*25, y))
        if s[i] == '6':
            window.blit(images[6], (x + i*25, y))
        if s[i] == '7':
            window.blit(images[7], (x + i*25, y))
        if s[i] == '8':
            window.blit(images[8], (x + i*25, y))
        if s[i] == '9':
            window.blit(images[9], (x + i*25, y))


def draw_difficulty(window, difficulty_images, time_between_pipe, x, y):
    """
    Draw difficulty for user to see
    :param window: pygame window
    :param difficulty_images: list of pygame images
    :param time_between_pipe: int, time between each pipe
    :param x: int, x coordinate
    :param y: int y, coordinate
    :return: none
    """
    if time_between_pipe == 1500:
        window.blit(difficulty_images[0], (x, y))
    if time_between_pipe == 1250:
        window.blit(difficulty_images[1], (x, y))
    if time_between_pipe == 1000:
        window.blit(difficulty_images[2], (x, y))
    if time_between_pipe == 750:
        window.blit(difficulty_images[3], (x, y))
