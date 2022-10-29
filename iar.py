import requests
from bs4 import BeautifulSoup as bs
import string

def get_data(callsign):
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
    print(f'{callsign},{nama},{provinsi},{masalaku},{tingkat},{status}')

def run():
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase+' ':
                for d in string.ascii_lowercase+' ':
                    try:
                        get_data('yb0'+a+b+c+d)
                    except:
                        pass  
                    
if __name__ == '__main__':
    run()
  
