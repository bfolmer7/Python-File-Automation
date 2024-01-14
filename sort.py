import os
import shutil

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
        print(f'Moved: {os.path.basename(source_path)} to {os.path.dirname(dest_path)}')
    else:
        print(f'Skipped: {os.path.basename(source_path)} (File already exists in destination)')

source_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')

for filename in os.listdir(source_folder):
    file_extension = filename.split('.')[-1].lower()
    dest_folder = get_destination_folder(file_extension)

    if dest_folder:
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(dest_folder, filename)
        move_file(source_path, dest_path)
    else:
        print(f'Ignored: {filename} (unknown type)')
