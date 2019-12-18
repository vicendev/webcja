$(document).ready(function(){


$("#idConstruccion").on('click',function(e){
    e.preventDefault();
    $('#idDivTransformacion').hide("slide", {direction: "right"}, 500);
    $('#idDivReparacion').hide("slide", {direction: "right"}, 500);
    $('#idDivDemolicion').hide("slide", {direction: "right"}, 500);

    $('#idDivConstrucion').show("slide", {direction:"left"}, 500);

    fnscroll()
})

$("#idTransformacion").on('click',function(e){
    e.preventDefault();
    $('#idDivConstrucion').hide("slide", {direction: "right"}, 500);
    $('#idDivReparacion').hide("slide", {direction: "right"}, 500);
    $('#idDivDemolicion').hide("slide", {direction: "right"}, 500);

    $('#idDivTransformacion').show("slide", {direction:"left"}, 500);

    fnscroll()
})

$("#idReparacion").on('click',function(e){
    e.preventDefault();
    $('#idDivConstrucion').hide("slide", {direction: "right"}, 500);
    $('#idDivTransformacion').hide("slide", {direction: "right"}, 500);
    $('#idDivDemolicion').hide("slide", {direction: "right"}, 500);

    $('#idDivReparacion').show("slide", {direction:"left"}, 500);

    fnscroll()
})

$("#idDemolicion").on('click',function(e){
    e.preventDefault();
    $('#idDivConstrucion').hide("slide", {direction: "right"}, 500);
    $('#idDivTransformacion').hide("slide", {direction: "right"}, 500);
    $('#idDivReparacion').hide("slide", {direction: "right"}, 500);

    $('#idDivDemolicion').show("slide", {direction:"left"}, 500);

    fnscroll()
})

function fnscroll(){

    $('html,body').animate({scrollTop: $('#scroll_point').offset().top}, 200, function() {
        $('#scroll_point').focus();
        $('#scroll_point').blur()
    })
}

})