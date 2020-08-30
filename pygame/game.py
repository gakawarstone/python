# import files
import pygame
import chapter_dio as dio
from chapter_sprite import grant


def main():
    # pygame init function and set window title
    pygame.init()
    pygame.display.set_caption('GK')

    # functions call
    grant()
    dio.dio()
    dio.dio_new()

    # close window
    pygame.quit()


if __name__ == "__main__":
    main()
