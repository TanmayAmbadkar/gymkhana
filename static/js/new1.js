jQuery(document).ready(function () {

		//Pagination JS
		//how much items per page to show
		var show_per_page2 = 3;
		//getting the amount of elements inside pagingBox2 div
		var number_of_items = $('#pagingBox2').children().size();
		//calculate the number of pages we are going to have
		var number_of_pages = Math.ceil(number_of_items/show_per_page2);

		//set the value of our hidden input fields
		$('#current_page2').val(0);
		$('#show_per_page2').val(show_per_page2);

		//now when we got all we need for the navigation let's make it '

		/*
		what are we going to have in the navigation?
			- link to previous page
			- links to specific pages
			- link to next page
		*/
		var navigation_html = '<a class="previous_link" href="javascript:previous2();">Prev</a>';
		var current_link = 0;
		while(number_of_pages > current_link){
			navigation_html += '<a class="page_link" href="javascript:go_to_page2(' + current_link +')" longdesc2="' + current_link +'">'+ (current_link + 1) +'</a>';
			current_link++;
		}
		navigation_html += '<a class="next_link" href="javascript:next2();">Next</a>';

		$('#page_navigation2').html(navigation_html);

		//add active_page2 class to the first page link
		$('#page_navigation2 .page_link:first').addClass('active_page2');

		//hide all the elements inside pagingBox2 div
		$('#pagingBox2').children().css('display', 'none');

		//and show the first n (show_per_page2) elements
		$('#pagingBox2').children().slice(0, show_per_page2).css('display', 'block');

});



//Pagination JS

function previous2(){

	new_page = parseInt($('#current_page2').val()) - 1;
	//if there is an item before the current active link run the function
	if($('.active_page2').prev('.page_link').length==true){
		go_to_page2(new_page);
	}

}

function next2(){
	new_page = parseInt($('#current_page2').val()) + 1;
	//if there is an item after the current active link run the function
	if($('.active_page2').next('.page_link').length==true){
		go_to_page2(new_page);
	}

}
function go_to_page2(page_num){
	//get the number of items shown per page
	var show_per_page2 = parseInt($('#show_per_page2').val());

	//get the element number where to start the slice from
	start_from = page_num * show_per_page2;

	//get the element number where to end the slice
	end_on = start_from + show_per_page2;

	//hide all children elements of pagingBox2 div, get specific items and show them
	$('#pagingBox2').children().css('display', 'none').slice(start_from, end_on).css('display', 'block');

	/*get the page link that has longdesc attribute of the current page and add active_page2 class to it
	and remove that class from previously active page link*/
	$('.page_link[longdesc2=' + page_num +']').addClass('active_page2').siblings('.active_page2').removeClass('active_page2');

	//update the current page input field
	$('#current_page2').val(page_num);
}
