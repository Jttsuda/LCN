import zipfile
import tarfile
import gzip
import shutil
import os
import filetype

counter = 1
new_file = "./flag0.zip"

def rename_file():
    global counter
    global new_file
    new_file = "./flag" + str(counter)
    if os.path.isfile('C:/Users/Suda/Desktop/Unzipping/flag.zip'):
        os.rename('flag.zip', new_file[2:] + ".zip")
        new_file += ".zip"
    elif os.path.isfile('C:/Users/Suda/Desktop/Unzipping/flag.tar'):
        os.rename('flag.tar', new_file[2:] + ".tar")
        new_file += ".tar"
    elif os.path.isfile('C:/Users/Suda/Desktop/Unzipping/flag.gz'):
        os.rename('flag.gz', new_file[2:] + ".gz")
        new_file += ".gz"
    counter += 1

def delete_previous_file():
    global counter
    path_name = 'C:/Users/Suda/Desktop/Unzipping/flag' + str(counter - 2)
    if os.path.isfile(path_name + '.zip'):
        os.remove(path_name + '.zip')
    elif os.path.isfile(path_name + '.tar'):
        os.remove(path_name + '.tar')
    elif os.path.isfile(path_name + '.gz'):
        os.remove(path_name + '.gz')

while True:
    print(counter)
    delete_previous_file()
    if new_file.endswith('zip'):
        with zipfile.ZipFile(new_file, 'r') as zip_ref:
            zip_ref.extractall('./')
            rename_file()
    elif new_file.endswith('tar'):
        my_tar = tarfile.open(new_file[2:])
        my_tar.extractall('./')
        my_tar.close()
        rename_file()
    elif new_file.endswith('gz'):
        with gzip.open(new_file[2:], 'r') as f_in, \
            open('flag', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                f_in.close()
                f_out.close()
                extension = "." + filetype.guess('C:/Users/Suda/Desktop/Unzipping/flag').extension
                os.rename('flag', 'flag' + str(counter) + extension)
                new_file = "./flag" + str(counter) + extension
                counter += 1
    else:
        break
input()