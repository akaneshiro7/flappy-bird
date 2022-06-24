import random

import pygame
from pygame.locals import *

from draw import draw_mode
from draw import draw_text
from draw import draw_score
from draw import draw_background
from draw import draw_ground
from draw import draw_difficulty
from change_difficulty import change_difficulty

pygame.init()

clock = pygame.time.Clock()

# Create Window Variables
WINDOW_WIDTH = 864
WINDOW_HEIGHT = 936
MIDDLE_WIDTH = WINDOW_WIDTH // 2
MIDDLE_HEIGHT = WINDOW_HEIGHT // 2

# Create Window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Create Game Variables
ground_coordinate = 0
scroll = 4
FPS = 60
is_flying = False
game_over = False
gravity = 10
pipe_gap = 75
time_between_pipe = 1500
pipe_variety = 100
last_pipe = pygame.time.get_ticks() - time_between_pipe
score = 0
high_score = 0
in_pipe = False
WHITE = (255, 255, 255)
font = pygame.font.SysFont('Segoe UI', 40)
sound_played = False

# Load Images
background = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')
restart_button_img = pygame.image.load('img/restart.png')
game_over_img = pygame.image.load('img/gameover.png')
antigravity_button_img = pygame.image.load('img/antigravity.png')
normal_button_img = pygame.image.load('img/normal.png')
bird_img = pygame.image.load('img/bird1.png')
emma_img = pygame.image.load('img/emma.png')

# load difficulty pictures
difficulty_img = pygame.image.load('img/difficulty.png')
difficulty_images = []
for i in range(1, 5):
    img = pygame.image.load(f'img/difficulty{i}.PNG')
    difficulty_images.append(img)


# load images
num_images = []
for i in range(10):
    img = pygame.image.load(f'img/{i}.png')
    num_images.append(img)

# load sounds
die_sound = pygame.mixer.Sound('img/die.wav')
hit_sound = pygame.mixer.Sound('img/hit.wav')
point_sound = pygame.mixer.Sound('img/point.wav')
wing_sound = pygame.mixer.Sound('img/wing.wav')


# Create bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, antigravity=False):
        """
        Initialize Bird Attributes
        :param x: int, x coordinate of bird
        :param y: int, y coordinate of bird
        :param antigravity: boolean, whether antigravity mode is one
        """
        # Create Bird from Pygame Sprite Class
        pygame.sprite.Sprite.__init__(self)
        # Load Image of Bird
        self.image = pygame.image.load('img/bird1.png')
        # Create Rectangle from Image
        self.rect = self.image.get_rect()
        # Place Bird center at coordinates
        self.rect.center = [x, y]
        # Initialize the gravity
        self.vel = 0
        # Initialize Antigravity mode
        self.antigravity = antigravity

    def update(self):
        """
        Updates Bird's y coordinate
        :return: None
        """
        # If the bird is flying:
        if is_flying:
            # Create Constant Gravity
            self.vel += 0.5
            # Create Terminal Velocity
            if self.vel > 10:
                self.vel = 10
            # If antigravity is off, gravity goes down
            if self.antigravity is False:
                self.rect.y += int(self.vel)
            # If antigravity is on, gravity goes up
            elif self.antigravity is True:
                self.rect.y -= int(self.vel)
            # If the bird hits the ground, the bird stays on the ground
            if self.rect.bottom == 768:
                self.rect.bottom = 768

        # If the game is over and the bird is not on the ground
        if game_over is True and self.rect.bottom <= 768:
            # Make the bird fall fast and spin
            self.vel = 20
            self.image = pygame.transform.rotate(self.image, -90)

            # If antigravity is off, bird will fall down
            if self.antigravity is False:
                self.rect.y += self.vel
            # if antigravity is on, bird will fall up
            elif self.antigravity is True:
                self.rect.y -= self.vel

    def jump(self):
        """
        Allow the bird to jump
        :return: None
        """
        # Give bird movement in y direction
        self.vel = -8
        # play wing sound
        wing_sound.play()


# Create Pipe Class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        """
        Initialize pipe Class
        :param x: int, x coordinate of pipe
        :param y: int, y coordinate of pipe
        :param position: 'top' or 'bottom', pipe orientation
        """
        # Initialize Pipe from Pygame Sprite Class
        pygame.sprite.Sprite.__init__(self)
        # Draw pipe
        self.image = pygame.image.load('img/pipe.png')
        # Draw rectangle from pipe image
        self.rect = self.image.get_rect()
        # If the pipe is a top pipe,
        if position == 'top':
            # flip image
            self.image = pygame.transform.flip(self.image, False, True)
            # draw image at coordinates
            self.rect.bottomleft = [x, y - pipe_gap]
        # If pipe is a top pipe
        if position == 'bottom':
            # draw image at coordinates
            self.rect.topleft = [x, y + pipe_gap]

    def update(self):
        """
        Update Pipe Position
        :return:
        """
        # Move pipe at same speed of ground
        self.rect.x -= scroll
        # If pipe is off screen, delete pipe
        if self.rect.right < 0:
            self.kill()


def create_pipe():
    """
    Create pipes
    :return: None
    """
    # get random pipe height
    pipe_height = random.randint(-pipe_variety, pipe_variety)
    # Create one top and one bottom pipe
    bottom_pipe = Pipe(WINDOW_WIDTH, MIDDLE_HEIGHT + pipe_height, 'bottom')
    top_pipe = Pipe(WINDOW_WIDTH, MIDDLE_HEIGHT + pipe_height, 'top')
    # add pipes to pipe group
    pipe_group.add(bottom_pipe)
    pipe_group.add(top_pipe)


# Create Button Class
class Button:
    def __init__(self, x, y, image):
        """
        Initialize Button Attributes
        :param x: int, button x position
        :param y: int, button y coordinate
        :param image: pygame image
        """
        # Set image
        self.image = image
        # Get rectangle from image
        self.rect = self.image.get_rect()
        # Set center of rectangle to coordinates
        self.rect.center = (x, y)

    def draw(self):
        """
        Draw the Button and check if clicked
        :return: Boolean, True if button is clicked, False if not clicked
        """
        # Initially set the button to not clicked
        button_clicked = False
        window.blit(self.image, (self.rect.x, self.rect.y))
        # Get position of the mouse
        mouse_position = pygame.mouse.get_pos()
        # If mouse is over button
        if self.rect.collidepoint(mouse_position):
            # if mouse is clicked
            if pygame.mouse.get_pressed()[0] == 1:
                # THe button was clicked
                button_clicked = True
        # return whether button was clicked
        return button_clicked


# Define when a game is reset
def reset(image=bird_img):
    """
    Reset game variables
    :param image: pygame image, which image to redraw flappy as
    :return: None
    """
    global score
    global game_over
    global sound_played
    global high_score
    # Delete all pipes
    pipe_group.empty()
    # Reset bird to original position
    flappy.rect.x, flappy.rect.y = 100, 500
    # Reset bird to original position
    flappy.image = image
    # Reset Score
    score = 0
    # Reset the game over variable to false
    game_over = False
    # Reset the death sound played variable to false
    sound_played = False
    # If the difficulty or game mode is changed, set score to 0


# Create pipe and bird groups
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

# Create Instance of Bird Object
flappy = Bird(100, MIDDLE_WIDTH)
# add bird instance to group
bird_group.add(flappy)

# Create Button Objects from Button Class
# Restart Button
restart_button = Button(MIDDLE_WIDTH, MIDDLE_HEIGHT, restart_button_img)
# Mode change buttons
antigravity_button = Button(MIDDLE_WIDTH, MIDDLE_HEIGHT + 50, antigravity_button_img)
normal_button = Button(MIDDLE_WIDTH, MIDDLE_HEIGHT + 50, normal_button_img)

# Difficulty Buttons
difficulty1_button = Button(MIDDLE_WIDTH - 75, MIDDLE_HEIGHT + 200, difficulty_images[0])
difficulty2_button = Button(MIDDLE_WIDTH - 25, MIDDLE_HEIGHT + 200, difficulty_images[1])
difficulty3_button = Button(MIDDLE_WIDTH + 25, MIDDLE_HEIGHT + 200, difficulty_images[2])
difficulty4_button = Button(MIDDLE_WIDTH + 75, MIDDLE_HEIGHT + 200, difficulty_images[3])

emma_button = Button(0, 900, emma_img)


def check_score():
    """
    Check to see if the score was changed
    :return: None
    """
    global in_pipe
    global high_score
    global score
    # If there is at least one pipe
    if len(pipe_group) > 0:
        # If left of bird is passed leftmost of left pipe
        # and right of bird is not passed right of pipe
        # and the bird is not yet in pipe
        if flappy.rect.left > pipe_group.sprites()[0].rect.left \
                and flappy.rect.right < pipe_group.sprites()[0].rect.right \
                and in_pipe is False:
            # Set that the bird is in the pip
            in_pipe = True
        # If the bird is in the pipe
        # If the left of the bird passes the right of the pipe
        if in_pipe is True:
            if flappy.rect.left > pipe_group.sprites()[0].rect.right:
                # Add to score
                score += 1
                # Set bird to no longer in pipe
                in_pipe = False
                # Check if current score is greater than high score
                high_score = max(score, high_score)
                # play point sound
                point_sound.play()


# Main loop
if __name__ == '__main__':
    # Create infinite loop
    run = True
    while run is True:
        # Set Frames Per Second
        clock.tick(FPS)
        # Draw Main Code
        pipe_group.draw(window)

        check_score()

        # draw background
        draw_background(window, background)

        pipe_group.draw(window)
        bird_group.draw(window)
        bird_group.update()

        # animate ground
        draw_ground(window, ground, ground_coordinate)

        # if the bird is flying
        if is_flying:
            # move the ground
            ground_coordinate -= scroll
            # reset ground to original position
            if ground_coordinate == -36:
                ground_coordinate = 0
            # get current time
            current_time = pygame.time.get_ticks()
            # if enough time passed to create a pipe
            if current_time > time_between_pipe + last_pipe:
                # Create a pipe
                create_pipe()
                # Reset time of last pipe
                last_pipe = current_time
            # update the pipe group
            pipe_group.update()
        # if the bird hits the pipe or the bird hits the top
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
            # the game is over
            game_over = True
            # the bird can't fly
            is_flying = False
            # if the death sound hasn't played
            if sound_played is False:
                # play death sounds
                hit_sound.play()
                die_sound.play()
                # change the sound played to true
                sound_played = True

        # if bird is on ground
        if flappy.rect.bottom >= 768:
            # the game is over
            game_over = True
            # the bird can no longer fly
            is_flying = False
            # if a death sound hasn't played
            if sound_played is False:
                # play the death sound
                die_sound.play()
                # change the sound played to true
                sound_played = True
        # if the game is over
        if game_over:
            # draw the game over image
            window.blit(game_over_img, (200, 200))
            # draw the difficulty image
            window.blit(difficulty_img, (MIDDLE_WIDTH - 80, 580))

            # draw reset button
            if restart_button.draw() is True:
                # if button is clicked reset
                reset()
            # if the antigravity is off
            if flappy.antigravity is False:
                # draw antigravity button
                if antigravity_button.draw() is True:
                    # if the antigravity button is clicked,
                    # reset to antigravity mode
                    flappy.antigravity = True
                    reset()
            # if antigravity is on
            elif flappy.antigravity is True:
                # draw normal mode
                if normal_button.draw() is True:
                    # if normal modes is clicked,
                    # reset to normal mode
                    flappy.antigravity = False
                    reset()
            # draw difficulty buttons
            # if difficulty is changed,
            # reset to that difficulty mode

            # draw difficulty buttons
            # if difficulty button is clicked,
            # change difficulty

            if difficulty1_button.draw() is True:
                time_between_pipe = change_difficulty(1)
                reset()
            if difficulty2_button.draw() is True:
                time_between_pipe = change_difficulty(2)
                reset()
            if difficulty3_button.draw() is True:
                time_between_pipe = change_difficulty(3)
                reset()
            if difficulty4_button.draw() is True:
                time_between_pipe = change_difficulty(4)
                reset()
            if emma_button.draw() is True:
                reset(image=emma_img)

        # Get user inputs
        for event in pygame.event.get():
            # If user clicks x on window
            if event.type == pygame.QUIT:
                # turn game off
                run = False
            # if user presses key
            if event.type == pygame.KEYDOWN:
                # if user presses escape key
                if event.key == K_ESCAPE:
                    # turn game off
                    run = False
                # if user presses space
                if event.key == K_SPACE:
                    # if the bird is not flying and game is not over
                    # Basically if the bird has reset but game has not started
                    if is_flying is False and game_over is False:
                        # Allow the game to begin
                        is_flying = True
                    # if the game is running
                    if is_flying and game_over is False:
                        # allow the bird to jump
                        flappy.jump()

        # draw the scores
        draw_text(window, WHITE, 'High Score:', font, 20, 10)
        draw_score(window, high_score, num_images, 220, 25)
        draw_text(window, WHITE, 'Current Score:', font, 500, 10)
        draw_score(window, score, num_images, 750, 25)
        draw_text(window, WHITE, 'Mode:', font, 20, 65)
        draw_mode(window, flappy.antigravity, antigravity_button_img, normal_button_img, 140, 75)
        draw_text(window, WHITE, 'Difficulty:', font, 20, 120)
        draw_difficulty(window, difficulty_images, time_between_pipe, 180, 130)

        # Update the display
        pygame.display.update()
    # if the game is over,
    # delete the screen
    pygame.quit()
