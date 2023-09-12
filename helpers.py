import os
import requests
import folium

STORAGE_ICON = "./assets/Storage_Icon.png"
CPU_ICON = "./assets/CPU_Icon.png"
Plain_ICON = "./assets/Plain_Icon.png"
Shadow = "./assets/Shadow.png"

class Icons:

    @classmethod
    def storage(cls):
        return cls.custom_icon_generator(STORAGE_ICON, icon_size=(24, 32), icon_anchor=(10, 28))

    @classmethod
    def cpu(cls):
        return cls.custom_icon_generator(CPU_ICON, icon_size=(24, 32), icon_anchor=(10, 28))

    @classmethod
    def plain(cls, size=.1):
        return cls.custom_icon_generator(
            Plain_ICON,
            icon_size=(293 * size, 424 * size),
            icon_anchor=((293 * size)/ 2, 424 * size),
            popup_anchor=(0, -415 * size),
            shadow_image=Shadow,
            shadow_size=(298 * size, 86 * size),
            shadow_anchor=((149 * size)/ 2, 86 * size)
        )

    @classmethod
    def custom_icon_generator(cls, icon_path, icon_size: tuple, icon_anchor: tuple, **kwargs):
        return folium.features.CustomIcon(icon_path, icon_size=icon_size, icon_anchor=icon_anchor, **kwargs)


if __name__ == "__main__":
    print(Icons.cpu())