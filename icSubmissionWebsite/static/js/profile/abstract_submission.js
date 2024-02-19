var affilations = 0;
var authors = 0;
var errors = 0;
$(document).ready(function () {
  $(".affilation").each(function (index, element) {
    if (parseInt(element.id) > affilations) affilations = parseInt(element.id);
  });

  $(".author").each(function (index, element) {
    if (parseInt(element.id) > authors) authors = parseInt(element.id);
  });
});
function swap_windows(element) {
  id = element.id;
  $(".form-window").hide();

  $("#" + id + ".form-window").show();
}

function add_affilation(element) {
  elem = $(`
    <div class="affilation section" id="${affilations + 1}">
    <div class="affilation-head">
      <h3>${affilations + 1}</h3>
      <button onclick="delete_affilation(this)" id="remove_affilation" class="button">x</button>
    </div>

    <div class="section flex-row">
      <div class="flex-column">
        <h4>Affilation</h4>
      </div>
      <div class="flex-column">
        <input
          class="input-text"
          type="text"
          name="company_or_institution"
          
        />
      </div>
    </div>

    <div class="section flex-row">
      <div class="flex-column">
        <h4>City/Suburb/Town</h4>
      </div>
      <div class="flex-column">
        <input
          class="input-text"
          type="text"
          name="city"
       
        />
      </div>
    </div>

    <div class="section flex-row">
      <div class="flex-column">
        <h4>Country</h4>
      </div>
      <div class="flex-column">
        <input
          class="input-text"
          type="text"
          name="country"
       
        />
      </div>
    </div>

    <div class="section flex-row">
      <div class="flex-column">
        <h4>State</h4>
      </div>
      <div class="flex-column">
        <input class="input-text" name="state" type="text" />
      </div>
    </div>
  </div>
    `);
  $("#affilations").append(elem);
  affilations += 1;
}

function delete_affilation(element) {
  $(element).parent().parent().remove();
}

function delete_author(element) {
  $(element).parent().parent().remove();
}
function add_author(element) {
  elem = $(`<div class="author section" id="${authors + 1}">
    <div class="author-head">
      <h3>${authors + 1}</h3>
      <button
        id="remove_author"
        onclick="delete_author(this)"
        class="button"
      >
        x
      </button>
    </div>
    
    <div class="section flex-row">
      <div class="flex-column">
        <h4>Title</h4>
      </div>
      <div class="flex-column">
        <input
          class="input-text"
          type="text"

          name="title"

        />
      </div>
    </div>
    
    <div class="section flex-row">
      <div class="flex-column">
        <h4>First Name</h4>
      </div>
      <div class="flex-column">
        <input
          class="input-text"
          type="text"

          name="first_name"

        />
      </div>
    </div>
    
    <div class="section flex-row">
      <div class="flex-column">
        <h4>Last Name</h4>
      </div>
      <div class="flex-column">
        <input
          class="input-text"
          type="text"

          name="last_name"

        />
      </div>
    </div>
    
    <div class="section flex-row">
      <div class="flex-column">
        <h4>Presenter</h4>
      </div>
      <div class="flex-column">
        <input
          type="checkbox"
          name="presenter"

        />
      </div>
    </div>
    
    <div class="section flex-row">
      <div class="flex-column">
        <h4>Organization</h4>
      </div>
      <div class="flex-column">
        <input
          class="input-text"
          type="text"

          name="organization"

        />
      </div>
    </div>
    
    <div class="section flex-row">
      <div class="flex-column">
        <h4>Affilation</h4>
      </div>
      <div class="flex-column">
        <input
          class="input-text"
          type="text"
          name="affilation"

        />
      </div>
    </div>
    </div>
      `);
  $("#authors").append(elem);
  authors += 1;
}
function add_error(text) {
  errors += 1;
  error = $(`
  <span class="error">${text}</span>
    `);
  $("#errors").append(error);
}
function check_for_errors() {
  $("#errors").empty();
  errors = 0;
  if ($("#abstract_title").val() == null || $("#abstract_title").val() == "") {
    add_error("Title Required");
  }

  if (
    $("#abstract_presentation_type").val() == null ||
    $("#abstract_presentation_type").val() == ""
  ) {
    add_error("Presentation Type Required");
  }
  if ($("#topic_text").val() == null || $("#topic_text").val() == "") {
    add_error("Topic Required");
  }
  $(".affilation").each(function (index, element) {
    affilation = element.id;
    if (
      $(this).find('input[name="company_or_institution"]').val() == null ||
      $(this).find('input[name="company_or_institution"]').val() == ""
    ) {
      add_error("Affilation Required for Affilation " + author);
    }

    if (
      $(this).find('input[name="city"]').val() == null ||
      $(this).find('input[name="city"]').val() == ""
    ) {
      add_error("City Required for Affilation " + author);
    }
    if (
      $(this).find('input[name="country"]').val() == null ||
      $(this).find('input[name="country"]').val() == ""
    ) {
      add_error("Country Required for Affilation " + author);
    }
  });
  $(".author").each(function (index, element) {
    author = element.id;
    if (
      $(this).find('input[name="title"]').val() == null ||
      $(this).find('input[name="title"]').val() == ""
    ) {
      add_error("Title Required for Author " + author);
    }

    if (
      $(this).find('input[name="first_name"]').val() == null ||
      $(this).find('input[name="first_name"]').val() == ""
    ) {
      add_error("First Name Required for Author " + author);
    }

    if (
      $(this).find('input[name="last_name"]').val() == null ||
      $(this).find('input[name="last_name"]').val() == ""
    ) {
      add_error("Last Name Required for Author " + author);
    }

    if (
      $(this).find('input[name="organization"]').val() == null ||
      $(this).find('input[name="organization"]').val() == ""
    ) {
      add_error("Organization Required for Author " + author);
    }

    if (
      $(this).find('input[name="affilation"]').val() == null ||
      $(this).find('input[name="affilation"]').val() == ""
    ) {
      add_error("Affilation Required for Author " + author);
    }
  });
  if ($("#bio").val() == null || $("#bio").val() == "") {
    add_error("Biography Required");
  }

  if ($("#abstract_text").val() == null || $("#abstract_text").val() == "") {
    add_error("Abstract Required");
  }
}
function get_affilation(id) {
  affilation = $("#" + id + ".affilation");
  affilation_data = {
    affilation: affilation.find('input[name="company_or_institution"]').val(),
    city: affilation.find('input[name="city"]').val(),
    country: affilation.find('input[name="country"]').val(),
    state: affilation.find('input[name="state"]').val(),
  };
  return affilation_data;
}
function get_authors() {
  authors_data = [];

  $(".author").each(function (index, element) {
    affilation_id = $(this).find('input[name="affilation"]').val();
    author = {
      title: $(this).find('input[name="title"]').val(),
      first_name: $(this).find('input[name="first_name"]').val(),
      last_name: $(this).find('input[name="last_name"]').val(),
      organization: $(this).find('input[name="organization"]').val(),
      affilation: get_affilation(affilation_id),
      is_presenter: document.getElementsByName("presenter")[0].checked,
    };
    authors_data.push(author);
  });
  return authors_data;
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function post(url, data) {
  const csrfToken = getCookie("csrftoken");
  $.ajax({
    type: "POST",
    headers: {
      "X-CSRFToken": csrfToken,
    },
    async: false,
    dataType: "json",
    data: JSON.stringify(data),
    url: url,
    success: function (response) {
      return response;
    },
    error: function (response) {
      return response;
    },
  });
}
function submit_abstract() {
  data = {
    title: $("#abstract_title").val(),
    presentation_type: $("#abstract_presentation_type").val(),
    topic: $("#topic_text").val(),
    authors: get_authors(),
    bio: $("#bio").val(),
    abstract: $("#abstract_text").val(),
  };
  response = post("", data);
  console.log(response);

  window.location(response.url);
}
