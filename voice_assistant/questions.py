from statistics import *


def get_team(team):
    if team.lower() in ['rzeszów', 'asseco resovia rzeszów', 'asseco', 'resovia']:
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1401.html', "Asseco Resovia Rzeszów"]
    elif team.lower() in ['aluron CMC warta zawiercie', 'warta zawiercie', 'zawiercie', 'aluron']:
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/30288.html', "Aluron CMC Warta Zawiercie"]
    elif team.lower() in ['barkom każany lwów', 'lwów', 'barkom', 'każany', 'barkom każay', 'kazany',
                          'barkom kazany lwów']:
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/2100376.html', "Barkom Każany Lwów"]
    elif team.lower() in ['bbts bielsko biała', 'bielsko biała', 'bielsko', 'bielsko biala', 'bielsko-biała']:
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1548.html', "BBTS Bielsko-Biała"]
    elif team.lower() in 'cerrad enea czarni radom':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1545.html', "Cerrad Enea Czarni Radom"]
    elif team.lower() in 'kuprum lubin':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/26787.html', "Cuprum Lubin"]
    elif team.lower() in 'gks katowice':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/29741.html', "GKS Katowice"]
    elif team.lower() in 'grupa azoty zaksa kędzierzyn-koźle':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1410.html', "Grupa Azoty ZAKSA Kędzierzyn-Koźle	"]
    elif team.lower() in 'indykpol azs olsztyn':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1406.html', "Indykpol AZS Olsztyn"]
    elif team.lower() in 'jastrzębski węgiel':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1405.html', "Jastrzębski Węgiel"]
    elif team.lower() in 'luk lublin':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/2100016.html', "LUK Lublin"]
    elif team.lower() in 'pge skra bełchatów':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1407.html', "PGE Skra Bełchatów"]
    elif team.lower() in 'projekt warszawa':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1403.html', "Projekt Warszawa"]
    elif team.lower() in 'psg stal nysa':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1304.html', "PSG Stal Nysa"]
    elif team.lower() in 'ślepsk malow suwałki':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/30289.html', "Ślepsk Malow Suwałki"]
    elif team.lower() in 'trefl gdańsk':
        return ['https://www.plusliga.pl/statsTeams/type/teams/id/1411.html', "Trefl Gdańsk"]
    else:
        return None


def get_answer(question, team1, team2):
    statistics = get_statistics(team1)
    #staty drużynowe
    if question.lower() in ['ile mistrzostw polski', 'mistrzostwo', 'mistrzostwa polski', 'mistrzostwa']:
        return f'Liczba zdobytych mistrzostw Polski to {statistics[0][0]}.'
    elif question.lower() in ['ile wicemistrzostw polski', 'wicemistrzostwo', 'wicemistrzostwa polski', 'wicemistrzostwa']:
        return f'Liczba zdobytych wicemistrzostw Polski to {statistics[0][1]}.'
    elif question.lower() in ['ile trzecich miejsc', 'trzecie miejsce', 'trzecie']:
        return f'Liczba zdobytych trzecich miejsc Polski to {statistics[0][2]}.'
    elif question.lower() in ['podium mistrzostw polski', 'podium', 'ile razy na podium']:
        return f'Liczba zdobytych mistrzostw Polski to {statistics[0][0]}. ' \
               f'Liczba zdobytych wicemistrzostw Polski to {statistics[0][1]}. ' \
               f'Liczba zdobytych trzecich miejsc Polski to {statistics[0][2]}. '
    elif question.lower() in ['ile wygranych meczy', 'ile wygranych', 'wygrane']:
        return f'Drużyna wygrała {statistics[0][4]} meczy'
    elif question.lower() in ['ile przegranych meczy', 'ile przegranych', 'przegrane']:
        return f'Drużyna przegrała {statistics[0][5]} meczy'
    elif question.lower() in ['najdłuższa seria wygranych', 'seria wygranych', 'jaka najdłuższa seria wygranych']:
        return f'Najdłuższa seria wygranych meczy drużyny to {statistics[0][6]} '
    elif question.lower() in ['najdłuższa seria przegranych', 'seria przegranych', 'jaka najdłuższa seria przegranych']:
        return f'Najdłuższa seria przegranych meczy drużyny to {statistics[0][7]} '

    #staty łączne
    elif question.lower() in ['rozegrane mecze', 'ile rozegranych meczy', 'ile wszystkich meczy']:
        return f'Liczba rozegranych meczy przez drużynę to {statistics[1][0]} '
    elif question.lower() in ['rozegrane sety', 'ile rozegranych setów', 'ile setów']:
        return f'Liczba rozegranych setów przez drużynę to {statistics[1][1]} '
    elif question.lower() in ['zdobyte punkty', 'ile zdobytych punktów', 'ile punktów', 'punkty']:
        return f'Liczba zdobytych punktów przez drużynę to {statistics[1][2]} '
    elif question.lower() in ['zagrywka']:
        return f'Liczba wykonanych zagrywek przez drużynę to {statistics[1][3]}.  ' \
               f'`Asy {statistics[1][4]}. ' \
               f'Błędne zagrywki {statistics[1][5]}. ' \
               f'Średnia liczba asów na set {statistics[1][6]}.'
    elif question.lower() in ['as', 'asy', 'asy serwisowe', 'ile asów serwisowych']:
        return f'Liczba asów to {statistics[1][4]}. '
    elif question.lower() in ['błędne zagrywki', 'ile błędnych zagrywek']:
        return f'Liczba błędnych zagrywek to {statistics[1][5]}. '
    elif question.lower() in ['średnia asów', 'ile asów na set', 'asy na set']:
        return f'Średnia asów na set to {statistics[1][6]}. '
    elif question.lower() in ['przyjęcie']:
        return f'Liczba wykonanych przyjęć przez drużynę to {statistics[1][7]}. ' \
               f'Błędne przyjęcia {statistics[1][8]}. ' \
               f'Negatywne przyjęcia {statistics[1][9]}. ' \
               f'Perfekcyjne przyjęcia {statistics[1][10]}.   Procentowo {statistics[1][11]}%. '
    elif question.lower() in ['ile przyjęć', 'liczba przyjęć']:
        return f'Liczba wykonanych przyjęć przez drużynę to {statistics[1][7]}.'
    elif question.lower() in ['ile przyjęć błędnych', 'liczba przyjęć błędnych', 'błędne przyjęcia']:
        return f'Liczba wykonanych błędnych przyjęć przez drużynę to {statistics[1][8]}.'
    elif question.lower() in ['ile przyjęć negatywnych', 'liczba przyjęć negatywnych', 'negatywne przyjęcia']:
        return f'Liczba wykonanych negatywnych przyjęć przez drużynę to {statistics[1][9]}.'
    elif question.lower() in ['ile przyjęć perfekcyjnych', 'liczba przyjęć perfekcyjnych', 'perfekcyjne przyjęcia']:
        return f'Liczba wykonanych perfekcyjnych przyjęć przez drużynę to {statistics[1][10]}. Procentowo {statistics[1][11]}%.'
    elif question.lower() in ['atak']:
        return f'Liczba wykonanych ataków przez drużynę to {statistics[1][12]}' \
               f'Błędne ataki {statistics[1][13]}. ' \
               f'Zablokowane ataki {statistics[1][14]}. ' \
               f'Perfekcyjne ataki {statistics[1][15]}.  Procentowo {statistics[1][16]}%. '
    elif question.lower() in ['ile ataków', 'liczba ataków']:
        return f'Liczba wykonanych ataków przez drużynę to {statistics[1][12]}.'
    elif question.lower() in ['ile ataków błędnych', 'liczba ataków błędnych', 'błędne ataki']:
        return f'Liczba wykonanych błędbych przyjęć przez drużynę to {statistics[1][13]}.'
    elif question.lower() in ['ile ataków zablokowanych', 'liczba ataków zablokowanych', 'zablokowane ataki']:
        return f'Liczba zablokowanych własnych atakówto {statistics[1][14]}.'
    elif question.lower() in ['ile ataków perfekcyjnych', 'liczba ataków perfekcyjnych', 'perfekcyjne ataki']:
        return f'Liczba wykonanych perfekcyjnych ataków przez drużynę to {statistics[1][15]}. Procentowo {statistics[1][16]}%.'
    elif question.lower() in ['bloki']:
        return f'Liczba wykonanych bloków przez drużynę to {statistics[1][17]}. ' \
               f'Średnia liczba bloków na set to {statistics[1][18]}.'
    elif question.lower() in ['klasyfikacja', 'tabela', 'miejsce w tabeli']:
        return get_classification_place(team2)
    else:
        return 'Nie rozumiem'


def get_classification_place(team_name):
    classification = get_classification()
    for team in classification:
        if team == team_name:
            return f'Miejsce w tabeli to {classification.index(team) +1 }'



if __name__ == '__main__':

    print(get_classification_place("Cuprum Lubin"))