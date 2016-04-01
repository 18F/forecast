
/**
 *Initializes list.js
 **/

var opportunitiesPerPage = 10;

var paginationBottomOptions = {
  name: 'paginationBottom',
  paginationClass: 'pagination-bottom',
  innerWindow: 2,
  outerWinder: 1
};

var listOptions = {
  valueNames: [
    'agency',
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
    'dollar_value_max',
    'socioeconomic'
  ],
  page: opportunitiesPerPage,
  plugins: [
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
$("#more-filters").hide();
$("#toggle-filters").on('click', function(e) {
    var filters = $("#more-filters");
    if (filters.is(":visible")) {
        filters.hide();
        $("#toggle-filters").text("More Filters");
    } else {
        filters.show();
        $("#toggle-filters").text("Fewer Filters");
    }
});

// A function to check whether an item matches any active filters
var filterCheck = function (item, queries) {
  shouldReturn = true;
  _.each(_.keys(queries), function (key) {
    if (key === 'description') {
      if (item.values()[key].search(new RegExp(queries[key], "i")) < 0) {
        shouldReturn = false;
        return shouldReturn;
      }
    } else if (key === 'dollar_value_min') {
      var value = item.values()[key].replace('$','').replace(',','');
      if (parseInt(value) < parseInt(queries[key])) {
        shouldReturn = false;
        return shouldReturn;
      }
    } else if (key === 'dollar_value_max') {
      var value = item.values()[key].replace('$','').replace(',','');
      if (parseInt(value) > parseInt(queries[key])) {
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

var startOpportunities = function(opportunityContainer, pageContainer) {
  var getOpportunityRowNode = function(o) {
    var currency = function(value) {
      var fixed = Number(value).toFixed(2);
      var whole = fixed.substr(0, fixed.length - 3);
      var i = whole.length - 3;
      while(i > 0) {
        whole = whole.substr(0, i) + ',' + whole.substr(i);
        i -= 3;
      }
      return '$' + whole + fixed.substr(-3);
    }

    if(!o._node) {
      var html = '<li class="opportunity-row">' +
      '  <p class="office">' +
      '    <span class="agency">' + o.agency + '</span>';
      if(o.office) {
        html += '    <span class="h5">|</span>' +
        '    <span> ' + o.office + ' </span>';
      }
      html += '  </p>' +
      '  <p class="description">' + o.description + ' (#' + o.id + ')</p>' +
      '  <div class="details">' +
      '    <div class="row">' +
      '      <div class="usa-width-one-half">' +
      '        <p class="detail-row">' +
      '          <span class="detail-label">Award Status: </span><span class="award_status detail-field">' + (o.award_status || "–") + '</span>' +
      '        </p>' +
      '        <p class="detail-row">' +
      '          <span class="detail-label">Place of Performance: </span>' +
      '          <spam class="detail-field">' + o.place_of_performance_city + ', <span class="place_of_performance_state">' + o.place_of_performance_state + '</span>' +
      '          </span>' +
      '        </p>' +
      '        <p class="detail-row">' +
      '          <span class="detail-label">NAICS Code: </span><span class="detail-field naics">' + (o.naics || "–") + '</span>' +
      '        </p>' +
      '        <p class="detail-row">' +
      '          <span class="detail-label">Estimated Award Date: </span>' +
      '          <span class="detail-field">FY ' + o.estimated_fiscal_year + ' - <span class="estimated_fiscal_year_quarter">' + o.estimated_fiscal_year_quarter + ' Quarter</span></span>' +
      '        </p>' +
      '      </div>' +
      '      <div class="usa-width-one-half">' +
      '        <p class="detail-row">' +
      '          <span class="detail-label">Minimum Value: </span>' +
      '          <span class="detail-field dollar_value_min">' + currency(o.dollar_value_min) + '</span>' +
      '        </p>' +
      '        <p class="detail-row">' +
      '          <span class="detail-label">Maximum Value: </span>' +
      '          <span class="detail-field dollar_value_max">' + currency(o.dollar_value_max) + '</span>' +
      '        </p>' +
      '        <p class="detail-row">' +
      '          <span class="detail-label">Contract Type: </span>' +
      '          <span class="detail-field contract_type">' + (o.contract_type || "-") + '</span>' +
      '        </p>' +
      '        <p class="detail-row">' +
      '          <span class="detail-label">Socioeconomic Category: </span>' +
      '          <span class="detail-field socioeconomic">' + (o.socioeconomic || "-") + '</span>' +
      '        </p>' +
      '        <p class="detail-row opportunity-details"><a class="detail-label" href="/details/' + o.id + '">View Details </a></p>' +
      '      </div>' +
      '    </div>' +
      '  </div>' +
      '</li>';
      o._node = html;
    }
    return o._node;
  }

  var _opportunityContainer = $('#opportunities .list');
  var _pageContainer = $('.pagination-bottom');
  var _status = $('.opportunity-pagination_status');
  var _list = [ ];
  var _page = 1;
  var _totalOpps = 0;
  var _totalPages = -1;

  var getPageGoToer = function(pageNumber) {
    return function() {
      goToPage(pageNumber);
    };
  };

  var updateStatus = function() {
    _status.empty();
    if(_list.length > 0) {
      var start = ((_page - 1) * opportunitiesPerPage) + 1;
      var end = start + 9;
      _status.append(start + ' – ' + end + ' of ' + _totalOpps + ' opportunities');

    } else {
      _status.append('No opportunities found.');
    }
  };

  var updatePageCounter = function() {
    _pageContainer.empty();

    if(_page > 3) {
      _pageContainer.append($('<li class="disabled">...</li>'));
    }

    var min = Math.max(1, _page - 2);
    var max = Math.min(_page + 2, _totalPages);
    for(var i = min; i <= max; i++) {
      var link = $('<a class="page" href="javascript:">' + i + '</a>');
      if(i !== _page) {
        link.click(getPageGoToer(i));
      }

      var li = $('<li class="' + (i === _page ? 'active' : '') + '">');
      li.append(link);
      _pageContainer.append(li);
    }

    if(_page < _totalPages - 3) {
      _pageContainer.append($('<li class="disabled">...</li>'));
    }
    updateStatus();
  };

  var goToPage = function(pageNumber) {
    if(_list.length < (pageNumber * opportunitiesPerPage)) {
      $.get('api/opportunities/?format=json&limit=' + opportunitiesPerPage + '&offset=' + ((pageNumber - 1) * opportunitiesPerPage), function(data) {
        _list = _list.concat(data.results);
        if(_totalPages < 0) {
          _totalOpps = data.count;
          _totalPages = Math.floor(data.count / opportunitiesPerPage);
        }
        goToPage(pageNumber);
      });
    } else {
      _opportunityContainer.empty();
      var start = (pageNumber - 1) * opportunitiesPerPage;
      var nodes = _list.slice(start, start + opportunitiesPerPage).map(getOpportunityRowNode);
      _opportunityContainer.append(nodes);
      _page = pageNumber;
      updatePageCounter();
    }
  }

  goToPage(1);
  return {

  };
};

$(document).ready(function() {

  // Update current page (.opportunity-pagination_status)
  $paginationStatus = $('.opportunity-pagination_status');

  var renderPageStatus = function renderPageStatus() {
    if (listObj.matchingItems.length) {
      var pageLimit = listObj.i + opportunitiesPerPage - 1,
        totalOpportunities = listObj.matchingItems.length;

      var lastOpportunity = (pageLimit > totalOpportunities)
        ? totalOpportunities
        : pageLimit;

      var currentOpportunities = listObj.i + ' – ' + lastOpportunity;

      var opportunitiesText = (totalOpportunities === 1)
        ? ' opportunity'
        : ' opportunities';
      var status = currentOpportunities + ' of ' + totalOpportunities + opportunitiesText;
      $paginationStatus.text(status);
    } else {
      $paginationStatus.text('No opportunities found.');
    }
  }

  startOpportunities();

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
    $(".button-download_wrapper a").attr("href",urlStem+urlQuery);
    listObj.filter(function(item) {
      return (filterCheck(item, queries));
    });

    renderPageStatus();
  });

  // // Search within list of opportunities
  $(".search").keyup(function () {
    listObj.search($(this).val());
    renderPageStatus();
  });


  // Disable search while it doesn't actually query the DB
  $(".search").keypress(function (event) {
    if (event.which == '13') {
      event.preventDefault();
    }
    renderPageStatus();
  });

  $("#dollar-value-min").keyup(function (event) {
    var value = $(this).val();
    urlQuery = "";
    // queries = _.omit(queries, name);
    queries.dollar_value_min = value;
    _.each(_.keys(queries), function(key) {
      urlQuery += "&"+key+"="+queries[key];
    });
    $(".button-download_wrapper a").attr("href",urlStem+urlQuery);
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
    $(".button-download_wrapper a").attr("href",urlStem+urlQuery);
    listObj.filter(function(item) {
      return (filterCheck(item, queries));
    });
  });

  renderPageStatus();

  // listen for list to update
  listObj.on('updated', function() {
    renderPageStatus();
  });

});
