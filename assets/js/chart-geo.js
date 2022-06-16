google.charts.load('current', {
  'packages':['geochart'],
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
  var data0 = google.visualization.arrayToDataTable(originGross);
  var data1 = google.visualization.arrayToDataTable(destinationGross);

  var options = {
    region: 'US',
    displayMode: 'regions',
    resolution: 'metros',
  };

  var chart0 = new google.visualization.GeoChart(document.getElementById('earningsByOrigin'));
  var chart1 = new google.visualization.GeoChart(document.getElementById('earningsByDestination'));

  chart0.draw(data0, options);
  chart1.draw(data1, options);
}
