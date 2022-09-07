
function statusLicitacao(licitacao,id) {

    console.log("isso aí mermo: "+licitacao);
    if(licitacao=="pending"){
        document.getElementById("status"+id).style.color = "green" ;
        console.log("status"+id)

    }

    if(licitacao == "submetido" ){
        document.getElementById("status"+id).style.color = "red" ;
        console.log("status"+id)
    }


  }