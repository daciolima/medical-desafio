
    function clean_form_zip_code() {
            //Limpa valores do formulário de zip_code.
            document.getElementById('address').value=("");
            document.getElementById('neighborhood').value=("");
            document.getElementById('city').value=("");
            document.getElementById('state').value=("");

    }

    function meu_callback(conteudo) {
        if (!("erro" in conteudo)) {
            //Atualiza os campos com os valores.
            document.getElementById('address').value=(conteudo.logradouro);
            document.getElementById('neighborhood').value=(conteudo.bairro);
            document.getElementById('city').value=(conteudo.localidade);
            document.getElementById('state').value=(conteudo.uf);
        } //end if.
        else {
            //CEP não Encontrado.
            clean_form_zip_code();
            alert("CEP não encontrado.");
            document.getElementById('zip_code').value=("");
        }
    }

    function search_zip_code(vl) {

        //Nova variável "zip_code" somente com dígitos.
        var zip_code = vl.replace(/\D/g, '');

        //Verifica se campo zip_code possui valor informado.
        if (zip_code !== "") {

            //Expressão regular para validate o CEP.
            var validate_zip_code = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validate_zip_code.test(zip_code)) {

                //Preenche os campos com "..." enquanto consulta webservice.
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

function formatar(mascara, documento){
  var i = documento.value.length;
  var saida = mascara.substring(0,1);
  var texto = mascara.substring(i);

  if (texto.substring(0,1) != saida){
            documento.value += texto.substring(0,1);
  }

}
