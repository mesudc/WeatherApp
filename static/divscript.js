$(document).ready(function(){
  $('#content div').hide();
  $('#About-Me').fadeIn('slow');
  $('.btn').click(function() {
    $('#content div').hide();
    var target = '#' + $(this).data('target');
    $(target).fadeIn('slow');
  })
});