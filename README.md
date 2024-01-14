
# File Organizer

This Python script automatically organizes the files in your Downloads folder into designated folders based on their file extensions.

## How It Works

The script scans the Downloads folder, identifies files by their extensions, and moves them into appropriate folders such as Pictures, Videos, Music, and Documents.

## Usage

To use the script, simply run it with Python from your command line:

```bash
python file_organizer.py
```

Make sure you have Python installed on your system.

## Docker
To pull the image from Docker Hub, run the following command in your terminal:

```sh
docker pull bfol/file_organizer:v1.0
```

Once the image is pulled, you can run the container using the following command:

```sh
docker run -v /Users/YourUsername/Downloads:/app/Downloads bfol/file_organizer:v1.0
``` 

Replace YourUsername with your actual username on your system.


## License

This project is licensed under the MIT License.
