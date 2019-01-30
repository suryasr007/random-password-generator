$(document).ready(function() {
  function parseExcludeChars(excludechars) {
    //Define regex
    var uppercase = new RegExp("^[A-Z]");
    var lowercase = new RegExp("^[a-z]");
    var number = new RegExp("^[0-9]");
    var special = new RegExp("^[a-zA-Z0-9_]*$");

    var toBeExcluded = {
      excludeuchars: "",
      excludelchars: "",
      excludenumbers: "",
      excludeschars: ""
    };

    for (var i = 0; i < excludechars.length; i++) {
      if (uppercase.test(excludechars[i])) {
        toBeExcluded.excludeuchars += excludechars[i];
      } else if (lowercase.test(excludechars[i])) {
        toBeExcluded.excludelchars += excludechars[i];
      } else if (number.test(excludechars[i])) {
        toBeExcluded.excludenumbers += excludechars[i];
      } else if (!special.test(excludechars[i])) {
        toBeExcluded.excludeschars += excludechars[i];
      }
    }
    return $.param(toBeExcluded);
  }

  // Normal password. (Request to /api/v1/generate)
  $("#normal-btn").click(function() {
    var request = "./api/v1/generate?";
    request += $("#normal-form").serialize();
    request += "&" + parseExcludeChars($("#normal-form #excludechars").val());
    $.get(request, function(data, status) {
      $("#normal-pwd").val(data.password);
    });
  });

  // nonduplicate password. (Request to /api/v1/nonduplicate)
  $("#nonduplicate-btn").click(function() {
    var request = "./api/v1/nonduplicate?";
    request += $("#nonduplicate-form").serialize();
    $.get(request, function(data, status) {
      $("#nonduplicate-pwd").val(data.password);
    });
  });

  // password from given characters. (Request to /api/v1/shuffle)
  $("#shuffle-btn").click(function() {

    if($("#shuffle-form .form-group #char-input").val() == "") {
      $("#shuffle-error-empty").removeClass("d-none");
    } else {
      $("#shuffle-error-empty").addClass("d-none");
    }

    var request = "./api/v1/shuffle?";
    request += $("#shuffle-form").serialize();
    $.get(request, function(data, status) {
      $("#shuffle-pwd").val(data.password);
    });
  });
});
