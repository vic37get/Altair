function createJSON(id) {
    var json = {};
    var titulos = getTitulo();
    var conteudos = getConteudo();
    json['secoes'] = [];
    for (let i = 0; i < titulos.length; i++) {
        json['secoes'].push({'titulo':titulos[i].replace(/"/g, "'"),'conteudo':conteudos[i].map(rep)})
    }
    var output = {'json':json,'_id':id};
    return JSON.stringify(output);
}

function saveJSON(id){
    var dataJSON = createJSON(id);
    $.ajax({
      type: 'POST',
      url: '/construcao/salvar',
      data: dataJSON,
      dataType : 'json',
      contentType: 'application/json; charset=utf-8',
      cache: false,
    });
    alert('O Documento foi Salvo.');
  }

function loadJSON(json){
    var jsonDecoded = JSON.parse(decodeEntity(json).replace(/\n\r?/g, ''));
    for (let index = 0; index < jsonDecoded.secoes.length; index++) {novaInstanciaTinyMCE();}
    var sleep = 1000+jsonDecoded.secoes.length*260;
    /*console.log(jsonDecoded);*/
    setTimeout(function(){
        setConteudo(jsonDecoded);
    },sleep);
}

function decodeEntity(inputStr) {
    var textarea = document.createElement("textarea");
    textarea.innerHTML = inputStr;
    return textarea.value;
}

function rep(string){
    return string.replace(/"/g, "'");
}

function setConteudo(jsonDecoded){
    var divs_secoes = document.getElementsByClassName('conteudoCaptura');
    for (let index = 0; index < divs_secoes.length; index++) {
        var secao = divs_secoes[index];
        var secao_filhos = secao.children;
        if(secao_filhos[0].tagName == 'DIV'){
            tinymce.get(secao_filhos[0].children[1].id).setContent($(jsonDecoded.secoes[index].titulo)[0].children[1].outerHTML);
        }
        for (let j = 0; j < secao_filhos.length; j++) {
            if(secao_filhos[j].tagName == 'TEXTAREA'){
                /*console.log(secao_filhos[j].id);
                console.log(jsonDecoded.secoes[index].conteudo[0]);*/
                tinymce.get(secao_filhos[j].id).setContent(jsonDecoded.secoes[index].conteudo[0]);
            }
        }
    }
}