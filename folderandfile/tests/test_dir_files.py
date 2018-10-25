import os
from folderandfile.dir_files import DirFiles

def test_createDirFilesInstance():
    '''
    Validates if it's possible to create an instance of
    DirFiles class
    :return: Boolean/Assertion
    '''

    dir_files = DirFiles()
    assert isinstance(dir_files, DirFiles)

def test_createFolder():
    '''
    Validates if it's possible to create a folder
    in the current directory
    :return:
    '''

    dir_files = DirFiles()
    dir_files.create_folder()

def test_createFolderWithName():
    '''
    Validates if it's possible to create a folder
    in the current diretory given a name
    :return: Bollean if the tests passes or nah
    '''

    dir_files = DirFiles()
    expected_folder = 'folder1'
    dir_files.create_folder(expected_folder)
    # get current working directory
    current_path = os.getcwd()
    result = os.path.exists(os.path.join(current_path,expected_folder))

    assert result == True

def test_create_file():
    '''

    :return:
    '''

    dir_files = DirFiles()
    dir_files.create_file()

    assert True

def test_createFileIntheGivenPath():
    '''
    Validates if it's possible to create a folder
    in the current diretory given a name
    :return: Bollean if the tests passes or nah
    :return:
    '''
    path = os.path.dirname(__file__)
    dir_files = DirFiles()
    dir_files.create_file(path, 'teste.txt')

    result = os.path.isfile(os.path.join(path, 'teste.txt'))
    assert result == True

