var fullResults;
// This is going to load the GSA data
$.getJSON('/api/opportunities/?format=json')
  .done(function (d) {
    $("#loading").remove();
    var options = {
        item: 'opportunity-row',
        valueNames: ['description','naics']
    };
    new List('results', options, d);

}).then(function () {
  fullResults = $("#opportunities").clone()  
})
