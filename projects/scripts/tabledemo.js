$(function(){

	var container = $('#table_container');

	$(document).off('click.page', '.previous_page_button').on('click.page', '.previous_page_button', function(){
		var page = parseInt(container.attr('data-page'));
		container.attr('data-page', Math.max(0, page-1));
		$('#table_container').trigger('table_refresh');
	});

	$(document).off('click.page', '.pagination li').on('click.page', '.pagination li', function(){
		var page = parseInt($(event.target).html());
		if(page){
			container.attr('data-page', Math.min(20, page-1));
			$('#table_container').trigger('table_refresh');	
		}		
	});

	$(document).off('click.page', '.next_page_button').on('click.page', '.next_page_button', function(){
		var page = parseInt(container.attr('data-page'));
		container.attr('data-page', Math.min(20, page+1));
		$('#table_container').trigger('table_refresh');
	});

	$('#table_container').on('table_refresh', function(){

		$.ajax({
			url: '/projects/tabledemo.get_table/',
			data: {
				'table_page' : container.attr('data-page')
			}
		}).success(function(data){
				$('#table_container').html(data);
		});
	});

});