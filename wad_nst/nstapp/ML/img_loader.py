from . import *


class ImageLoader:
    def __init__(self, contentpath, stylepath):

        self.stylepath = stylepath
        self.contentpath = contentpath

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.imsize = 512 if torch.cuda.is_available() else 128  # use small size if no gpu
        self.loader = transforms.Compose(
            [transforms.Resize(imsize), transforms.ToTensor()]  # scale imported image
        )

    # transform it into a torch tensor

    def image_loader(self, image_name):
        image = Image.open(image_name)
        image = self.loader(image).unsqueeze(0)

        return image.to(device, torch.float)

    # style_img = image_loader("./data/images/neural-style/picasso.jpg")
    # content_img = image_loader("./data/images/neural-style/dancing.jpg")
    def open_images(self):
        style_img = image_loader(self.stylepath)
        content_img = image_loader(self.contentpath)
        assert style_img.size() == content_img.size()

        return content_img, style_img
