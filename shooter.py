import pygame


def main():
    # initialize the pygame module
    pygame.init()

    # logo and set the logo
    logo = pygame.image.load('./logo.jpg')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Joungwoo Baik')

    # set up screent width and height
    screen_width = 480
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))

    # background and set background
    background = pygame.image.load('./background.png')

    # character setting

    charcter_image = pygame.image.load('./character.png')
    character_size = charcter_image.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = screen_width / 2 - character_width/2
    character_y_pos = screen_height - character_height

    move_x_to_right = 0
    move_x_to_left = 0
    move_y_to_top = 0
    move_y_to_bottom = 0

    # pygame clock
    clock = pygame.time.Clock()

    running = True

    while running:
        # getting all events

        dt = clock.tick(60)
        for event in pygame.event.get():
            # if user clicks quit button at top right corner

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_y_to_top += 5
                elif event.key == pygame.K_DOWN:
                    move_y_to_bottom += 5
                elif event.key == pygame.K_LEFT:
                    move_x_to_left += 5
                elif event.key == pygame.K_RIGHT:
                    move_x_to_right += 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    move_y_to_top = 0
                elif event.key == pygame.K_DOWN:
                    move_y_to_bottom = 0
                elif event.key == pygame.K_LEFT:
                    move_x_to_left = 0
                elif event.key == pygame.K_RIGHT:
                    move_x_to_right = 0

        character_x_pos += move_x_to_right - move_x_to_left
        character_y_pos += move_y_to_bottom - move_y_to_top

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height
        # background position
        screen.blit(background, (0, 0))

        # character position
        screen.blit(charcter_image, (character_x_pos, character_y_pos))
        pygame.display.update()


if __name__ == "__main__":
    main()
