---
Title: Charts

menus:
  main:
    weight: 1
    title: Project
layout: splash
classes: wide
---

#### Playground

<canvas id="myChart"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>

<script>
  timeJsonURL = 'https://raw.githubusercontent.com/galibhassan/sample-json/master/sampleDataForPowerGridFrequencyWebsitePlayground/time.json'
  frequencyJsonURL = 'https://raw.githubusercontent.com/galibhassan/sample-json/master/sampleDataForPowerGridFrequencyWebsitePlayground/frequency.json'

      async function getXYData() {
        const xData = await fetch(timeJsonURL).then((response) => response.json());
        const yData = await fetch(frequencyJsonURL).then((response) => response.json());

        return new Promise((resolve, reject) => {
          resolve({ xData, yData });
        });
      }

      function getRandData(n) {
        outputArr = [];
        for (let i = 0; i < n; i++) {
          scale = 100;
          outputArr.push(Math.random() * scale);
        }
        return new Promise((resolve, reject) => {
          resolve(outputArr);
        });
      }

      async function makePlot() {

        const { xData, yData } = await getXYData();

        var ctx = document.getElementById("myChart").getContext("2d");
        var chart = new Chart(ctx, {
          type: "line",
          data: {
            xLabels: xData,
            datasets: [
              {
                label: "Frequency in Hz",
                data: yData,
                fill: false,
                borderColor: "#00ADB5",
                borderWidth: 2,
                backgroundColor: "#00ADB5",
                pointRadius: 0,
                steppedLine: false,
                pointStyle: "circ",
                lineTension: 0,
              },
            ],
          },
          options: {
            scales: {
              yAxes: [
                {
                  scaleLabel: {
                    display: true,
                    labelString: 'Frequency (Hz)'
                  }
                },
                {
                  ticks: {
                    display: false,
                    beginAtZero: true,
                    fontColor: '#00ADB5'
                  },
                },
              ],
              xAxes: [
                {
                  ticks: {
                    display: true,
                  },
                },
              ],
            },
          },
        });
      }

      makePlot();
</script>
