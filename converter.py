import subprocess, json, re
from glob import glob

class converter:

    def __init__(self):
        try:
            with open("config.json","r") as config:
                settings = json.load(config)
                self.dvd = settings["Optical Drive"]
                self.path = settings["Working Directory"]

        except FileNotFoundError:
            print("Please run setup.py before using the program!")
            exit()

        if self.path[-1] == '/':
            self.dir = self.path + 'dvd'
        else:
            self.dir = self.path + '/dvd'
        
        self.iso = self.dir + '.iso'
        self.log = self.dir + '.log'
    

    def decrypt(self):
        subprocess.run(
            [
                'dvdbackup',
                '-i',
                self.dvd,
                '-o',
                self.path,
                '-M',
                '-n',
                'dvd'
            ]
        )

    def digitalize(self):
        subprocess.run(
            [
                'mkisofs',
                '-dvd-video',
                '-udf',
                '-o',
                self.iso,
                self.dir
            ]
        )
        
    def handbrake(self):
        subprocess.run(f'flatpak run fr.handbrake.HandBrakeCLI -i {self.iso} --title 0 2> {self.log}',shell=True)

        with open(self.log,"r") as file:
            sign = "+ title "
            text = file.read()
            index = 0
            parts = 0
            while index < len(text):
                index = text.find(sign,index)
                if index == -1:
                    break
                parts += 1
                index += len(sign)

        existing = glob("/home/feron/Desktop/output*.mp4")
        numbers = [0]
        if existing:
            for filename in existing:
                match = re.search(r'output(\d+)\.mp4', filename)
                if match:
                    numbers.append(int(match.group(1)))
        n = max(numbers)

        for k in range(1,parts+1):
            subprocess.run(
                [
                    'flatpak',
                    'run',
                    'fr.handbrake.HandBrakeCLI',
                    '-i',
                    self.iso,
                    '-o',
                    f'/home/feron/Desktop/output{n+k}.mp4',
                    '-t',
                    str(k),
                    '--no-dvdnav'
                ]
            )

    def cleanup(self):
        ls = ['rm -r ' + self.dir, 'rm ' + self.log, 'rm ' + self.iso]
        for i in ls:
            subprocess.run(i,shell=True)

instance = converter()
instance.decrypt()
instance.digitalize()
instance.handbrake()
instance.cleanup()