# Chart.js

#javascript #web-programming #visualization

[Chart.js](https://github.com/chartjs/Chart.js) provides simple HTML5 charts using the `<canvas>` tag.

The project [react-chartjs-2](https://github.com/reactchartjs/react-chartjs-2) brings Chart.js to [[§ React]].

## Customize Axis Labels

```javascript
const options = {
  scales: {
    yAxis: {
      max: 100,
      ticks: {
        callback: (v) => `${v}%`,
      },
    },
    xAxis: {
      ticks: {
        callback: (i) => {
          const label = labels[i];
          return label.endsWith("00:00") ? label.split(" ")[0] : "";
        },
      },
    },
  },
};
```

## Customize Tooltip

Chart.js implements tooltips, legends via plugins. See [Tooltip Callbacks](https://www.chartjs.org/docs/latest/configuration/tooltip.html#tooltip-callbacks) to customize the tooltip labels.
