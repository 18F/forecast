$(function(){

  var throttle = function throttle(fn, threshhold, scope) {
    threshhold || (threshhold = 250);
    var last,
        deferTimer;
    return function () {
      var context = scope || this;

      var now = +new Date,
          args = arguments;
      if (last && now < last + threshhold) {
        // hold on to it
        clearTimeout(deferTimer);
        deferTimer = setTimeout(function () {
          last = now;
          fn.apply(context, args);
        }, threshhold);
      } else {
        last = now;
        fn.apply(context, args);
      }
    };
  };

  var header = document.querySelector('header'),
    drawer = document.querySelector('drawer');

  function setDrawerTop () {
    var newHeight = header.getBoundingClientRect().bottom;
    drawer.style.top = newHeight + 'px';
  };

  // initialize height of drawer path
  setTimeout(setDrawerTop, 0);

  window.addEventListener('resize', throttle(setDrawerTop, 150, window));
});
