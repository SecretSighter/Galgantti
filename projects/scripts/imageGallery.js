(function($){
  $.fn.popout = function(options){
    var container = $('#image_gallery_container');
    var searchElems = container.find('.oneImageDiv');
    var imageBannerCSS = 'imageBanner';
    var fixedCSS = 'fixed';
    var biggerCSS = 'bigger';

    var duration = 50;

    $(document).on('mouseenter', '.oneImageDiv', function(event){
      var element = event.target;
      $('.'+imageBannerCSS+'').remove();
      $(element).addClass(biggerCSS);
      $(element).parent().addClass(fixedCSS);
      var image = new Object();
      image.title = $(element).attr('title');
      $(element).animate({
        width: '200px',
        height: '200px',
        top: "-24px",
        left: "-20px"
      }, duration, function(){
        $(element).after('<div class="'+imageBannerCSS+'">' + image.title + '</div>');
      });
    });

    $(document).on('mouseleave', '.oneImageDiv', function(event){
      var element = event.target;
      $('.'+imageBannerCSS+'').remove();
      $(element).animate({
        width: '160px',
        height: '160px',
        top: "0px",
        left: "0px"
      }, duration, function(){
        $(element).removeClass(biggerCSS);
        $('.'+imageBannerCSS+'').remove();
        $(element).parent().removeClass(fixedCSS);
      });

    });

    $(document).on('click', '.oneImageDiv', function(event){
      var element = event.target;
      var image = new Object();
      image.title = $(element).attr('title');
      image.filename = $(element).attr('filename');
      window.location = '/projects/getImage?src='+image.filename;
    });

    $(document).on('mouseleave', '.'+imageBannerCSS+'', function(event){
      searchElems.removeClass(biggerCSS);

    });
  }  
})(jQuery);

$(function(){
  $.fn.popout();

});