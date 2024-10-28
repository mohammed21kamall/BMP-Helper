import os
from datetime import datetime
from random import randint

class FolderCreator:
    def __init__(self, base_path="../../Temp"):
        self.base_path = base_path
        self.folder_name = self.generate_folder_name()
        self.main_folder_path = os.path.join(self.base_path, self.folder_name)
        self.subfolders = ["Horizontal", "Vertical", "U", "The Design"]

    def generate_folder_name(self):
        now = datetime.now()
        rand_num = randint(0, 100000)
        return now.strftime("%Y-%m-%d %H-%M-%S") + f" - Sera{rand_num}"

    def create_main_folder(self):
        os.makedirs(self.main_folder_path)

    def create_subfolders(self):
        for subfolder in self.subfolders:
            os.makedirs(os.path.join(self.main_folder_path, subfolder))

    def create_folders(self):
        self.create_main_folder()
        self.create_subfolders()

# كيفية الاستخدام
if __name__ == "__main__":
    folder_creator = FolderCreator()
    folder_creator.create_folders()