(function( $ ){


	$.fn.tazMultiselect = function ( options ) {

		var that = this;

		// tbi
		var settings = {
		};
		if ( options ) {
			$.extend( settings, options );
		}

		var selected_element = '<p>Selected: <span id="active-groups"></span> <a id="show-groups" class="edit" href="#">edit</a></p>';
		var search_element   = '<div class="tazMultiselect-hidable"><strong>Filter:</strong> <input id="multiselect-filter" type="text" /></div>';

		function change_list_of_active_groups () {
			$('#active-groups').text( that.find("input:checkbox:checked").map(function () {
				return $(this).val();
			}).get().join(', '));
		}

		function filter_groups (input) {
			var filter = input.val();
			if ( filter ) {
				that.find(".multiselect-group").show();
				that.find(".multiselect-field").hide();
				that.find(".multiselect-field").filter( function () { return $(this).text().match(new RegExp(filter)) } ).show();
				that.find(".multiselect-group").filter( function () { return $('.multiselect-field:visible',this).length == 0 }).hide();
			}
			else {
				that.find(".multiselect-group").show();
				that.find(".multiselect-field").show();
			}
		}


		this.children('legend').first().after(selected_element + search_element);

		var filter_element   = $( that.find('#multiselect-filter'));

		filter_element.bind('keyup', function () {
			filter_groups($(this));
		});

		filter_element.bind('cut paste', function () {
			window.setTimeout(filter_groups,1,$(this));
		});

		that.find(".multiselect-group").addClass('tazMultiselect-hidable');
		$('.tazMultiselect-hidable').hide();

		this.find("input:checkbox").change(function () {
			change_list_of_active_groups();
		});

		this.find('#active-groups').text( change_list_of_active_groups() );

		this.find('#show-groups').click(function(e) {
			e.preventDefault();
			$(this).toggleClass('edit')
			if ( $(this).hasClass('edit')) {
				$(this).html('edit');
				$('.tazMultiselect-hidable').hide();
			} else {
				$(this).html('hide');
				$('.tazMultiselect-hidable').show();
				filter_groups( filter_element );
			}
		});
		return this;
	}
})( jQuery );

