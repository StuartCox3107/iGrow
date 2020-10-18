$(document).ready(function () {
  $(".collapsible").collapsible();
  $(".sidenav").sidenav();
  $("input#input_text, textarea#textarea2").characterCounter();
});

$('.datepicker').datepicker({
        format: "dd, mmmm yyyy",
        yearRange: 10,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });


