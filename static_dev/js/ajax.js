var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$("#input_search").click(function () {
	criteria = $("#id_querycom").val();
	resultsClothes(criteria)
});

function resultsClothes(criteria) {
	$.ajax({
		beforeSend: function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url: "/shop/clothes/",
		type: "GET",
		data: { criteria: criteria },
		success: function (json) {
			value = "<div class='card' style='width: 18rem;'>" +
				"<img class='card-img-top' src='/media/" + json[0].imagen.toString() + "' alt='Card image cap'>" +
				"<div class='card-body'>" +
				"<h5 class='card-title'>" + json[0].prod.toString() + "</h5>" +
				"<p class='card-text'>Some quick example text to build on the card title and make up the bulk of the card's content.</p>" +
				"</div>" +
				"</div>"
			$('#contenedor_filtrado').html(value);
			// console.log(json[0].producto);
			console.log("Succeded")
		},
		error: function (xhr, errmsg, err) {
			console.log('Error en carga de respuesta');
		},
	});
}


"<div class='card' style='width: 18rem;'>" +
	"<img class='card-img-top' src='/media/'" + json[0].imagen.toString() + "alt='Card image cap'>" +
	"<div class='card-body'>" +
	"<h5 class='card-title'>" + json[0].prod.toString() + "</h5>" +
	"<p class='card-text'>Some quick example text to build on the card title and make up the bulk of the card's content.</p>" +
	"</div>" +
	"</div>"