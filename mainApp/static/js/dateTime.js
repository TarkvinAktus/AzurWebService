$(function() {
    $('input[name="daterange"]').daterangepicker({
      locale: {
        cancelLabel: 'Clear'
      },
      
      autoUpdateInput: false,
    });

    
    $('input[name="daterange"]').on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
  });

  $('input[name="daterange"]').on('cancel.daterangepicker', function(ev, picker) {
      $(this).val('');
  });
  });


  