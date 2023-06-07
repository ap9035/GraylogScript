class GraylogAPIClient:
    def __init__(self, url, username: str = None, password: str = None):
        self.url: str = url
        self.username: str = username
        self.password: str = password

    def authenticate(self):
        pass

    def query(self, search_string: str):
        with open(self.url, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        matching_lines = [line for line in lines if search_string in line]
        return matching_lines
