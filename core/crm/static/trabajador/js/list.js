$(function () {
  const data_table = $("#data").DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: "POST",
      data: {
        action: "searchdata",
      },
      dataSrc: "",
    },
    columns: [
      { data: "id" },
      { data: "nombres" },
      { data: "apellidos" },
      { data: "edad" },
      { data: "direccion" },
      { data: "correo" },
      { data: "curriculum_vitae" },
      { data: "sede.nombre" },
      { data: "id" },
    ],
    columnDefs: [
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          var buttons =
            '<a href="/crm/trabajador/update/' +
            row.id +
            '/" class="btn btn-primary btn-s btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons +=
            '<a href="/crm/trabajador/delete/' +
            row.id +
            '/" type="button" class="btn btn-danger btn-s btn-flat"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) {},
  });
});
