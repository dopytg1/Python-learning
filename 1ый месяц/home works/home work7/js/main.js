console.log("hello world");

$('#Modal_reg').on('shown.bs.modal', function () {
    $('#UserName').trigger('focus')
  })