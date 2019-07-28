import urllib.request
import json


def characters_get():
    """ Gets character list from the rickandmorty API """
    url = 'https://rickandmortyapi.com/api/character/'
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read().decode())
    #print(data)
    return data


def characters_save(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as fout:
        fout.write("id\tname\tstatus\tspecies\tgender\timage\turl\n")
        for item in data["results"]:
            fout.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                item["id"],
                item["name"],
                item["status"],
                item["species"],
                item["gender"],
                item["image"],
                item["url"]
            ))
    return


def solution(A):
    """ Finds a value that occurs in more than half of the elements of an array """
    n = len(A)
    L = [-1] + A
    count = 0
    pos = (n + 1) // 2
    candidate = L[pos]
    for i in range(1, n + 1):
        if L[i] == candidate:
            count = count + 1
    print(count, n/2)
    if count > n/2:
        return candidate
    return -1


if __name__ == '__main__':
    #characters_get()
    #characters_save(characters_get(), 'e:/temp/rick_and_morty.tsv')
    print(solution([2,2]))
