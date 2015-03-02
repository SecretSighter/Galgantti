$(function(){
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
    $(element).stop().animate({
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
    $(element).stop().animate({
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

});

// (function($){
  // $.fn.popout = function(options){
  //   var settings = $.extend(true, {
  //     //default set of options
  //     duration: 50
  //     width: '200px',
  //     height: '200px',
  //     top: '-24px',
  //     left: '-20px'
  //   }, options);

  //   return this.animate({}, settings.duration, function(){

  //   });
  // }

  // $.fn.popin = function(options){
  //   var settings = $.extend(true, {
  //     duration: 50,
  //     width: '200px',
  //     height: '200px',
  //     top: '0px',
  //     left: '0px'
  //   }, options);

  //   return this.animate({settings}, settings.duration, function(){

  //   });
  // }

  
// })(jQuery);
