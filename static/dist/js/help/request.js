/**
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-10-15 00:59:34
 * @modify date 2021-10-15 12:00:56
 * @desc [description]
 */

$(document).ready(function () {



    /**
     * função que vai bloquiar o curso caso a sua classe não seja ensino medio
     */

    $('.ajax_classeFrequencia').click(function () {

        var classe = $('.ajax_classeFrequencia').val();
        if (classe < 10) {
            $(".ajax_curso").attr("disabled", "disabled");
        } else {
            $(".ajax_curso").removeAttr("disabled", "disabled");

        }
    });

    /**
     * função que vai retorna todas os os municipios em função do id da provincia
     */
    $('.ajax_provincia').click(function () {
        $.ajax({
            url: '/ajax/retorna_municipio/',
            type: 'POST',
            data: JSON.stringify({ 'id': $('.ajax_provincia').val() }),
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            success: function (data) {
                var municipio = document.getElementById("id_municipio");

                var cont = 1;
                while (municipio.options.length) {
                    municipio.remove(0);
                }
                for (let k = 0; k < data.muncipios.length; k++) {
                    var resp = data.muncipios[k];
                    var novos = ""

                    novos = new Option(resp[1], resp[0]);
                    municipio.options.add(novos)
                    cont = cont + 1;
                }

            },
            error: function () {
                console.log('erro na busca do municipio')
            }
        });


        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }


    });






});

$(function () {
    $('.maiuscula').keyup(function () {
        this.value = this.value.toLocaleUpperCase();
    });
});