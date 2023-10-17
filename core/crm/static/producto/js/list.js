$(function () {
    const data_table=$('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "nombre"},
            {"data": "categoria.nombre"},
            {"data": "imagen"},
            {"data": "stock"},
            {"data": "precio"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="'+data+'" class="img-fluid d-block mx-auto" style="width: 20px; height: 20px;">';
                }
            },
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if(data>0){
                        return '<span class="badge badge-success">'+data+'</span'
                    }

                    return '<span class="badge badge-danger">'+data+'</span'
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$'+parseFloat(data).toFixed(2);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons =
                      '<a href="/crm/producto/update/' +
                      row.id +
                      '/" class="btn btn-primary btn-s btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/crm/producto/delete/' + row.id + '/" type="button" class="btn btn-danger btn-s btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
      initComplete: function (settings, json) {
        }
    });
});