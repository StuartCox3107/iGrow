$(document).ready(function () {
  $(".collapsible").collapsible();
  $(".sidenav").sidenav();
  $(".datepicker").datepicker({
        format: "dd, mmm yyyy",
        yearRange: 10,
        showClearBtn: true,
        i18n: {
        done: "Select"
        }
    });
  $("input#input_text, textarea#textarea2").characterCounter();
});




