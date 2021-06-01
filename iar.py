from selenium import webdriver

def getIARInfo(callsign):
    callsign = str.upper(callsign)
    data = {}
    driver = webdriver.Chrome()
    driver.get("https://iar-ikrap.postel.go.id/")
    element = driver.find_element_by_name("Iar[callsign]")
    element.send_keys(callsign)
    driver.find_element_by_xpath("//button[@class='btn btn-white btn-raised btn-fab btn-round']").click()
    tds = driver.find_elements_by_tag_name('td')

    for i,td in enumerate(tds):
        if td.text:
            print(i,td.text)

    data[tds[3].text] = tds[5].text
    data[tds[9].text] = tds[11].text
    data[tds[12].text] = tds[14].text
    data[tds[15].text] = tds[17].text
    data[tds[18].text] = tds[20].text
    data[tds[21].text] = tds[23].text

    res = ""
    for k,v in data.items():
        res = res + k + ": " + v +"\n"

    driver.close()
    driver.quit()
    if len(res) < 10:
        res = "Not found."
    return(res)


if __name__ == '__main__':
    print(getIARInfo('YC0DMS'))
