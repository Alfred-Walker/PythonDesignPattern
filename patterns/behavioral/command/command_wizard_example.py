class Wizard:
    def __init__(self, src, root_dir):
        self.choices = []
        self.root_dir = root_dir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.root_dir)
            else:
                print("No Operation")


if __name__ == '__main__':
    # client side code
    wizard = Wizard('python3.5.gzip', '/usr/bin/')

    # choices of the user
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()
    # >>> Copying binaries -- python3.5.gzip  to  /usr/bin/
    # >>> No Operation
