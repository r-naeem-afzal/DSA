import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from linked_lists.doubly_circular_linked_list import (
    DoublyCircularLinkedList,
)


class Carousel:
    def __init__(self) -> None:
        self.images = DoublyCircularLinkedList()

    def add_image(self, image_name: str) -> None:
        self.images.append(image_name)
        print(f'Image "{image_name}" added to the carousel.')

    def remove_image(self, image_name: str) -> None:
        self.images.delete_node(image_name)
        print(f'Image "{image_name}" removed from the carousel.')

    def show_images(self) -> None:
        images = self.images.display()
        if images:
            print("Current Carousel:", " -> ".join(images))
        else:
            print("The carousel is empty.")

    def show_images_reverse(self) -> None:
        images = self.images.display_reverse()
        if images:
            print("Current Carousel (Reverse):", " -> ".join(images))
        else:
            print("The carousel is empty.")


carousel = Carousel()
carousel.add_image("image1.jpg")
carousel.add_image("image2.jpg")
carousel.add_image("image3.jpg")
carousel.show_images()  # Output: Carousel (forward): image1.jpg -> image2.jpg -> image3.jpg
carousel.show_images_reverse()  # Output: Carousel (backward): image3.jpg -> image2.jpg -> image1.jpg
carousel.remove_image("image2.jpg")
carousel.show_images()  # Output: Carousel (forward): image1.jpg -> image3.jpg
