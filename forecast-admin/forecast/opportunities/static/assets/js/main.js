
// Get the opportunities from the API
$.getJSON('/api/opportunities/?format=json', function (d){
  $("#results").html('');
  d.map(function (o){




    return $("#results").append(createRow(o))
  })
  console.log(d);
})


function createRow(o) {

  var res = '<div class="opportunity-row"><div class="office">' + o.office + '</div><div class="description">' + o.description + '</div><div class="usa-grid"> <div class="usa-width-one-half"><p><span class="detail-label">Award Status: </span>' + o.award_status + '</p><p><span class="detail-label">Place of Performance: </span>' + o.place_of_performance_city + ", " + o.place_of_performance_state + '</p><p><span class="detail-label">NAICS Code: </span>' + o.naics + '</p></div><div class="usa-width-one-half"><p><span class="detail-label">Estimated Award Date: </span>FY ' + o.estimated_fiscal_year + '- Quarter' +  o.estimated_fiscal_year_quarter + '</p><p><span class="detail-label">Category: </span>' + o.socioeconomic + '</p> <p><a href="">View Details </a></p></div></div></div>'
  return res;
}
