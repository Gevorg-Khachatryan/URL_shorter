import random
import string

class shortner:
    def __init__(self,token_size=None):
        self.token_size = random.randrange(4,12,2)


    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token_size))