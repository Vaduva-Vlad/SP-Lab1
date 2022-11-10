from JPGImageLoader import JPGImageLoader
from BMPImageLoader import BMPImageLoader


class ImageLoaderFactory:
    def create(self, imagePath):
        if ".jpg" in imagePath:
            return JPGImageLoader()
        if '.bmp' in imagePath:
            return BMPImageLoader()
        return None
