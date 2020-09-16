# `confluence-crawler`: A utility to grab data from tables on Confluence pages

### Setup
- Run `pip install pipenv` if you do not already have `pipenv` installed.
- Run `pipenv install` to install all of the dependencies (listed at the bottom)
- Run `pipenv shell` to enter the shell
- Run `python main.py` to run the program.

The program requires two differnet files to actually run:
`pages.csv` and `authDetails.json`

`pages.csv` is just a list of all the page ID's separated by a comma.

`authDetails.json` is formatted like so
```
{
	"api-token": "YOUR API TOKEN HERE",
	"username": "USERNAME/EMAIL OF THE OWNER OF THE API TOKEN",
	// Note that the endpoint base will change for Atlassian Cloud and
	// Atlassian server. This is for Cloud.
	"endpoint": "https://[YOUR-DOMAIN].atlassian.net/wiki"
}

```

Just drop these two in the base directory and that's all you need to run.

When you run the script, everything you need will be put into `tables.json`.

It's as easy as that! (＊^▽^＊)

#### A note:
This was made and tested with Python 3.7.2 and up, so while this *should* work with any Python 3 client,
I haven't tested it with anything else, so if it doesn't don't yell at me please. :)

### Dependencies
- `requests`
