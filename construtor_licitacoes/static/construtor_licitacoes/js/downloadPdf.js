function baixarPdf(salvar, isSave){
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
    var stringpdf = "<h4>Preambulo</h4>"+textoInicial;
    divconteudo.forEach(element => {
      stringpdf += element
    });
    //console.log(stringpdf)

    var doc = new jsPDF();
    var data = new Date();
    
    var dataAtual = new Date();
    var dataAtual = dataAtual.getDate()+'-'+(dataAtual.getMonth()+1)+'-'+dataAtual.getFullYear();

    doc.fromHTML(stringpdf, // page element which you want to print as PDF
    15,
    15, 
    {
      'width': 170
    },
    function(a) 
    {
        if(isSave){
          doc.save("edital "+ dataAtual.toString()+".pdf","../");
        }
    });

    var bs4 = doc.output('datauristring')
    var saidabs4 = bs4.split(',')
    return saidabs4[1]
  }