function baixarPdf(salvar){
    var ids = getAllIds();
    var divconteudo = []
    var divs_secoes = document.getElementsByClassName('conteudoCaptura');
    var textoInicial = tinymce.get('cabecalho').getContent();
    if(divs_secoes.length>0)
      divs_secoes[0].childNodes[0]

    for (let index = 0; index < divs_secoes.length; index++) {
      var div_conteudo = document.createElement('div');
      div_conteudo.setAttribute('class','w-100')
      var filhos = divs_secoes[index].childNodes;
      if(filhos[0].tagName == 'DIV'){
        var titulo = tinymce.get(filhos[0].childNodes[1].id).getContent();
        div_conteudo.innerHTML = titulo;
      }

      for (let j = 1; j < filhos.length; j++) {
        var elemento = filhos[j];
        if(elemento.id.match(/mce_.*/i)!=null){
          var conteudo = tinymce.get(elemento.id).getContent();
          div_conteudo.innerHTML = conteudo;
          divconteudo.push((divs_secoes[index].childNodes[0]).outerHTML)
          divconteudo.push(conteudo)
        }
       
      }
    }
    var stringpdf = "";
    divconteudo.forEach(element => {
      stringpdf += element
    });
    var textoHeader = tinymce.get("cabecalho").getContent();
    stringpdf = textoHeader + stringpdf
    console.log(stringpdf)
    var dataPDf = {};
    dataPDf['contentPDF'] = stringpdf;
    dataPDf = JSON.stringify(dataPDf);
    $.ajax({
      type: 'POST',
      url: '/construcao/toPDF',
      data: dataPDf,
      contentType: 'application/json; charset=utf-8',
      cache: false,
      success: function(data){
        var file = document.createElement('a');
        file.style.display='none';
        file.href = "data:application/pdf;base64,"+data;
        file.download = "filename.pdf";
        file.click();
      },
      error: function () {
        console.log('error')
      },
    });
  }