

import random

class Film:
    def __init__(self,tytuł: str,rok_wyd: int ,gatunek: str):
        self.tytuł=tytuł
        self.rok_wyd=rok_wyd
        self.gatunek=gatunek
        self.counter=0



    def __str__(self):
        return f"{self.tytuł} {self.rok_wyd} {self.gatunek}"

    def play(self):
        self.counter +=1

class Serial(Film):
    def __init__(self,sezon: int,epizod: int,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.sezon=sezon
        self.epizod=epizod

    def __str__(self):
        return f" {self.tytuł} {self.rok_wyd} {self.gatunek} S{self.sezon:02} E{self.epizod:02}"


baza=[Film("Venom 2", 2021 ,"Sci-fi"),Film("Project Adam",2022,"Sci-fi"),Film("Monthy Python i Święty Grall",1975,"Komedia"),
    Serial(2,3,"Peaky Blinder's",2018,"Sensacyjny" ),Serial(2,7,"Vikings",2018,"Przygodowy")]

def genarate_views(baza :Film):
    for i in range(random.randint(0,10)):
        baza.play()

def get_movies(baza: list):
    result = []
    for f in baza:
        if isinstance(f,Film) and not  isinstance (f,Serial):
            result.append(f)
        return result
for f in baza:
    print(f)