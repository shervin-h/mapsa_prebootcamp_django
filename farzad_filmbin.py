n = int(input())
films = list()
for i in range(n):
    films.append(input().strip())

for film in films:
    print(film.lower().title())
