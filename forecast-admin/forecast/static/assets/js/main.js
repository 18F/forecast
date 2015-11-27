
// Get the opportunities from the API
$.getJSON('/api/opportunities/?format=json', function (d){
  d.map(function (o){
    return $("#results").append("<li>" + o.description + "</li>")
  })
  console.log(d);
})
