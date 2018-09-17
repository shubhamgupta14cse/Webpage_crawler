# Webpage_crawler
A powerfull python program that lets you discover visible and hidden subdomain, directory and all the site links of a site/server.

## Library used

* Request
* BeautifulSoup
* Urllib


## Getting Started

To set up the project in your local enivironment ,first clone the repository and save it on your local environment/machine.
Go to the crawl(target_url) at the last line and enter the homepage url or base url instaed of target_url of the site you want to get info about

To get all the url of the site anter the target_url in the below give line at the bottom of the code
```
crawl(target_url)
```
To discover the sub domains go to the below mention code at line no 16 and change the value of the target_url string by the url of the page you want info about
```
 target_url="https://www.rottentomatoes.com"
```
To discover the directory and sub directory go to the below mention code at line no 16 and change the value of the target_url string by the url of the page you want info about
```
 target_url="https://www.rottentomatoes.com"
```
