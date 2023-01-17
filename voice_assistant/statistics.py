from bs4 import BeautifulSoup
import requests


def get_statistics(path):
    statistics = []
    statistics2 = []
    url = path
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    statystyki_laczne = doc.find_all('table', attrs={
        'class': 'rs-standings-table stats-table table table-bordered table-hover table-condensed table-striped'})
    for row in statystyki_laczne:
        b = row.find_all('tbody')
        for for2 in b:
            c = for2.find('th')
            statistics2.append(int(c.string))
    for row in statystyki_laczne:
        a = row.find_all('td')
    for i in range(len(a)):
        statistics2.append(a[i].string)

    for i in range(8):
        row = doc.find_all('div', attrs={"class": "stats-icon"})[
            i]  # w ten sposob wybierajac indeksy 0-7 dostaniemy statystyki druzyny
        statistics.append(int(row.parent.find("span").string))

    return statistics, statistics2


def get_classification():
    classification = []
    url = "https://www.plusliga.pl/table.html"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    dane = doc.find_all('tr', attrs={"data-termin":"1-1-30"})
    for row in dane:
        team = row.find("a")
        classification.append(team.string)

    return classification


if __name__ == '__main__':
    print(get_classification())
