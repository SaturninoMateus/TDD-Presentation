import os


class DirFiles:
    '''

    '''

    def create_folder(self, folder_name=None):
        '''

        :return:
        '''

        directory = os.getcwd()
        if folder_name:
            new_directory = os.path.join(directory, folder_name)
        else:
            new_directory = directory
        try:
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
        except OSError:
            raise ('Error {} creating folder in {}', folder_name, directory)

    def create_file(self, path=None, file=None):
        '''

        :return:
        '''
        if path and file:
            try:
                f = open(os.path.join(path, file), 'w')
                f.close()
            except:
                raise ('Error creating file {}', file)
