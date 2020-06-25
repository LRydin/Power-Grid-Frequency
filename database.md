---
Title: Database

menus:
  main:
    weight: 1
    title: Database
layout: single
toc: true
toc_label: "Database"
toc_icon: "cog"
---

The target is to collect, process, and document all available power-grid frequency data publicly available and make it research ready.

# Publicly available data from TSOs

The links are direct downloads. Each is a zipped csv `.csv.zip` file. In [Power-Grid-Frequency-Data/](https://github.com/LRydin/Power-Grid-Frequency-Data/tree/master/) and each respective subfolder you can find a plot for each month of the processed data with some details of the data processing and the quality of the actual data.

_Data structure_

The data is structured in two columns: first column is a data-time format, e.g. `2017-01-01 00:00:00`. The second column is the frequency deviation from the reference in mHz, e.g. `44.006`.

To read the data directly in `python`, use `pandas` as

```python
import pandas as pd
df = pd.read_csv('path/to/germany_2017_01.csv.zip', index_col=0)
```

`pandas` is smart enough to unzip the `.csv` and read it.

<div class="downloadTablesContainerWrapper">
      <div id="downloadTablesContainer">
        <div class="downloadTablesHeader">
          Download Area
        </div>
      </div>
</div>

## Continental Europe

### Germany

{% include_relative /Data/Continental-Europe/Germany/readme.md %}

### France

{% include_relative /Data/Continental-Europe/France/readme.md %}

## Nordic Grid

### Finland

{% include_relative /Data/Nordic-Grid/Finland/readme.md %}

## National Grid

### Great Britain

{% include_relative /Data/National-Grid/Great-Britain/readme.md %}

# Research projects open data

## Power grid frequency data base

{% include_relative /Data/Research-Projects/Power-grid-frequency-data-base/readme.md %}

# Independent measurements

## Continental Europe

### Hungary

{% include_relative /Data/Independent-Measurements/Hungary/readme.md %}

<style>
      .downloadTablesContainerWrapper {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 80%;
        padding: 20px;
      }
      .downloadTablesHeader {
        background-color: #1e232c;
        border-radius: 5px;
        width: auto;
        text-align: center;
        padding: 10px;
      }

      #downloadTablesContainer {
        padding: 20px;
        box-shadow: 1px 1px 15px 1px rgba(0, 0, 0, 0.4);
        border-radius: 5px;
        transition: width 2s, height 4s;
      }

      .tab-link {
        display: inline-block;
        padding: 10px;
        cursor: pointer;
        background-color: rgb(68, 75, 88);
        border-radius: 5px;
        border-top-right-radius: 20px;
        margin: 2px;
        color: white;
      }
      .tab-content {
        display: none;
      }
      .tab-active {
        background-color: #00acb4;
      }
      .tab-not-active {
        background-color: rgb(68, 75, 88);
      }
      .realm {
        margin-top: 20px;
        border: 1px solid #1D2129;
        border-radius: 3px;
        transition: border 1.5s;
      }
      .realm:hover{
        border: 1px solid #00ABB3;
      }
      .realm-header {
        background: #2f3a45;
        padding: 10px;
        border-radius: 3px;
        box-shadow: 1px 1px 15px 1px rgba(0,0,0,0.3);
        /* border-top: 1px solid gray; */
      }
      .download-table{
        padding: 15px
      }
</style>

<script>
      // var sampleJsonEndpointURL = "https://raw.githubusercontent.com/galibhassan/power-grid-frequency-data-automation/automationStandalone/output/tableJsonOsf.json";
      var sampleJsonEndpointURL = '../json/tableJsonOsf.json'

      fetch(sampleJsonEndpointURL)
        .then((response) => response.json())
        .then((data) => {
          // data is structured as realm > country > year > month > file
          data.forEach((realm) => {
            getTabsfromJson(realm.name, realm.children, "downloadTablesContainer");
          });
        });
</script>

<script>
      function getTabsfromJson(headerString, jsonData, tableContainerId) {
        var tabLinks = document.createElement("ul");
        var tabContents = document.createElement("div");

        tabLinks.setAttribute("id", "tabList");
        var tableContainer = document.getElementById(tableContainerId);
        var realm = document.createElement("div");
        realm.classList.add("realm");
        var realmHeader = document.createElement("div");
        realmHeader.classList.add("realm-header");
        realmHeader.innerHTML = headerString;
        realm.appendChild(realmHeader);

        jsonData.forEach((entry, index) => {
          // creating tab-links links
          const currentTabLink = document.createElement("li");
          currentTabLink.innerHTML = entry.name;
          currentTabLink.classList.add("tab-link");
          currentTabLink.setAttribute("data-tableInfo", index);

          // creating tab-contents
          const currentTabContent = document.createElement("div");
          currentTabContent.appendChild(getTable(index, jsonData));
          currentTabContent.classList.add("tab-content");
          currentTabContent.setAttribute("data-tableInfo", index);

          tabLinks.appendChild(currentTabLink);
          tabContents.appendChild(currentTabContent);

          realm.appendChild(tabLinks);
          realm.appendChild(tabContents);

          tableContainer.appendChild(realm);

          // initial tab visibility
          tabContents.children[0].style.display = "block";
          tabLinks.children[0].classList.add("tab-active");

          // listening to click events
          currentTabLink.addEventListener("click", function (e) {
            Array.from(tabLinks.children).forEach((tablink) => {
              tablink.classList.add("tab-not-active");
            });

            e.currentTarget.classList.remove("tab-not-active");
            e.currentTarget.classList.add("tab-active");

            var clickedTableInfo = e.currentTarget.getAttribute("data-tableInfo");
            Array.from(tabContents.children)
              .slice()
              .reverse()
              .forEach((tabContent) => {
                var correspondingContentIndex = tabContent.getAttribute("data-tableInfo");
                if (clickedTableInfo === correspondingContentIndex) {
                  tabContent.style.display = "block";
                } else {
                  tabContent.style.display = "none";
                }
              });
          });
        });
      }

      function getTable(index, jsonData) {
        // making table
        var currentTable = document.createElement("table");
        var currentTBody = document.createElement("tbody");

        var years = jsonData[index].children;
        if (years.length === 0) {
          var noDataDiv = document.createElement("div");
          noDataDiv.innerHTML = "Data not yet available.";
          return noDataDiv;
        }
        years
          .slice()
          .reverse()
          .forEach((year) => {
            let currentTR = document.createElement("tr");
            let currentTD = document.createElement("td");

            currentTD.innerHTML = year.name;
            currentTR.appendChild(currentTD);

            var months = year.children;
            // var months12 =
            months.forEach((month, monthIndex) => {
              let currentTD = document.createElement("td");
              if (month.children.length === 0) {
                currentTD.innerHTML = getMonthName(month.name);
              } else {
                currentTD.appendChild(getDownloadLinkForMonth(month));
              }
              currentTR.appendChild(currentTD);
            });

            currentTBody.appendChild(currentTR);
          });

        currentTable.appendChild(currentTBody);

        return currentTable;
      }

      function getDownloadLinkForMonth(month) {
        var link = document.createElement("a");
        let downloadURL;
        month.children.forEach((child) => {
          if (child.name === "Data") {
            downloadURL = child.downloadURL;
          }
        });
        link.innerHTML = getMonthName(month.name);

        link.setAttribute("href", downloadURL);
        return link;
      }

      function getMonthName(monthString) {
        if (monthString === "01") return "Jan";
        else if (monthString === "02") return "Feb";
        else if (monthString === "03") return "Mar";
        else if (monthString === "04") return "Apr";
        else if (monthString === "05") return "May";
        else if (monthString === "06") return "Jun";
        else if (monthString === "07") return "Jul";
        else if (monthString === "08") return "Aug";
        else if (monthString === "09") return "Sep";
        else if (monthString === "10") return "Oct";
        else if (monthString === "11") return "Nov";
        else if (monthString === "12") return "Dec";
        else return monthString;
      }
</script>
