$(function(e) {
	
	//______Basic Data Table
	$('#basic-datatable').DataTable({
		language: {
			searchPlaceholder: 'Buscar...',
			sSearch: '',
		}
	});

	//______Input fields Data Table
	$('#input-fields').DataTable({
		language: {
			searchPlaceholder: 'Buscar...',
			sSearch: '',
		}
	});
	

	//______Basic Data Table
	$('#responsive-datatable').DataTable({
		responsive: true,
		language: {
			searchPlaceholder: 'Buscar...',
			sSearch: '',
		}
	});

	//______File-Export Data Table
	var table = $('#file-datatable').DataTable({
		buttons: [ 'copiar', 'excel', 'pdf', 'colvis' ],
		responsive: true,
		language: {
			searchPlaceholder: 'Buscar...',
			sSearch: '',
		}
	});
	table.buttons().container()
	.appendTo( '#file-datatable_wrapper .col-md-6:eq(0)' );	

	//______Delete Data Table
	var table = $('#delete-datatable').DataTable({
		language: {
			searchPlaceholder: 'Buscar...',
			sSearch: '',
		}
	}); 
    $('#delete-datatable tbody').on( 'click', 'tr', function () {
        if ( $(this).hasClass('selected') ) {
            $(this).removeClass('selected');
        }
        else {
            table.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
        }
    } );
    $('#button').click( function () {
        table.row('.selected').remove().draw( false );
    } );
	

	//______Select2 
	$('.select2').select2({
		minimumResultsForSearch: Infinity,
		width:"auto",
	});


});