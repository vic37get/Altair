function getHeader(){
  return tinymce.get("cabecalho").getContent(); 
}

function getAllIds(){
    var lista_textAreas = document.getElementsByTagName('textarea');
    lista_textAreas = Array.prototype.slice.call(lista_textAreas);
    lista_textAreas = lista_textAreas.filter(filterTinyMce);
    lista_textAreas = lista_textAreas.map(mapTinyMce);
    return lista_textAreas
  }

  function getAllContent(){
    var divconteudo = []
    var divs_secoes = document.getElementsByClassName('conteudoCaptura');

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
    var doc = new jsPDF();
    doc.fromHTML(stringpdf, // page element which you want to print as PDF
    15,
    15, 
    {
      'width': 170
    },
    function(a) 
    {
      var file = document.getElementById("embedpreview")
      file.src = doc.output('datauristring') + "#view=FitH"
    });
  }

  function getTitulo(){
    var titulos = document.getElementsByClassName('tituloCaptura');
    var titulos_prontos = [];
    for (let i = 0; i < titulos.length; i++) {
      var tituloCompleto = '';
      var titulo = titulos[i];
      if(titulo.tagName=='DIV'){
        filhos_divTitulo = titulo.children;
        var prefixo;
        var tituloCaixa;
        for (let j = 0; j < filhos_divTitulo.length; j++) {
          var filho = filhos_divTitulo[j];
          if(filho.tagName == 'H5'){
            prefixo = filho;
          }else{
            if(filho.tagName == 'TEXTAREA'){
              tituloCaixa = $(tinymce.get(filho.id).getContent())[0];
            }
          }
        }
        if (tituloCaixa == undefined){
          tituloCompleto = document.createElement('div');
          tituloCompleto.appendChild(prefixo.cloneNode(true));
        }
        else{
        tituloCompleto = document.createElement('div');
        tituloCompleto.appendChild(prefixo.cloneNode(true));
        tituloCompleto.appendChild(tituloCaixa);
        }
      }
      else{
        tituloCompleto = titulo;
      }
      titulos_prontos.push(tituloCompleto.outerHTML);
    }
    return titulos_prontos;
  }

  function getConteudo(){
    var divs_secoes = document.getElementsByClassName('conteudoCaptura');
    var conteudosAll = [];
    for (let index = 0; index < divs_secoes.length; index++) {
      var conteudos = []
      var secao = divs_secoes[index];
      var secao_filhos = secao.children;
      for (let j = 0; j < secao_filhos.length; j++) {
        if(secao_filhos[j].tagName == 'TEXTAREA'){
          conteudos.push(tinymce.get(secao_filhos[j].id).getContent());
        }
      }
      conteudosAll.push(conteudos);
    }
    return conteudosAll;
  }