function message_error(obj) {
  var html = "";
  if (typeof obj === "object") {
    //si es un objeto, lo itero
    html = '<ul style="text-align: Left; ">';
    $.each(obj, function (key, value) {
      html += "<li>" + key + ": " + value + "</li>";
    });
    html += "</ul>";
  } else {
    //sino, puede ser un string, solo se lo paso
    html = "<p>" + obj + "</p>";
  }

  Swal.fire({
    title: "¡Error!",
    //ya no le paso un "text", sino un "html" porque construi uno para los errores
    html: html,
    icon: "error",
  });
}

function submit_with_ajax(url,title,content, parameters,callback) {
  $.confirm({
    theme: "material", //tipo de tema
    title: title, //titulo de la alerta
    icon: "fa fa-info", //icono de fontawesome
    content: content, //contenido de la alerta
    columnClass: "medium", //tamaño, tambien puede ser small
    typeAnimated: true,
    cancelButtonClass: "btn-primary",
    draggable: true,
    dragWindowBorder: false, //estos 4 anteriores es para los efectos, en su doc lo explica
    buttons: {
      //le paso los botones
      //que tipo de boton y sus propiedades
      info: {
        text: "Si", //el texto
        btnClass: "btn-green", //la clase
        //la función a realizar
        action: function () {
          $.ajax({
            //url:'{% url 'crm:categoria_create' %}',
            //de esta forma obtengo la url actual
            url: url, //se la paso por la función
            type: "POST",
            data: parameters, //se lo paso por la función
            dataType: "json",
            processData: false,
            contentType:false //por defecto estos 2 estan en true, y modifican los datos que le pase, pero con el FormData ya lo hago y le digo que no procese esos datos
          })
            .done(function (data) {
              //Este metodo se ejecuta si la peticion se realiza de manera exitosa
              if (!data.hasOwnProperty("error")) {
                callback(); //Como no solo la voy a utilizar una vez, ya dependiendo de la necesidad, ejecuto una función que le pase

                //pregunto si el data NO tiene errores
                //lo regreso a la lista
                //location.href = "{{list_url}}";
                //le retorno false para que salga del proceso
                return false;
              }
              message_error(data.error);
            })
            .fail(function (jqXHR, textStatus, errorThrown) {
              //Este se ejecuta si la peticion tiene algun error
              alert(`${textStatus} : ${errorThrown}`);
            })
            .always(function () {
              //este se ejecuta siempre
            });
        },
      },
      danger: {
        text: "No",
        btnClass: "btn-red",
        action: function () {},
      },
    },
  });
};

// Configurar el token CSRF globalmente para todas las solicitudes AJAX
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", $("input[name=csrfmiddlewaretoken]").val());
        }
    }
});