$(document).ready(function() {
  /*
  $('#authenticate-facebook').on("click", function(evt) {
    controllers.authenticate_facebook();
  });
  */
  $('#submit').on("click", function(evt) {
    //var facebook = $('#facebook').val();
    var twitter = $('#twitter').val();
    var instagram = $('#instagram').val();
    controllers.submit(twitter, instagram);
  });
  display.displayValue(0);
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
  submit: function(twitter, instagram) {
    $.post({
      url: "/getNumeric.py",
      data: twitter
    }).done(function(data) {
      display.displayValue(data);
    }).fail(function(data) {

    });
  }
};

var display = {
  scrollToBottom: function() {
    window.scrollTo(0, document.body.scrollHeight);
  },
  displayValue: function(value) {
    var g = new JustGage({
      id: "gauge",
      value: value * 100,
      min: -100,
      max: 100,
      title: "levelOfDepression"
    });
    display.scrollToBottom();
  }
};
