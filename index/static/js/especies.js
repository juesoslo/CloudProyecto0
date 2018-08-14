$(document).ready(function (){

    $("#guardar").on("click", function(){
        if( $("#comentario").val() == "" ){
            alert("Debe ingresar alguna frase en el comentario");
            return false;
        }

    });

    $.ajax('../categorias/categoriasService').done(function(data){
        console.log(data);
        $.each(data, function(index, value){
            var select = $('<option value="' + value.id + '">').text(value.nombre);
            $('#CategoriasFiltro').append(select);
        });
        $('#CategoriasFiltro').on('change', function(){
            var val = $(this).val();
            if(val) {
                filterEspecies(val);
            }else {
                window.location.href = window.location.href;
            }
        });

    });

    function filterEspecies(value) {
        $.ajax('./especiesService/categoria/' + value).done(function(data) {
            $('#especiesListWrapper').html('');
            $.each(data, function(index, value){
                var li = $('<li class="rounded col-sm-3 especie">');
                var div = $('<div class="img-wrapper">');
                div.html('<a href="./' + value.id + '">' +
                            '<img src="' + value.foto + '" title="' + value.nombre + '"' +
                            'width="200" class="center img-responsive"/></a>');
                li.append(div);
                li.append('<strong class="col-sm-12 text-center d-block">' +
                        '<a href="./' + value.id + '">' + value.nombre + '</a>' +
                        '</strong>');
                $('#especiesListWrapper').append(li);
            });
            (function($){
                var options = {
                    valueNames: [ 'especie' ],
                    page: 8,
                    pagination: true
                  };
                var listObj = new List('especiesList', options);
            })(jQuery);
        });
    }

    $.ajax('./especiesService').done(function(data){
        $.each(data, function(index, value){
            var li = $('<li class="rounded col-sm-3 especie">');
            var div = $('<div class="img-wrapper">');
            div.html('<a href="./' + value.id + '">' +
                        '<img src="' + value.foto + '" title="' + value.nombre + '"' +
                        'width="200" class="center img-responsive"/></a>');
            li.append(div);
            li.append('<strong class="col-sm-12 text-center d-block">' +
					'<a href="./' + value.id + '">' + value.nombre + '</a>' +
				    '</strong>');
            $('#especiesListWrapper').append(li);
        });
        (function($){
            var options = {
                valueNames: [ 'especie' ],
                page: 8,
                pagination: true
              };
            var listObj = new List('especiesList', options);
        })(jQuery);
    });


});