
```Python
def get_domain_name(url):
    """
    Extracts the domain name from a URL string.

    Args:
        url (str): The URL string to extract the domain name from.

    Returns:
        str: The extracted domain name.
    """
    # Remove the protocol prefix (e.g. "http://", "https://") from the URL
    if url.startswith("http://"):
        domain = url[7:]
    elif url.startswith("https://"):
        domain = url[8:]
    else:
        domain = url

    # Remove the "www." prefix from the domain (if it exists)
    if domain.startswith("www."):
        domain = domain[4:]

    # Extract the domain name from the remaining string
    domain = domain.split('/')[0]

    return domain
```

```Python
s = 90
s%=60
print(s)
```

