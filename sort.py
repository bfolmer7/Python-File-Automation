import os
import shutil


source_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')

destinations = {
    'png': os.path.join(os.environ['USERPROFILE'], 'Pictures'),
    'jpg': os.path.join(os.environ['USERPROFILE'], 'Pictures'),
    'jpeg': os.path.join(os.environ['USERPROFILE'], 'Pictures'),
    'gif': os.path.join(os.environ['USERPROFILE'], 'Pictures'),
    'jfif': os.path.join(os.environ['USERPROFILE'], 'Pictures'),
    'mp4': os.path.join(os.environ['USERPROFILE'], 'Videos'),
    'mov': os.path.join(os.environ['USERPROFILE'], 'Videos'),
    'mp3': os.path.join(os.environ['USERPROFILE'], 'Music'),
    'm4a': os.path.join(os.environ['USERPROFILE'], 'Music'),
    'wav': os.path.join(os.environ['USERPROFILE'], 'Music'),
    'docx': os.path.join(os.environ['USERPROFILE'], 'Documents'),
    'pdf': os.path.join(os.environ['USERPROFILE'], 'Documents'),
    'xlsx': os.path.join(os.environ['USERPROFILE'], 'Documents'),
    'txt': os.path.join(os.environ['USERPROFILE'], 'Documents'),
}

for filename in os.listdir(source_folder):
    file_extension = filename.split('.')[-1].lower()

    dest_folder = destinations.get(file_extension)

    if dest_folder:
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(dest_folder, filename)

        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        if not os.path.exists(dest_path):
            shutil.move(source_path, dest_path)
            print(f'Moved: {filename} to {dest_folder}')
        else:
            print(f'Skipped: {filename} (File already exists in destination)')
    else:
        print(f'Ignored: {filename} (unknown type)')
