class File:
    def __init__(self, file_name):
        self.link = file_name

    def write(self, str):
        with open(self.link, 'a') as the_file:
            the_file.write(str + '\n')

    def read(self):
        outp = []
        with open(self.link) as the_file:
            for line in the_file:
                outp.append(line.split())
        self.content = outp
        return outp
