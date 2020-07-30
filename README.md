# pyjisho

Python HTTP client for the [Jisho.org](https://jisho.org/)
search API.

## Install

```bash
pip install pyjisho
```

## Usage

```python
from jisho import Client

client = Client()
response = client.search('house')
print(response)
```