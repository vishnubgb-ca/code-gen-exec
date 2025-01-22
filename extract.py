
import zipfile

def unzip_file(file_name):
    try:
        with zipfile.ZipFile(file_name, "r") as zip_ref:
            zip_ref.extractall()
        print("File unzipped successfully.")
    except zipfile.BadZipFile as e:
        print("BadZipFile: ", e)
    except FileNotFoundError as e:
        print("FileNotFoundError: ", e)
    except Exception as e:
        print("An error occurred: ", e)

unzip_file("Training.zip")

