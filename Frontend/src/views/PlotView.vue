<template>
  <div id = "forScatter">
    <ScatterChart />
  </div>
</template>
<script>
import { defineComponent, h, PropType } from 'vue'
import { Scatter } from 'vue-chartjs'
import asia from '../continent/asia.json'
import northamerica from '../continent/northamerica.json'
import southamerica from '../continent/southamerica.json'
import europe from '../continent/europe.json'
import oceania from '../continent/oceania.json'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Plugin
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
)
export default defineComponent({
  name: 'ScatterChart',
  components: {
    Scatter
  },
  props: {
    chartId: {
      type: String,
      default: 'scatter-chart'
    },
    width: {
      type: Number,
      default: 800
    },
    height: {
      type: Number,
      default: 800
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object ,
      default: () => {}
    }
  },
  setup(props) {
    const chartData = {
      datasets: [
        {
          label: '아시아',
          fill: true,
          borderColor: '#DC6093',
          backgroundColor: '#DC6093',
          data: asia,
          pointRadius: 5
        },
        {
          label: '북아메리카',
          fill: true,
          borderColor: '#FFC341',
          backgroundColor: '#FFC341',
          data: northamerica,
          pointRadius: 5
        },
        {
          label: '남아메리카',
          fill: true,
          borderColor: '#7B75B4',
          backgroundColor: '#7B75B4',
          data: southamerica,
          pointRadius: 5
        },
        {
          label: '유럽',
          fill: true,
          borderColor: '#3BE0CB',
          backgroundColor: '#3BE0CB',
          data: europe,
          pointRadius: 5
        },
        {
          label: '오세아니아',
          fill: true,
          borderColor: '#9B3E63',
          backgroundColor: '#9B3E63',
          data: oceania,
          pointRadius: 5
        },
      ]
    }

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend : {
          labels:{
            font: {
              size: 25
            }
          }
          },
        title: {
                display: false,
                font: {
                  size: 30
                },
                text: 't-SNE Visualization of University',
                padding: 100,
              },
      tooltip: {
            caretSize: 8,
            caretPadding: 3,
            // boxPadding: 5,
            intersect: true,
            usePointStyle: true,
            callbacks: {
                    labelPointStyle: function(context) {
                        return {
                            pointStyle: 'triangle',
                            rotation: 0
                        };
                    },
                    label: function(context) {
                        return context.raw.name
                    }
            }
      }
        },
      scales: {
        x: {
          grid: {
            display: false
          },
          ticks: {
            display: false
          }
        },
        y: {
          grid: {
            display: false
          },
          ticks: {
            display: false
          }
        }
      },
      onClick: function(point){
          location.href='https://kuabroad.herokuapp.com/detailresult?name=' + point.chart.tooltip.dataPoints[0].raw.name.replace(' ','+');
          console.log(point.chart.tooltip.dataPoints[0].raw.name);
        },
      layout: {
            padding: {
                top: 100,
                left: 100,
                right: 100,
                bottom: 50
            }
        }
      
    }
    return () =>
      h(Scatter, {
        chartData,
        chartOptions,
        chartId: props.chartId,
        width: props.width,
        height: props.height,
        cssClasses: props.cssClasses,
        styles: props.styles
       })
  }
})
</script>
<style scoped>
.container {
  overflow: auto;
  width: 1440px;
  height: 900px;
  display: flex;
  flex-direction: column;
}
.intro {
  z-index: 2;
  display: flex;
  flex-direction: column;
  margin-left : 10%;
  margin-top: 3%;
}
.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 540px;
  height: 72px;
  font-size: 45px;
  letter-spacing: 0;
  flex-shrink: 1;
}
.intro_msg2 {
  color:gba(153.00000607967377, 153.00000607967377, 153.00000607967377, 1);
  width: 420px;
  height: 30px;
  font-size: 22.101093292236328px;
  letter-spacing: 0;
}
</style>