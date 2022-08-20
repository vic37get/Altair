function createJSON(id) {
    var json = {};
    var titulos = getTitulo();
    var conteudos = getConteudo();
    json['secoes'] = [];
    for (let i = 0; i < titulos.length; i++) {
        json['secoes'].push({'titulo':titulos[i],'conteudo':conteudos[i]})
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
      success: function(data) {
          alert('O Documento foi Salvo.'+data.ajax_resp);
      }
    });
  }