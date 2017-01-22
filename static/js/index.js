$(document).ready(function() {
  /*
  $('#authenticate-facebook').on("click", function(evt) {
    controllers.authenticate_facebook();
  });
  */
  $('#load').css('display', 'none');
  $('#gauge').css('display', 'none');
  $('#submit').on("click", function(evt) {
    //var facebook = $('#facebook').val();
    var twitter = $('#twitter').val();
    var instagram = $('#instagram').val();
    controllers.submit(twitter, instagram);
  });
  display.displayValue(0.32);
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
      url: "/get-numeric",
      data: twitter
    }).done(function(data) {
      console.log(data);
      display.displayValue(data);
    }).fail(function(data) {

    });
  }
};

var display = {
  displayValue: function(value) {
    $('#initial-content').css('display', 'none');
    $('#load').css('display', 'block');
    setTimeout(function() {
      $('#load').css('display', 'none');
      $('#gauge').css('display', 'block');
      var g = new JustGage({
        id: "gauge",
        value: value * 100,
        min: -100,
        max: 100,
        title: "Depression Indicator"
      });
    }, 3000);
  }
};
