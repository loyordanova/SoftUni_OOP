def start_playing(obj):
    return obj.play()


class Guitar:
    def play(self):
        return 'Guitar is playing'


guitar = Guitar()
print(start_playing(guitar))