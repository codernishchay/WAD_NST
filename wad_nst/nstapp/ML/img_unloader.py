from . import *


class Unloader:
    def __init__(self):
        self.unloader = transforms.ToPILImage()

    def pil_img(self, tensor):
        image = tensor.cpu().clone()
        image = image.squeeze(0)  # remove the fake batch dimension
        image = self.unloader(image)

        return image
