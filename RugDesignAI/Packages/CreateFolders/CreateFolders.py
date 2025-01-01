import os
from datetime import datetime
from random import randint

class CreateFolder:
    @staticmethod
    def CreateFolders():
        current_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

        rond_num = randint(0, 1000000)
        main_folder = f"Temp/{current_time} - Sera{rond_num}"

        subfolders = ['Patterns', 'Vertical', 'U', 'Horizontal', 'Design']

        for subfolder in subfolders:
            subfolder_path = os.path.join(main_folder, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
        return main_folder  # Return the main folder path