
function statusLicitacao(licitacao,id) {

    console.log("isso aí mermo: "+licitacao);
    if(licitacao==0){
        document.getElementById("status"+id).setAttribute('class','status pendente fa-solid fa-circle');
        document.getElementById("Labelstatus"+id).innerHTML = "Pendente";
        console.log("status"+id)

    }

    if(licitacao==1){
        document.getElementById("Labelstatus"+id).innerHTML = "Submetido";
        document.getElementById("status"+id).setAttribute('class','status submetido fa-solid fa-circle');
        document.getElementById("editar"+id).setAttribute('visibility','hidden');
        
        console.log("status"+id)

    }


  }