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
        <input class="input-text" name="country" type="text" />
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

function submit_abstract() {
  //   if (errors != 0) {
  //     alert("There are multiple errors, please check Review section");
  //     return;
  //   }
}
