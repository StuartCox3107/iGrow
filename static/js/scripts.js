$(document).ready(function() {
            $('.collapsible').collapsible();
            $(".button-collapse").sideNav();
            $('input#input_text, textarea#textarea2').characterCounter();
        })
        
      $(".datepicker").pickadate({
        selectMonths: true, 
        selectYears: 10, 
        today: "Today",
        clear: "Clear",
        close: "Ok",
        format: 'dd/mm/yyyy',
        closeOnSelect: true, 
      });

      document.getElementById("matfix").addEventListener("click", function(e) {
    e.stopPropagation();
    
});