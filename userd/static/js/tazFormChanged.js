// Idea by http://misterdai.wordpress.com/2010/06/04/jquery-form-changed-warning/

(function( $ ){

	$.fn.tazFormChanged = function(options) {

		var that = this;

		var settings = {
			"changed-function":   function (form,e) {},
			"unchanged-function": function (form,e) {},
		};

		if ( options ) {
			$.extend( settings, options );
		}

		this.data('initialForm', this.serialize());

		this.submit( function(e) {
			if (that.data('initialForm') != that.serialize()) {
				return settings["changed-function"](that,e);
			}
			else {
				return settings["unchanged-function"](that,e);
			}
		});

		return this;
	};
})( jQuery );;
