/**
 *Initializes list.js
 **/
var paginationTopOptions = {
  name: 'paginationTop',
  paginationClass: 'paginationTop',
  innerWindow: 5,
  outerWinder: 1
};
var paginationBottomOptions = {
  name: 'paginationBottom',
  paginationClass: 'paginationBottom',
  innerWindow: 5,
  outerWinder: 1
};
var listOptions = {
  valueNames: [
    'award_status',
    'place_of_performance_state',
    'naics',
    'award_amount',
    'estimated_fiscal_year_quarter',
    'description',
    'funding_agency',
    'estimated_fiscal_year',
    'place_of_performance_city',
    'contract_type',
    'office',
    'dollar_value_min',
    'dollar_value_max'
  ],
  page: 25,
  plugins: [
    ListPagination(paginationTopOptions),
    ListPagination(paginationBottomOptions)
  ]
};
var listObj = new List('opportunities', listOptions);
var data = {};
var queries = {};
var urlStem = "api/opportunities/?format=csv";

/**
 *Initializes the More/Fewer Filters
 **/
$("#dollar-value-min").parent().toggle();
$("#dollar-value-max").parent().toggle();
$("#estimated_fiscal_year_quarter-dropdown").parent().toggle();
$("#more-filters").on('click', function(e){
  $("#more-filters").text("Fewer Filters");
  $("#dollar-value-min").parent().toggle();
  $("#dollar-value-max").parent().toggle();
  $("#estimated_fiscal_year_quarter-dropdown").parent().toggle();
});

// A function to check whether an item matches any active filters
var filterCheck = function (item, queries) {
  shouldReturn = true;
  _.each(_.keys(queries), function (key) {
    if (key === 'description') {
      if (item.values()[key].indexOf(queries[key]) < 0) {
        shouldReturn = false;
        return shouldReturn;
      }
    } else if (key === 'dollar_value_min') {
      if (parseInt(item.values()[key]) < parseInt(queries[key])) {
        shouldReturn = false;
        return shouldReturn;
      }
    } else if (key === 'dollar_value_max') {
      if (parseInt(item.values()[key]) > parseInt(queries[key])) {
        shouldReturn = false;
        return shouldReturn;
      }
    } else {
      if (item.values()[key] != queries[key]) {
        shouldReturn = false;
        return shouldReturn;
      }
    }
  });
  return shouldReturn;
};

$(document).ready(function () {
  /**
   * Load the Data into the Filters
   **/
  _.each(listOptions.valueNames, function (name) {

    // Create an array for each filterable element
    data[name] = [];
    _.each(listObj.items, function(item) {
      data[name].push(item.values()[name]);
    });

    // This jQuery won't work because list.js removes the items that aren't
    // on the first page of results
    // $('.'+name).each( function (index) {
    //   data[name].push($(this).text());
    // })

    // Find unique values and add them as options in dropdowns
    var opt = _.sortBy(_.uniq(data[name]));
    $.each(opt, function(key, value) {
      $('#' + name + '-dropdown')
        .append($("<option></option>")
        .attr("value",value)
        .text(value));
    });

    // Add the filtering action to each dropdown
    var dropdown = "#" + name + "-dropdown";
    $(dropdown).change(function (){
      var value = $(dropdown).val();
      urlQuery = "";
      queries = _.omit(queries, name);
      if (value != "all") {
        queries[name] = value;
      }
      _.each(_.keys(queries), function(key) {
        urlQuery += "&"+key+"="+queries[key];
      });
      $(".download-spreadsheet>a").attr("href",urlStem+urlQuery);
      listObj.filter(function(item) {
        return (filterCheck(item, queries));
      });
    });
  });

  // Search within list of opportunities
  $(".search").keyup(function () {
    urlQuery = "";
    if ($(this).val().length > 0) {
      queries.description = $(this).val();
    } else {
      queries = _.omit(queries, "description");
    }
    _.each(_.keys(queries), function(key) {
      urlQuery += "&"+key+"="+queries[key];
    });
    $(".download-spreadsheet>a").attr("href",urlStem+urlQuery);
    listObj.filter(function(item) {
      return (filterCheck(item, queries));
    });
  });

  // Disable search while it doesn't actually query the DB
  $(".search").keypress(function (event) {
    if (event.which == '13') {
      event.preventDefault();
    }
  });

  $("#dollar-value-min").keyup(function (event) {
    var value = $(this).val();
    urlQuery = "";
    // queries = _.omit(queries, name);
    queries.dollar_value_min = value;
    _.each(_.keys(queries), function(key) {
      urlQuery += "&"+key+"="+queries[key];
    });
    $(".download-spreadsheet>a").attr("href",urlStem+urlQuery);
    listObj.filter(function(item) {
      return (filterCheck(item, queries));
    });
  });

  $("#dollar-value-max").keyup(function (event) {
    var value = $(this).val();
    urlQuery = "";
    // queries = _.omit(queries, name);
    queries.dollar_value_max = value;
    _.each(_.keys(queries), function(key) {
      urlQuery += "&"+key+"="+queries[key];
    });
    $(".download-spreadsheet>a").attr("href",urlStem+urlQuery);
    listObj.filter(function(item) {
      return (filterCheck(item, queries));
    });
  });
});
