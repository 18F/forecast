var fullResults;
var data;

_initializeFilters();
_loadGSAdata()


/**
 * Load the GSA data
 **/
function _loadGSAdata() {
  // This is going to load the GSA data
  $.getJSON('/api/opportunities/?format=json')
    .done(function (d) {
      d["agency"] = "gsa";
      _loadFilterOptions(d);

      $("#loading").remove();
      var options = {
          page: 100,
          item: 'opportunity-row',
          valueNames: ['description','office','naics']
      };
      var listObj = new List('results', options, d);
      data = d;
      // Create Filter events
      _createFilterEvents(['award_status','naics','place_of_performance_state'],
        listObj);

      _initDetails(listObj);

      _loadOtherAgencies(['state','ed'], listObj);

  }).then(function () {
    fullResults = $("#opportunities").clone()
  })
}

/**
 *Initializes the More/Fewer Filters
 **/
function _initializeFilters() {
  // init
  $("#award-amount-dropdown").parent().toggle();
  $("#estimated_fiscal_year_quarter-dropdown").parent().toggle();
  $("#more-filters").on('click', function(e){
    $("#more-filters").text("Fewer Filters");
    $("#award-amount-dropdown").parent().toggle();
    $("#estimated_fiscal_year_quarter-dropdown").parent().toggle();
  })
}

/**
 *Initializes the More/Fewer Filters
 **/

function _loadFilterOptions(d) {
  data = d;
  _getOptions(d, 'award_status');
  _getOptions(d, 'naics');
  _getOptions(d, 'place_of_performance_state');
}

/**
 * Load the Data into the Filters
 **/
function _getOptions(d, field) {
  var opt = _.uniq(_.pluck(_.sortBy(d, field), field));
  $.each(opt, function(key, value) {
     $('#' + field + '-dropdown')
         .append($("<option></option>")
         .attr("value",value)
         .text(value));
  });
}

/**
 * Initializes event for Filters
 **/
function _createFilterEvents(filters, listObj) {

  _.each(filters, function(d) {

    var dropdown = "#" + d + "-dropdown";
    $(dropdown).change(function (){
      listObj.filter(function(item) {
        var val = $(dropdown).val();
        if (val === "all") {
          return true;
        }
        else {
          return (item.values()[d] === val ? true : false);
        }
      })
    })
  })
}


/**
 * Initializes event for Filters
 **/
function _loadOtherAgencies (agencies, listObj) {
  _.each(agencies, function (agency){
    $.getJSON('/static/data/fy16' + agency + '.json').done(function (d){
      d['agency'] = agency;
      listObj.add(d);
    })
  })
  var dropdown = "#agency-dropdown";
  $(dropdown).change(function (){
    listObj.filter(function (item) {
      var val = $(dropdown).val();
      if (val === "gsa") {
        return (item.values()["agency"] ? false : true);
      }
      return (item.values()["agency"] === val ? true : false);
    })
  })
}


// function _initDetails(listObj) {
//   _.each(listObj.items,
// }
