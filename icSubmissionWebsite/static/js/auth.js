function ValidateEmail(email) {
  const validRegex =
    /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
  return email.match(validRegex);
}
function getCookie(cookieName) {
  let cookie = {};
  document.cookie.split(";").forEach(function (el) {
    let [key, value] = el.split("=");
    cookie[key.trim()] = value;
  });
  return cookie[cookieName];
}
function submitRegisterForm(element) {
  const form = document.forms["register_form"];
  const data = new FormData(form);

  const formProps = Object.fromEntries(data);

  for (const value of Object.values(formProps)) {
    if (value == "" || value == null) {
      alert("Please fill the form");
      return;
    }
  }

  if (formProps.email != formProps.confirm_email) {
    alert("Emails don't match");
    return;
  }
  if (!ValidateEmail(formProps.email)) {
    alert("Wrong email pattern");
    return;
  }
  $.ajax({
    type: "POST",
    headers: { "X-CSRFToken": getCookie("csrftoken") },
    async: false,
    data: JSON.stringify({ email: formProps.email }),
    url: "auth/create_pending_user",
    success: function (response) {
      if (response.message == "user already exists")
        alert("User already exists");
    },
    error: function (response) {
      console.log(response);
    },
  });
}
