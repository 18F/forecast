
// This is going to load the GSA data
$.getJSON('/api/opportunities/?format=json')
  .done(function (d) {

    var options = {
        item: 'opportunity-row',
        valueNames: ['description','naics']
    };
    new List('results', options, d);
})
