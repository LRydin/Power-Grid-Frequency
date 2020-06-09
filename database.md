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

<style>
      #downloadTablesContainer{

        border-radius: 5px;
        padding: 15px;
        box-shadow: 1px 1px 15px 1px rgba(0,0,0,0.4)
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

</style>

The target is to collect, process, and document all available power-grid frequency data publicly available and make it research ready.

# Publicly available data

## Continental Europe

<div id="downloadTablesContainer"></div>

### Germany

{% include_relative /Data/Continental-Europe/Germany/readme.md %}

<script>
 var sampleJsonEndpointURL = "https://raw.githubusercontent.com/galibhassan/sample-json/master/sample_data.json";

fetch(sampleJsonEndpointURL)
.then((response) => response.json())
.then((data) => {
        getTabsfromJson(data, "downloadTablesContainer");
} );


</script>

<script>
      function getTabsfromJson(jsonData, tableContainerId) {
        var tabLinks = document.createElement("ul");
        var tabContents = document.createElement("div");

        tabLinks.setAttribute("id", "tabList");

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

          var tableContainer = document.getElementById(tableContainerId);
          tableContainer.appendChild(tabLinks);
          tableContainer.appendChild(tabContents);

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
            months.forEach((month, monthIndex) => {
              let currentTD = document.createElement("td");
              // currentTD.innerHTML = getMonthName(month.name, monthIndex);
              currentTD.appendChild(getDownloadLinkForMonth(month));
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
        link.innerHTML = month.name;

        link.setAttribute("href", downloadURL);
        return link;
      }

      /*       function getMonthName(monthName, monthIndex) {
        if (monthIndex === 0 && monthName === "Jan") return monthName;
        if (monthIndex === 1 && monthName === "Feb") return monthName;
        if (monthIndex === 2 && monthName === "Mar") return monthName;
        if (monthIndex === 3 && monthName === "Apr") return monthName;
        if (monthIndex === 4 && monthName === "May") return monthName;
        if (monthIndex === 5 && monthName === "Jun") return monthName;
        if (monthIndex === 6 && monthName === "Jul") return monthName;
        if (monthIndex === 7 && monthName === "Aug") return monthName;
        if (monthIndex === 8 && monthName === "Sep") return monthName;
        if (monthIndex === 9 && monthName === "Oct") return monthName;
        if (monthIndex === 10 && monthName === "Nov") return monthName;
        if (monthIndex === 11 && monthName === "Dec") return monthName;
      } */

    </script>
