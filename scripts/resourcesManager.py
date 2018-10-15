
class ResourcesManager:
    # private members for file manager
    __images = {1: "resources/images/overtime_level1.png",
                2: "resources/images/overtime_level2.png",
                3: "resources/images/overtime_level3.png",
                4: "resources/images/overtime_level4.png",
                'about_image': "resources/images/skull.jpeg"}

    def __init__(self):
        self.__init_resources()

    def __init_resources(self):
        pass

    def get_overtimes_level_image(self, level_index):
        if level_index <= 4:
            return self.__images[level_index]

    def get_about_image(self):
        return self.__images['about_image']


