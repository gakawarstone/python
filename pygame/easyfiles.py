class File:
    def __init__(self, file_name):
        self.link = file_name
        self.content = None

    def write(self, str):
        """
        write one string to the end of file
        includes /n
        """
        with open(self.link, 'a') as the_file:
            the_file.write(str + '\n')

    def read(self):
        """
        return list of file lines without \n
        you can take outp from attribute content
        """
        outp = []
        with open(self.link) as the_file:
            for line in the_file:
                outp.append(line.split())
        self.content = outp
        return outp
