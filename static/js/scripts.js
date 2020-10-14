$(document).ready(function() {
            $('.datepicker').datepicker()
            $('.collapsible').collapsible();
            $(".button-collapse").sideNav();
            $('input#input_text, textarea#textarea2').characterCounter();
        })
        
      $(".datepicker").datepicker({
        selectMonths: true, 
        selectYears: 10, 
        today: "Today",
        clear: "Clear",
        close: "Ok",
        format: 'dd/mm/yyyy',
        closeOnSelect: false, 
      });

      document.getElementById("matfix").addEventListener("click", function(e) {
    e.stopPropagation();
    
});