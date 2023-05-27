from PIL import Image


class Constants:
    INCH = 2.54
    SQUARE = 0.25
    ROUND = 0.28


class ImageModifier:
    def __init__(self):
        self.image = None

    def show_image(self):
        self.image.show()

    def open_image(self, image_path):
        self.image = Image.open(image_path)

    def get_image_dimensions(self):
        return self.image.size

    @staticmethod
    def get_painting_resolution(dpi=None, size=(35, 50), stone_type='square'):
        width, height = size
        if dpi:
            return round(width / Constants.INCH * dpi), round(height / Constants.INCH * dpi)
        if stone_type == 'square':
            return round(width / Constants.SQUARE), round(height / Constants.SQUARE)
        return round(width / Constants.ROUND), round(height / Constants.ROUND)

    def resize_image(self, new_size):
        self.image = self.image.resize(new_size)

    def convert_to_png(self):
        self.image = self.image.convert("P", palette=Image.ADAPTIVE)

    def reduce_number_of_colors(self, colors):
        self.image = self.image.quantize(colors=colors)

    def save_image_as_jpg(self, path):
        self.image.convert("RGB").save(path, "JPEG")

    def print_number_of_unique_colors(self):
        pixels = self.image.getdata()
        unique_colors = set(pixels)
        print(len(unique_colors))


COLORS_NUM = 40  # number of unique diamond colors
PAINTING_SIZE = (60, 90)  # in centimeters

image_modifier = ImageModifier()
image_modifier.open_image("input.jpg")
ori_width, ori_height = image_modifier.get_image_dimensions()
mod_width, mod_height = image_modifier.get_painting_resolution(size=PAINTING_SIZE)
image_modifier.resize_image((mod_width, mod_height))
image_modifier.reduce_number_of_colors(colors=COLORS_NUM)
image_modifier.resize_image((ori_width, ori_height))
image_modifier.save_image_as_jpg('output.jpg')
image_modifier.print_number_of_unique_colors()
