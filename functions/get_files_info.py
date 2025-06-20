import os
def get_files_info(working_directory, directory=None):
    '''
    We represent directory and working_directory as a
    strings with absolute path, so basic restriction for
    llm that it can't work outside of working directory
    looks like directory_path doesn't contain all of the
    working_directory path inside of it
    '''

    if working_directory not in directory:
        print(
            f'Error: Cannot list "{directory}", as it is outside the permitted working directory'
        )
    
    pass

def get_fspath(path):
    return os.fspath(path)

print(get_fspath("/Users/masakra/workspace/github.com/greetingromansoldier/AI-Agent-in-Python"))
