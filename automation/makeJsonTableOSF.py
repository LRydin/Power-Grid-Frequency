import json

repoStructureJsonPath = "./output/pathsAndLinksFromOsfApi.json"
OUTPUT_JSON_PATH = './output/tableJsonOsf.json'


def getRepoStructure(repoStructureJsonPath):
    tableJson = []
    repoStructureFile = open(repoStructureJsonPath)
    repoStructure = json.load(repoStructureFile)

    found = 0
    for i in range(len(repoStructure)):
        branch = repoStructure[i]
        found += 1
        currentDownloadURL = branch['url']
        pushToTableJson(branch['path'], tableJson, currentDownloadURL, found)

    return tableJson


# declaration
currentRealm = ''
currentCountry = ''
currentYear = ''
currentMonth = ''
currentFileName = ''


def pushToTableJson(apiPath, tableJson, downloadURL, found):
    global currentRealm
    global currentCountry
    global currentYear
    global currentMonth
    global currentFileName

    arrayfiedApiPath = apiPath.split('/')

    indexOffset = 2  # since for OSF ['', 'Data', 'Realm', 'Country', ...etc]
    realm = arrayfiedApiPath[0 + indexOffset]
    country = arrayfiedApiPath[1 + indexOffset]
    year = arrayfiedApiPath[2 + indexOffset]
    month = arrayfiedApiPath[3 + indexOffset]
    fileName = arrayfiedApiPath[4 + indexOffset]

    if found == 1:
        tableJson.append(getNewRealm(realm, country, year, month, downloadURL))
    else:
        if currentRealm != realm:
            tableJson.append(getNewRealm(
                realm, country, year, month, downloadURL))
        elif currentRealm == realm and currentCountry != country:
            for i in range(len(tableJson)):
                _realm = tableJson[i]
                if _realm["name"] == currentRealm:
                    _realm['children'].append(getNewCountry(
                        country, year, month, downloadURL))

        elif currentRealm == realm and currentCountry == country and currentYear != year:
            for i in range(len(tableJson)):
                _realm = tableJson[i]
                if _realm["name"] == currentRealm:
                    for j in range(len(_realm['children'])):
                        _country = _realm['children'][j]
                        if _country["name"] == currentCountry:
                            _country['children'].append(
                                getNewYear(year, month, downloadURL))

        elif currentRealm == realm and currentCountry == country and currentYear == year and currentMonth != month:
            for i in range(len(tableJson)):
                _realm = tableJson[i]
                if _realm["name"] == currentRealm:
                    for j in range(len(_realm['children'])):
                        _country = _realm['children'][j]
                        if _country["name"] == currentCountry:
                            for k in range(len(_country['children'])):
                                _year = _country['children'][k]
                                if _year["name"] == currentYear:
                                    _year["children"].append(
                                        getNewMonth(month, downloadURL))

    currentRealm = realm
    currentCountry = country
    currentYear = year
    currentMonth = month
    currentFileName = fileName

# ---------------


def getNewRealm(realm, country, year, month, downloadURL):
    return {
        "name": realm,
        "type": "folder",
        "tabSystem": True,
        "children": [getNewCountry(country, year, month, downloadURL)],
    }


def getNewCountry(country, year, month, downloadURL):
    return {
        "name": country,
        "type": "folder",
        "tabSystem": True,
        "children": [getNewYear(year, month, downloadURL)],
    }


def getNewYear(year, month, downloadURL):
    return {
        "name": year,
        "type": "folder",
        "children": [getNewMonth(month, downloadURL)],
    }


def getNewMonth(month, downloadURL):
    return {
        "name": month,
        "type": "folder",
        "children": [
            {
                "name": "Data",
                "type": "file",
                "downloadURL": downloadURL,
            },
        ],
    }

# sort all months


def getMonthSortedTableJsonOSF(unsortedTableJsonOSF):
    for i in range(len(unsortedTableJsonOSF)):
        # cu stands for current unsorted
        cu_realm = unsortedTableJsonOSF[i]

        for j in range(len(cu_realm['children'])):
            cu_country = cu_realm['children'][j]

            for k in range(len(cu_country["children"])):
                cu_year = cu_country['children'][k]
                cu_months = cu_year['children']

                # we have to sort _year['children']
                sorted_months = sorted(cu_months, key=sorter_months)

                # replace unsorted part by sorted part
                unsortedTableJsonOSF[i]['children'][j]['children'][k]['children'] = sorted_months

    return unsortedTableJsonOSF


def sorter_months(monthDict):
    return int(monthDict["name"])


def getTableJsonWithMissingMonths(tableJsonWithoutMissingMonths):
    months12 = ["01", "02", "03", "04", "05",
                "06", "07", "08", "09", "10", "11", "12"]
    for i in range(len(tableJsonWithoutMissingMonths)):
        # cu stands for current
        cu_realm = tableJsonWithoutMissingMonths[i]

        for j in range(len(cu_realm['children'])):
            cu_country = cu_realm['children'][j]

            for k in range(len(cu_country["children"])):
                cu_year = cu_country['children'][k]
                cu_monthsDict = cu_year['children']

                cu_monthsStrList = []
                for h in range(len(cu_monthsDict)):
                    cu_monthsStrList.append(cu_monthsDict[h]["name"])

                currentMissingMonths = []
                for m in range(len(months12)):

                    if(months12[m] in cu_monthsStrList):
                        pass
                    else:
                        currentMissingMonths.append(months12[m])

                for n in range(len(currentMissingMonths)):
                    cu_monthsDict.append({
                        "name": currentMissingMonths[n],
                        "children": []
                    })

    return tableJsonWithoutMissingMonths


pathsAndLinksOSF = getRepoStructure(repoStructureJsonPath)
tableJsonOSF = getTableJsonWithMissingMonths(
    getMonthSortedTableJsonOSF(pathsAndLinksOSF))

outputJson = open(OUTPUT_JSON_PATH, 'w+')
json.dump(tableJsonOSF, outputJson, indent=2)
outputJson.close()
