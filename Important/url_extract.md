Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet
Here's a Python function that extracts the domain name from a URL string:

python
Copy code
import re

def get_domain_name(url):
    """
    Extracts the domain name from a URL string.

    Args:
        url (str): The URL string to extract the domain name from.

    Returns:
        str: The extracted domain name.
    """
    # Remove the protocol prefix (e.g. "http://", "https://") from the URL
    domain = re.sub(r'^https?://', '', url)

    # Remove the "www." prefix from the domain (if it exists)
    domain = re.sub(r'^www\.', '', domain)

    # Extract the domain name from the remaining string
    domain = re.search(r'^[^./]+', domain).group()

    return domain
Here's how you can use this function to extract the domain name from a URL:

python
Copy code
url1 = "http://github.com/carbonfive/raygun"
domain1 = get_domain_name(url1)
print(domain1)  # Output: github

url2 = "http://www.zombie-bites.com"
domain2 = get_domain_name(url2)
print(domain2)  # Output: zombie-bites

url3 = "https://www.cnet.com"
domain3 = get_domain_name(url3)
print(domain3)  # Output: cnet



Regenerate response
Send a message...

ChatGPT Mar 23 Version. Free Research Preview. ChatGPT may produce inaccurate information about people, places, or facts
