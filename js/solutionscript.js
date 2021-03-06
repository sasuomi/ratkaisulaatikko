$(document).ready(function(){
	updateOfferList();

	$('[rel=tooltip]').tooltip({
	    placement: "top",
	    trigger: "focus",
	    width: "200px"
	});

	$(document).on('click', '#submitMessage', function(e) {
    	e.preventDefault();
        $("#messageArea").val('');
        $("#messageArea").unbind(e);

		$.post('ajax/sendnewmessage',
			{},
			function(html) {
				$(".userMessageDiv").show();
			}
		);
	});
    $(document).on('click', '.btn-tarkastele', function(e) {
    	e.preventDefault();

    	$(".modal-body").html('');
		$(".modal-body").addClass('loader');
		$("#offerModal").modal('show')

		$.post('ajax/getofferdetails',
			{offerid: $(this).attr('data-id') },
			function(html) {
				$(".modal-body").removeClass('loader');
				$(".modal-body").html(html);
				$(".userMessageDiv").addClass("text-right");
				$(".userMessageDiv").hide();
			}
		);
	});
});

function updateOfferList() {
	    $(".offerZone").html('Ladataan...');
		$(".offerZone").addClass('loader');
		currentProblemId = getURLParameter('id');
		$.post('ajax/getofferlist',
			{problemid: currentProblemId },
			function(html) {
				$(".offerZone").removeClass('loader');
				$(".offerZone").html(html);
			}
		);
}

function getURLParameter(name) {
	return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
}

