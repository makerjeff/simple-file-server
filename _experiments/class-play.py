import time

class Song(object):

    # defines the class parameters.
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            time.sleep(0.250)
        time.sleep(1)


def Main():
    happy_bday = Song(['Happy birthday to you', 'I don\'t want to get sued', 'so I\'ll stop right there'])
    bulls_on_parade = Song(['They rally around tha family', 'with pockets full of shells.'])

    happy_bday.sing_me_a_song()
    bulls_on_parade.sing_me_a_song()


if __name__ == '__main__':
    Main()