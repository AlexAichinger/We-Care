$(document).ready(function() {
  $('#value').css("visibility", "hidden");
  $('#authenticate-facebook').on("click", function(evt) {
    controllers.authenticate_facebook();
  });
  $('#submit').on("click", function(evt) {
    var facebook = $('#facebook').val();
    var twitter = $('#twitter').val();
    var instagram = $('#instagram').val();
    controllers.submit(facebook, twitter, instagram);
  });
  display.displayValue(500);
});

var controllers = {
  authenticate_facebook: function() {
    $.get({
      url: '/authenticate-facebook'
    }).done(function(data) {
      if (data.success) {
        display.displayValue(9);
        console.log(data.url);
      } else {

      }
    }).fail(function(data) {

    });
  },
  submit: function(facebook, twitter, instagram) {
    $.post({
      url: '/submit',
      data: [facebook, twitter, instagram]
    }).done(function(data) {
      if (data.success) {
        display.displayValue(500);
      } else {

      }
    }).fail(function(data) {

    });
  }
};

var display = {
  scrollToBottom: function() {
    window.scrollTo(0, document.body.scrollHeight);
  },
  displayValue: function(value) {
    var element = $('#value');
    $('#value span').html(value);
    element.css("visibility", "visible");
    element.addClass('valign-wrapper');
    display.scrollToBottom();
  }
};
