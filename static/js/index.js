$(document).ready(function() {
  /*
  $('#authenticate-facebook').on("click", function(evt) {
    controllers.authenticate_facebook();
  });
  */
  $('#gauge').css('display', 'none');
  $('#load').css('display', 'none');
  $('#submit').on("click", function(evt) {
    //var facebook = $('#facebook').val();
    var twitter = $('#twitter').val();
    var instagram = $('#instagram').val();
    controllers.submit(twitter, instagram);
  });
});

var controllers = {
  authenticate_facebook: function() {
    $.get({
      url: '/authenticate-facebook'
    }).done(function(data) {
      if (data.success) {
        console.log(data.url);
      } else {

      }
    }).fail(function(data) {

    });
  },
  submit: function(twitter, instagram) {
    $.post({
      url: "/process",
      data: twitter
    }).done(function(data) {
      display.displayValue(data);
    }).fail(function(data) {

    });
  }
};

var display = {
  displayValue: function(value) {
    $('#start_content').css('display', 'none');
    $('#load').css('display', 'block');
    setTimeout(function() {
      $('#load').css('display', 'none');
      $('#gauge').css('display', 'block');
      var g = new JustGage({
        id: "gauge",
        value: value * 100,
        min: -100,
        max: 100,
        title: "Happiness Level"
      });
    }, 3000);
  }
};
