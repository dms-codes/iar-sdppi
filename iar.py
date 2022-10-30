import requests
from bs4 import BeautifulSoup as bs
import string
from datetime import datetime
import csv

def get_data(callsign, counts):
    #print(f'{counts}\tProcessing {callsign}')
    serviceurl = "https://iar-ikrap.postel.go.id/registrant/searchDataIar/?callsign="+callsign
    payload = {
               'callsign':callsign,
              }
    html = requests.post(serviceurl, data=payload).content
    soup = bs(html, 'html.parser')
    res = soup.text
    for tag in ['"','<\/ul>','\\n','<\/i>','<\/li>','<\/div>','<\/ul>"','                                              ','                                                                                            ']:
        res = res.replace(tag,'')
        res = res.lstrip()
        res = res.rstrip()
    _, status = res.split('Status : ')
    _, tingkat = _.split('Tingkat (License Class) : ')
    _, masalaku = _.split('Masa Laku (Date of expiration) : ')
    _, callsign = _.split('Tanda Panggilan (Callsign) : ')
    _, provinsi = _.split('Provinsi (Province) : ')
    _, nama = _.split('Nama Pemilik (Full name) : ')
    nama,provinsi,callsign,masalaku,tingkat,status = nama.rstrip(),provinsi.rstrip(),callsign.rstrip(),masalaku.rstrip(),tingkat.rstrip(),status.rstrip()
    nama,provinsi,callsign,masalaku,tingkat,status = nama.lstrip(),provinsi.lstrip(),callsign.lstrip(),masalaku.lstrip(),tingkat.lstrip(),status.lstrip()
    new_row = [callsign,nama,status,tingkat,provinsi,masalaku,tingkat]
    #print(f'{callsign},{nama},{provinsi},{masalaku},{tingkat},{status}')
    return new_row

def run():
    start = datetime.now()
    print('Time start : ',start)
    counts = 0
    with open('data-iar.csv','a+',encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        col_names = ['callsign','nama','provinsi','masalaku','tingkat','status']
        writer.writerow(col_names)
        for tingkat in ['b','c','d','e','f','g','h']:
            for area in ['0','1','2','3','4','5','6','7','8','9']:
                for a in ' '+string.ascii_lowercase:
                    for b in ' '+string.ascii_lowercase:
                        for c in ' '+string.ascii_lowercase:
                            for d in ' '+string.ascii_lowercase:
                                try:
                                    if c==' ' and d!=' ':
                                        continue
                                    elif b==' ' and c!=' ':
                                        continue
                                    elif a==' ' and b!=' ':
                                        continue
                                    else:
                                        counts += 1
                                        d = get_data('y'+tingkat+area+a+b+c+d,counts)
                                        writer.writerow(d)
                                        print(f'{d[0]},{d[1]},{d[2]},{d[3]},{d[4]},{d[5]}')
                                except:
                                    pass  
        end = datetime.now()
        print('Time finish: ',end)
        delta = end - start
        
                    
if __name__ == '__main__':
    run()
  
