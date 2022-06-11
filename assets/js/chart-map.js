google.charts.load('current', {
  'packages':['geochart'],
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
  var data = google.visualization.arrayToDataTable(origDest);

  var options = {
    region: 'US',
    displayMode: 'regions',
    resolution: 'provinces',
	colorAxis: {colors: ['Tomato', 'DodgerBlue']},
	legend: 'none',
  };

  var chart = new google.visualization.GeoChart(document.getElementById('orderRoute'));

  chart.draw(data, options);
}

