function clean_form_zip_code() {
            //clean values form zip_code
            document.getElementById('address').value=("");
            document.getElementById('neighborhood').value=("");
            document.getElementById('city').value=("");
            document.getElementById('state').value=("");

    }

    function fun_callback(content) {
        if (!("erro" in content)) {
            //Update fields
            document.getElementById('address').value=(content.logradouro);
            document.getElementById('neighborhood').value=(content.bairro);
            document.getElementById('city').value=(content.localidade);
            document.getElementById('state').value=(content.uf);
        }
        else {
            clean_form_zip_code();
            alert("CEP não encontrado.");
            document.getElementById('zip_code').value=("");
        }
    }

    function search_zip_code(vl) {

        //new variable "zip_code" only digites.
        var zip_code = vl.replace(/\D/g, '');

        if (zip_code !== "") {

            // Regex validate zip_code
            var validate_zip_code = /^[0-9]{8}$/;


            if(validate_zip_code.test(zip_code)) {

                // Display fields with "..." while search api viacep.
                document.getElementById('address').value="...";
                document.getElementById('neighborhood').value="...";
                document.getElementById('city').value="...";
                document.getElementById('state').value="...";

                // Create element javascript.
                var script = document.createElement('script');

                // Sicronize with the callback.
                script.src = '//viacep.com.br/ws/'+ zip_code + '/json/?callback=fun_callback';

                // Insert script document and load content.
                document.body.appendChild(script);

            }
            else {
                //zip_code is invalid.
                clean_form_zip_code();
                alert("Formato de CEP inválido.");
            }
        }
        else {
            //zip_code without, clean form.
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


