// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("earningsByDriver");
const myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: driverNames,
    datasets: [{
      data: driverGross,
      backgroundColor: ['#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#42d4f4', '#f032e6', '#bfef45', '#fabed4', '#469990', '#dcbeff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#a9a9a9', '#ffffff', '#000000']
    }],
  },
  options: {
    legend: {
        position: 'left'
    },
    maintainAspectRatio: false,
    responsive: true,
  }
});

