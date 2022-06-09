google.charts.load('current', {
  'packages':['geochart'],
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
  var data = google.visualization.arrayToDataTable(stateGross);

  var options = {
    region: 'US',
    displayMode: 'regions',
    resolution: 'provinces',
  };

  var chart = new google.visualization.GeoChart(document.getElementById('earningsByState'));

  chart.draw(data, options);
}
