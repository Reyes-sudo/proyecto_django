$(function(){
    $("#data").DataTable({
      responsive: true,
      autoWidth: false,
      destroy: true,
      deferRender: true,
      ajax: {
        url: window.location.pathnam,
        type: "POST",
        data: { action: "searchdata" }, // parametros
        dataSrc: "",
      },
      columns: [
        { data: "id" },
        { data: "nombre" },
        { data: "descripcion" },
        { data: "id" },
      ],
      columnDefs: [
        {
          targets: [-1],
          class: "text-center",
          orderable: false,
          render: function (data, type, row) {
            var buttons =
              '<a  href="/crm/categoria/update/' +
              row.id +
              '/" class="btn btn-primary btn-s btn-flat"><i class="fas fa-edit"></i></a> ';
            buttons +=
              '<a href="/crm/categoria/delete/' +
              row.id +
              '/" type="button" class="btn btn-danger btn-s btn-flat"><i class="fas fa-trash-alt"></i></a>';
            return buttons;
          },
        },
      ],
      initComplete: function (settings, json) {},
    });
})