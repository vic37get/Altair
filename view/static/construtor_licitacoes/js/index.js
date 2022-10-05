
function statusLicitacao(licitacao,avaliado,id) {
  if(avaliado==0){
    if(licitacao==0){
        document.getElementById("status"+id).setAttribute('class','status pendente fa-solid fa-circle');
        document.getElementById("Labelstatus"+id).innerHTML = "Pendente";
    }

    if(licitacao==1){
        document.getElementById("Labelstatus"+id).innerHTML = "Submetido";
        document.getElementById("status"+id).setAttribute('class','status submetido fa-solid fa-circle');
    }
  }else{
    
    document.getElementById("Labelstatus"+id).innerHTML = "Avaliado";
    document.getElementById("status"+id).setAttribute('class','status avaliado fa-solid fa-circle');
  }

    mostraFeedback(avaliado,id)
  }

  function switchLockEdit(licitacao,id) {
    if(licitacao==0){
        document.getElementById("editar"+id).disabled = false;
        document.getElementById("excluir"+id).disabled = false;
    }
    if(licitacao!=0){
        document.getElementById("editar"+id).disabled = true;
        document.getElementById("excluir"+id).disabled = true;
        
    }

   

  }
  function mostraFeedback(avaliado,id){
    //document.getElementById("modalButton"+id).style.visibility = "hidden";
    if(avaliado==0)
        document.getElementById("modalButton"+id).style.visibility = "hidden";
}

  function atualizaModal(comentariosauditor, indicios_apontados){
    document.getElementById("modalContent").innerHTML = indicios_apontados;
    document.getElementById("modalContent2").innerHTML = comentariosauditor;
    

  }