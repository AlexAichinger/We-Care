console.log("hey")
$(document).ready(function() {
  $('#authenticate-facebook').on("click", function(evt) {
    controllers.authenticate_facebook();
  });
  $('#submit').on("click", function(evt) {
    var facebook = $('#facebook').val();
    var twitter = $('#twitter').val();
    var instagram = $('#instagram').val();
    controllers.submit(facebook, twitter, instagram);
  });
});

var controllers = {
  authenticate_facebook: function() {
    $.get({
      url: '/authenticate-facebook'
    }.done(function(data) {
      if (data.success) {

      } else {

      }
    }).fail(function(data) {

    }));
  },
  submit: function(facebook, twitter, instagram) {
    $.post({
      url: '/submit',
      data: [facebook, twitter, instagram]
    }.done(function(data) {

    }).fail(function(data) {

    }));
  }
};
