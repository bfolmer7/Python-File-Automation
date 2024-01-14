import os
import shutil
import logging

logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def get_destination_folder(extension):
    user_profile = os.environ['USERPROFILE']
    destinations = {
        'png': os.path.join(user_profile, 'Pictures'),
        'jpg': os.path.join(user_profile, 'Pictures'),
        'jpeg': os.path.join(user_profile, 'Pictures'),
        'gif': os.path.join(user_profile, 'Pictures'),
        'jfif': os.path.join(user_profile, 'Pictures'),
        'mp4': os.path.join(user_profile, 'Videos'),
        'mov': os.path.join(user_profile, 'Videos'),
        'mp3': os.path.join(user_profile, 'Music'),
        'm4a': os.path.join(user_profile, 'Music'),
        'wav': os.path.join(user_profile, 'Music'),
        'docx': os.path.join(user_profile, 'Documents'),
        'pdf': os.path.join(user_profile, 'Documents'),
        'xlsx': os.path.join(user_profile, 'Documents'),
        'txt': os.path.join(user_profile, 'Documents'),
    }
    return destinations.get(extension.lower())

def move_file(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.move(source_path, dest_path)
        message = f'Moved: {os.path.basename(source_path)} to {os.path.dirname(dest_path)}'
        logging.info(message)
        return message
    else:
        message = f'Skipped: {os.path.basename(source_path)} (File already exists in destination)'
        logging.info(message)
        return message

source_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')

current_category = None  
separator = '-' * 50  

for filename in os.listdir(source_folder):
    file_extension = filename.split('.')[-1].lower()
    dest_folder = get_destination_folder(file_extension)

    if dest_folder:
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(dest_folder, filename)
        move_message = move_file(source_path, dest_path)

        if dest_folder != current_category:
            current_category = dest_folder
            logging.info(separator)

        logging.info(move_message)
    else:
        print(f'Ignored: {filename} (unknown type)')
