import requests as r
from dataclasses import dataclass

@dataclass
class Quote:
    quote: str
    author: str

def get_quote(url: str) -> Quote:
    response: r.Response = r.get(url=url, verify=False)
    data: dict = response.json()[0]

    quote: str = data.setdefault('content', '...')
    author: str = data.setdefault('author', '...')

    return Quote(quote, author)

if __name__ == '__main__':
    url: str = 'https://api.quotable.io/quotes/random'
    quote: Quote = get_quote(url)
    print('Quote:', quote.quote)
    print('Author:', quote.author)