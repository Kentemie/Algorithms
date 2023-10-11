# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

    # FileSystem() Initializes the object of the system.
    # List<String> ls(String path)
        # If path is a file path, returns a list that only contains this file's name.
        # If path is a directory path, returns the list of file and directory names in this directory.
        # The answer should in lexicographic order.
    # void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. 
    # If the middle directories in the path do not exist, you should create them as well.
    # void addContentToFile(String filePath, String content)
        # If filePath does not exist, creates that file containing given content.
        # If filePath already exists, appends the given content to original content.
    # String readContentFromFile(String filePath) Returns the content in the file at filePath.

# Unified Directory and File List

class File:

    def __init__(self):
        self.is_file = False
        self.content = []
        self.files = {}

    def __str__(self):
        return f"{self.files}"


class FileSystem:

    def __init__(self):
        self.root = File()

    def ls(self, path):
        curr_dir = self.root
        
        if path != "/":
            dirs = path.split("/")
            for dir in dirs[1:]:
                curr_dir = curr_dir.files[dir]
            if curr_dir.is_file:
                return [dirs[-1]]

        return sorted(curr_dir.files.keys())

    def mkdir(self, path):
        curr_dir = self.root 
        dirs = path.split("/")

        for dir in dirs[1:]:
            if dir not in curr_dir.files:
                curr_dir.files[dir] = File()
            curr_dir = curr_dir.files[dir]

    def addContentToFile(self, filePath, content):
        curr_dir = self.root
        dirs = filePath.split("/")

        for dir in dirs[1:-1]:
            curr_dir = curr_dir.files[dir]
        
        file_name = dirs[-1]
        if file_name not in curr_dir.files:
            curr_dir.files[file_name] = File()
        
        curr_dir = curr_dir.files[file_name]
        curr_dir.is_file = True
        curr_dir.content.append(content)

    def readContentFromFile(self, filePath):
        curr_dir = self.root
        dirs = filePath.split("/")

        for dir in dirs[1:]:
            curr_dir = curr_dir.files[dir]
        
        return "".join(curr_dir.content)

obj = FileSystem()
print(obj.ls("/"))
obj.mkdir("/a/b/c")
obj.addContentToFile("/a/b/c/d", "hello")
print(obj.ls("/"))
print(obj.readContentFromFile("/a/b/c/d"))
