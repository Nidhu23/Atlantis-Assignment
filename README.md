# Atlantis-Assignment
# README

The repo consists 5 files with solutions to the atlantis assignment.

- github_repo_scrapper
- lifts
- pronunciable
- shortest_city_distance
- wikipedia_scrapper

`python3.8` is used for the development of this project.
Please ensure that you have installed all the requirements.

```shell
pip install -r requirements.txt
```

### github_repo_scrapper
github_repo_scrapper scraps all the links in [awesome-python](https://github.com/vinta/awesome-python) and will output the link matching the word given user.

```shell
python github_repo_scrapper.py
Query? about
Output https://github.com/about
```

### pronunciable
pronunciable program lists all pronunciable substrings of a given string.
```shell
python pronunciable.py
Enter a word ? hello
Output lheol hoe ohle lhol eh hole ellho ellh eollh ohell ...., etc
```

### shortest_city_distance
shortest_city_distance program finds the shortest travel path between 4 cities
```shell
python shortest_city_distance.py
City A: 51.5074 N, 0.1278 W
City B: 60.8566 N, 2.3522 E
City C: 55.2311 N, 2.1222 E
City D: 64.0010 N, 0.1002 W
Output A to C to B to D
```

### wikipedia_scrapper
wikipedia_scrapper scraps a given wikipedia page and return the average of 3 letter, 4 letter and 5-letter words per paragraph
```shell
python wikipedia_scrapper.py
Enter a wikipedia page url https://en.wikipedia.org/wiki/Earth
20 3 letter words/paragraph
12 4 letter words/paragraph
14 5 letter words/paragraph
```

### lifts
program to allot to most efficiently lift to a user who requests it from any floor.
```shell
python lifts.py
Enter a request? 10U
Lift #{2} will be coming up to receive you.
```