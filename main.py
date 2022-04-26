import os
from PIL import Image
import shutil

images_folder_file = 'images_folder.txt'
converted_directory = 'CONVERTED'


def input_images_folder():
    print('>> Inform your images path, example:')
    print('>> "/home/johndoe/photos/your_folder"')
    new_path = input('>> ')

    if not os.path.isdir(new_path):
        print(f'>> Directory {new_path} does not exists.')
        return input_images_folder()

    with open(images_folder_file, 'w') as file:
        file.write(new_path)

    return new_path


def get_images_folder():
    path = ''
    try:
        with open(images_folder_file) as file:
            try:
                path = file.readlines()[0]
            except:
                pass

            if not path or not os.path.isdir(path):
                path = input_images_folder()

    except FileNotFoundError as error:
        path = input_images_folder()

    return path


def main(main_images_folder):
    if not os.path.isdir(main_images_folder):
        os.remove(images_folder_file)
        raise NotADirectoryError(
            f'>> Directory {main_images_folder} does not exists.')

    converted_full_path = os.path.join(main_images_folder, converted_directory)
    try:
        shutil.rmtree(converted_full_path)
    except:
        pass

    os.mkdir(converted_full_path)

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)
            if extension != '.webp' and extension != '.png' and extension != '.jpeg' and extension != '.jpg':
                continue

            new_file_full_path = os.path.join(root, converted_directory, file)

            if os.path.isfile(new_file_full_path):
                print(f'>> Image {new_file_full_path} already exists.')
                continue

            img_pillow = Image.open(file_full_path)
            width, height = img_pillow.size

            new_image = img_pillow.resize(
                (width, height),
                Image.Resampling.LANCZOS
            )

            try:
                new_image.save(
                    new_file_full_path,
                    optimize=True,
                    quality=70,
                )

                print(f'>> Image {file_full_path} converted with succcess.')
            except:
                pass
            finally:
                new_image.close()
                img_pillow.close()


if __name__ == '__main__':
    main_images_folder = get_images_folder()
    print(f'\n>> Image Optimizer v0.1.0 - by Bruno Hubner\n')
    main(main_images_folder)
    print('\n')
