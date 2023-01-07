from bs4 import BeautifulSoup
import requests


def get_statistics(path):
    statistics = []
    statistics2 = []
    url = path
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    statystyki_laczne = doc.find_all('table', attrs={'class': 'rs-standings-table stats-table table table-bordered table-hover table-condensed table-striped'})
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
        row = doc.find_all('div', attrs={"class" : "stats-icon"})[i] #w ten sposob wybierajac indeksy 0-7 dostaniemy statystyki druzyny
        statistics.append(int(row.parent.find("span").string))

    return statistics, statistics2


if __name__ == '__main__':

    statistics  = get_statistics("https://www.plusliga.pl/statsTeams/type/teams/id/1401.html")
    print(statistics)