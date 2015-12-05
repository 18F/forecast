var fullResults;
// This is going to load the GSA data
$.getJSON('/api/opportunities/?format=json')
  .then(function (d) {
    $("#loading").remove();
    var options = {
        item: 'opportunity-row',
        indexAsync: true,
        valueNames: ['description','naics']
    };
    new List('results', options, d);

}).then(function () {
  fullResults = $("#opportunities").clone()
})
