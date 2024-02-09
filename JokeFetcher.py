import requests


class JokeFetcher:
    def __init__(self):
        self._url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
        self._json = None

    def fetch_joke(self):
        response = requests.get(self._url)
        self._json = response.json()
        if self._json['category'] == 'Pun':
            raise PunJokeException("this joke is a pun\n")

    def get_joke(self):
        if self._json['type'] == 'single':
            return self._json['joke']
        elif self._json['type'] == 'twopart':
            return self._json['setup'] + '\n' + self._json['delivery']


class PunJokeException(Exception):
    def __init__(self, message):
        super().__init__(message)


def main():
    joke = JokeFetcher()
    response = True
    while response:
        try:
            joke.fetch_joke()
        except PunJokeException:
            answer = input("this joke is a pun, would you like to see it. answer yes or no\n")
            if answer== "yes":
                print('\n' + joke.get_joke())
        else:
            print('\n' + joke.get_joke())
        answer = input("\ndo you want to see another joke? yes or no\n")
        if answer == 'no':
            response = False
            print("okay bye\n")


if __name__ == '__main__':
    main()




