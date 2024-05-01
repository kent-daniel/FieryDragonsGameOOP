import random

import pygame
import math

from Character import CharacterImage


class DragonCard:
    def __init__(self):
        self.dragon_cards = []

    def generate_random_cards(self, num):
        for _ in range(num):
            random_character = random.choice(list(CharacterImage))
            self.dragon_cards.append((random_character,None))

    def display_cards(self, center_x, center_y, radius, screen):

        card_size = math.sqrt(2) * radius / 4
        # Calculate the spacing between cards
        spacing_x = math.sqrt(2) * radius / 5  # Adjust spacing for proper fit
        spacing_y = math.sqrt(2) * radius / 5  # Adjust spacing for proper fit

        # Calculate the top left corner of the first card
        card_start_x = center_x - math.sqrt(2) * radius // 2 + spacing_x / 2
        card_start_y = center_y - math.sqrt(2) * radius // 2 + spacing_y / 2

        # Blit each card inside the square
        for i, (character_image, _) in enumerate(self.dragon_cards):
            row = i // 4
            col = i % 4
            card_x = card_start_x + col * spacing_x
            card_y = card_start_y + row * spacing_y
            rect = pygame.Rect(card_x, card_y, card_size, card_size)  # Create a rect for each card
            self.dragon_cards[i] = (character_image, rect)  # Update tuple with rect
            card_image = pygame.image.load(character_image.value)
            scaled_card_image = pygame.transform.scale(card_image, (int(card_size), int(card_size)))
            screen.blit(scaled_card_image, (card_x, card_y))
