from unicodedata import name
import scrapy
from scraper.items import Subject
import sqlite3

def FindId(name,l_p, cursor):
    id = cursor.execute(f"""SELECT id FROM polls_subject WHERE name = ? AND lecture_practice = ?""", (name, l_p))
    return int(id.fetchone()[0])

def Check(value):
    if value != None:
        value = str(value)
        if '(' in value:
            value = value.split(' (')[0]
        return value
    return ''

class QuotesSpider(scrapy.Spider):
    name = 'mmf'

    def start_requests(self):
        urls = [
            'https://mmf.bsu.by/ru/raspisanie-zanyatij/dnevnoe-otdelenie/3-kurs/8-gruppa/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        products = response.css('tr')[1::]
        subj = Subject()
        con = sqlite3.connect("../db.sqlite3")
        cur = con.cursor()
        i = 1
        j = 1
        with con:
            for product in products:
                subj['name'] = Check(product.css("td.subject-teachers::text").get())
                subj['week'] = product.css('td.weekday::text').get()
                subj['lepr'] = Check(product.css('td.lecture-practice::text').get())
                subj['time'] = product.css('td.time::text').get()
                subj['room'] = Check(product.css('td.room::text').get())
                print(subj['name'])

                if not (subj['name'],subj['lepr']) in [*con.execute("""SELECT name, lecture_practice FROM polls_subject""")]:
                    cur.execute("""INSERT OR REPLACE INTO polls_subject(id, name, lecture_practice) VALUES(?, ?, ?)""",(i,subj['name'], subj['lepr']))
                    print("отработал")
                    # mass.append(subj['name']+subj['lepr'])
                    i+=1

                id =  FindId(name = subj['name'],l_p = subj['lepr'] ,cursor = cur)
                cur.execute(""" INSERT OR REPLACE INTO polls_timetable(id, subject_id, time, room, weekday) VALUES(?,?,?,?,?) """, (j, id, subj['time'], subj['room'], subj['week']))
                j+=1
