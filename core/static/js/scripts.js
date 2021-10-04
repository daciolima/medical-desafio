// Clear value form zipcode
function clean_form_zip_code() {
    document.getElementById('address').value=("");
    document.getElementById('neighborhood').value=("");
    document.getElementById('city').value=("");
    document.getElementById('state').value=("
}

// update field with values
function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        document.getElementById('address').value=(conteudo.logradouro);
        document.getElementById('neighborhood').value=(conteudo.bairro);
        document.getElementById('city').value=(conteudo.localidade);
        document.getElementById('state').value=(conteudo.uf);
    }
    else {
        clean_form_zip_code();
        alert("CEP não encontrado.");
        document.getElementById('zip_code').value=("");
    }
}

// new variable zip_code. Only with digites
function search_zip_code(vl) {
    var zip_code = vl.replace(/\D/g, '');

    if (zip_code !== "") {

        //regex validate zip_code.
        var validate_zip_code = /^[0-9]{8}$/;

        //validate zip_code format.
        if(validate_zip_code.test(zip_code)) {

            // moment with "..." while search API
            document.getElementById('address').value="...";
            document.getElementById('neighborhood').value="...";
            document.getElementById('city').value="...";
            document.getElementById('state').value="...";

            //Cria um elemento javascript.
            var script = document.createElement('script');

            //Sincroniza com o callback.
            script.src = '//viacep.com.br/ws/'+ zip_code + '/json/?callback=meu_callback';

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

        } //end if.
        else {
            //zip_code é inválido.
            clean_form_zip_code();
            alert("Formato de CEP inválido.");
        }
    } //end if.
    else {
        //zip_code sem valor, limpa formulário.
        clean_form_zip_code();
    }
}

function formate(mask, document){
  var i = document.value.length;
  var output = mask.substring(0,1);
  var text = mask.substring(i);

  if (text.substring(0,1) != output){
            document.value += text.substring(0,1);
  }

}


$(document).ready(function() {
$("input#id_phone")
        .mask("(99) 9 9999-999?9")
        .focusout(function (event) {
            var target, phone, element;
            target = (event.currentTarget) ? event.currentTarget : event.srcElement;
            phone = target.value.replace(/\D/g, '');
            element = $(target);
            element.unmask();
            if(phone.length > 10) {
                element.mask("(99) 9 9999-999?9");
            } else {
                element.mask("(99) 9 9999-999?9");
            }
        });
});
