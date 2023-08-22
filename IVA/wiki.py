import wikipediaapi

# Specify a user agent for your application
user_agent = "YourAppName/1.0 (YourContactInfo)"

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',  # Language code for English Wikipedia, adjust as needed
    user_agent=user_agent
)

# Now you can perform your Wikipedia API requests as before
page_title = "Python (programming language)"
page = wiki_wiki.page(page_title)

if page.exists():
    print("Page title: ", page.title)
    print("Page summary: ", page.summary)
else:
    print("Page does not exist.")
