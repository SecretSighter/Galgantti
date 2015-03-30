$(function(){

  $('#id_upload_file').off('change.uploader').on('change.uploader', function(){
    var fd = new FormData();
    var file = $(this).get(0).files[0];
    fd.append('uploadfile', file);

    $.ajax({
      processData: false,
      contentType: false,
      type: 'POST',
      url: '/projects/fileUpload.upload/',
      data: fd,
      xhr: function(){
        var xhr = jQuery.ajaxSettings.xhr();
        if(xhr.upload){
          $('.progress').remove();
          $('#id_upload_file').after('<div class="progress"><div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;">   60%  </div></div>');
          var progressbar = $( ".progressbar" );
          xhr.upload.addEventListener('progress', function(evt){
            if(evt.lengthComputable){
              var percentComplete = (evt.loaded/evt.total*100).toFixed(2);
              $(".progress-bar").attr('aria-valuenow', percentComplete);
              $(".progress-bar").html(percentComplete+'%');
              $(".progress-bar").css('width', percentComplete+'%');
            }//if
          });//add event listener
        }//if
        return xhr;
      }//xhr
    }).done(function(data){
      $('#id_upload_file').after('<input type="hidden" name="" value="'+data+'" />');
      $('#id_upload_fullName').val(data);
    });//ajax
  });

  $('#id_upload_file').closest('form').off('submit.uploader').on('submit.uploader', function(){
    $('#id_upload_file').remove();
    $('#id_upload_fullName').removeAttr('disabled');
  });//submit
 

});
