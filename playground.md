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

<style> 
      #chartContainer {
        border-radius: 5px;
        position: relative;
      }
      #legendDivContainer {
        color: #929294;
        margin: 10px;
        position: absolute;
        top: 20px;
        left: 20px;
        background-color: #343a46;
        padding: 10px;
        box-shadow: 1px 1px 15px 1px rgba(0, 0, 0, 0.3);
        border-radius: 5px;
        opacity: 0.7;
        font-size: 0.7rem;
      }
      .legendDiv {
        display: flex;
        width: 300px;
        justify-content: space-around;
        
      }
      .freqLegend {
        width: 10px;
        border-radius: 3px;
        height: 10px;
        background: tomato;
      }

</style>

<div id="chartContainer">
  <div id="legendDivContainer">
    <div class="legendDiv">
      <div id="maxFreqLegend" class="freqLegend"></div>
      <div>Max Frequency</div>
      <div id="maxFreq"></div>
    </div>
    <div class="legendDiv">
      <div id="minFreqLegend" class="freqLegend"></div>
      <div>Min Frequency</div>
      <div id="minFreq"></div>
    </div>
  </div>
  <canvas id="myChart"></canvas>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>

<script>
      timeJsonURL =
        "https://raw.githubusercontent.com/galibhassan/sample-json/master/sampleDataForPowerGridFrequencyWebsitePlayground/time.json";
      frequencyJsonURL =
        "https://raw.githubusercontent.com/galibhassan/sample-json/master/sampleDataForPowerGridFrequencyWebsitePlayground/frequency.json";

      const MAX_COLOR = "tomato";
      const MIN_COLOR = "#042e82";
      const DEFAULT_COLOR = "#00ADB5";

      document.getElementById("maxFreqLegend").style.backgroundColor = MAX_COLOR;
      document.getElementById("minFreqLegend").style.backgroundColor = MIN_COLOR;

      async function getXYData() {
        const xData = await fetch(timeJsonURL).then((response) => response.json());
        const yData = await fetch(frequencyJsonURL).then((response) => response.json());

        return new Promise((resolve, reject) => {
          resolve({ xData, yData });
        });
      }

      async function makePlot() {
        const { xData, yData } = await getXYData();

        const maxFrequency = yData.reduce(function (a, b) {
          return Math.max(a, b);
        });

        const minFrequency = yData.reduce(function (a, b) {
          return Math.min(a, b);
        });

        document.getElementById("maxFreq").innerHTML = maxFrequency;
        document.getElementById("minFreq").innerHTML = minFrequency;

        function customRadius(context) {
          let index = context.dataIndex;
          let value = context.dataset.data[index];
          if (value === maxFrequency) {
            return 8;
          } else if (value === minFrequency) {
            return 8;
          } else {
            return 0;
          }
        }

        function customBackgroundColor(context) {
          let index = context.dataIndex;
          let value = context.dataset.data[index];
          if (value === maxFrequency) {
            return MAX_COLOR;
          } else if (value === minFrequency) {
            return MIN_COLOR;
          } else {
            return DEFAULT_COLOR;
          }
        }

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
                backgroundColor: customBackgroundColor,
                steppedLine: false,
                pointStyle: "circ",
                lineTension: 0,
              },
            ],
          },
          options: {
            legend: {
              display: false,
            },
            elements: {
              point: {
                radius: customRadius,
                display: true,
              },
            },
            animation: {
              animateScale: true,
              animateRotate: true,
            },
            scales: {
              yAxes: [
                {
                  scaleLabel: {
                    display: true,
                    labelString: "Frequency (Hz)",
                    fontSize: 20,
                  },
                },
                {
                  ticks: {
                    display: false,
                    beginAtZero: true,
                    fontColor: "#00ADB5",
                  },
                },
              ],
              xAxes: [
                {
                  scaleLabel: {
                    display: true,
                    labelString: "Time",
                    fontSize: 20,
                  },
                  ticks: {
                    display: true,
                    autoSkip: true,
                    maxTicksLimit: 10,
                  },
                },
              ],
            }
          },
        });
      }

      makePlot();
    </script>
